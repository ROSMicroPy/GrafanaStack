from flask import Flask, request, jsonify
import requests
import logging
from random import randint
import os

# Configure logging first
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# OpenTelemetry setup (optional - only if not disabled)
otel_enabled = os.getenv("OTEL_SDK_DISABLED", "false").lower() != "true"

if otel_enabled:
    try:
        # OpenTelemetry imports
        from opentelemetry import trace, metrics
        from opentelemetry.instrumentation.requests import RequestsInstrumentor
        from opentelemetry.instrumentation.flask import FlaskInstrumentor
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        from opentelemetry.sdk.metrics import MeterProvider
        from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

        # Set up resource attributes for service identification
        resource = Resource.create(attributes={"service.name": "backend-service"})

        # Configure tracing
        trace.set_tracer_provider(TracerProvider(resource=resource))
        tracer = trace.get_tracer(__name__)
        otel_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "otel-collector:4317")
        # Remove http:// prefix if present (gRPC doesn't need it)
        otel_endpoint = otel_endpoint.replace("http://", "").replace("https://", "")
        span_exporter = OTLPSpanExporter(endpoint=otel_endpoint, insecure=True)
        span_processor = BatchSpanProcessor(span_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)

        # Instrument Flask and Requests automatically
        FlaskInstrumentor().instrument_app(app)
        RequestsInstrumentor().instrument()

        # Configure metrics
        meter_provider = MeterProvider(
            resource=resource,
            metric_readers=[
                PeriodicExportingMetricReader(ConsoleMetricExporter())
            ]
        )
        metrics.set_meter_provider(meter_provider)
        meter = metrics.get_meter(__name__)
        # Create a counter metric to count backend calls
        backend_call_counter = meter.create_counter(
            "backend.call.count", description="Number of calls to the backend service"
        )
        
        logger.info("OpenTelemetry instrumentation enabled")
    except Exception as e:
        logger.warning(f"Failed to initialize OpenTelemetry: {e}. Continuing without telemetry.")
        otel_enabled = False
        tracer = None
        backend_call_counter = None
else:
    logger.info("OpenTelemetry disabled via OTEL_SDK_DISABLED")
    tracer = None
    backend_call_counter = None

@app.route("/roll-dice")
def roll_dice():
    # Increment the counter metric each time the endpoint is called (if OTEL enabled)
    if backend_call_counter:
        backend_call_counter.add(1)
    
    # Get player name
    try:
        player = request.args.get('player', default=None, type=str)
    except Exception as e:
        player = None
        logger.error(f"Error getting player parameter: {e}")

    # Generate dice roll
    result = str(randint(1, 6))

    # Log the roll
    if player:
        logger.warning("%s is rolling the dice: %s", player, result)
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    
    return result


if __name__ == "__main__":
    app.run(port=9090)
