
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
#export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=http://otelcol:4317/v1/traces
#export OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=http://otelcol:4317/v1/metrics
#export OTEL_EXPORTER_OTLP_LOGS_ENDPOINT=http://otelcol:4317/v1/logs
#export OTEL_EXPORTER_OTLP_ENDPOINT=http://otelcol:4317

export FLASK_APP=frontend_app.py
opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp,console \
    --service_name dice-fe-server \
    flask run -p 8080 --host=0.0.0.0
