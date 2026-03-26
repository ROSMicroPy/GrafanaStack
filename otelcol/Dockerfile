# Use the official Python image from Docker Hub as a base
#FROM python:3.10-slim
FROM ubuntu:22.04

ARG OTEL_VER=0.135.0
ARG OTELCOL_CONFIG_PATH
ARG CREATE_COMPRESS_CRON=false
# Update and install system dependencies
RUN rm -rf /var/lib/apt/lists/* && \
    apt clean && \
    apt update --allow-insecure-repositories --allow-unauthenticated && apt install -y --allow-unauthenticated \
    curl \
    vim \
    iputils-ping \
    wget \ 
    systemctl \
    nano \
    links \
    tree \
    tcpdump \
    less \
    && apt clean

WORKDIR /opt
RUN wget -q -O otelcol_aarch64.deb https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v${OTEL_VER}/otelcol-contrib_${OTEL_VER}_linux_arm64.deb &&\
    wget -q -O otelcol_x86_64.deb https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v${OTEL_VER}/otelcol-contrib_${OTEL_VER}_linux_amd64.deb && \
    dpkg -i otelcol_`uname -m`.deb && \
    rm otelcol_aarch64.deb && rm otelcol_x86_64.deb

COPY ${OTELCOL_CONFIG_PATH}/config.yaml /etc/otelcol/config.yaml 
COPY ${OTELCOL_CONFIG_PATH}/otelcol.conf /etc/otelcol/otelcol.conf 

# RUN if [ "$CREATE_COMPRESS_CRON" = "true" ]; then \
#     echo "* * * * * root bash -c "find \$OTEL_EXPORT_BASE/metrics -name 'metrics-*.json' -exec gzip {} \;" >> /etc/cron.d/otel.file.compress.cron" && \
#     echo "* * * * * root bash -c "find \$OTEL_EXPORT_BASE/logs -name 'logs-*.json' -exec gzip {} \;" >> /etc/cron.d/otel.file.compress.cron" && \
#     echo "* * * * * root bash -c "find \$OTEL_EXPORT_BASE/traces -name 'traces-*.json' -exec gzip {} \;" >> /etc/cron.d/otel.file.compress.cron" && \
#     chmod 0644 /etc/cron.d/otel.file.compress.cron; \
# else \
#     echo "No compress cron created"; \
# fi

# Oreoare for incoming logs
RUN mkdir -p /mnt/comcol/logs

# Oreoare for incoming logs
RUN mkdir -p /var/log/otel-collector
#COPY assets/config.yaml /etc/otelcol/config.yaml 
RUN mkdir -p /var/lib/otelcol/file_storage/logs

# Copy applog certs for OpenSearch exporter (if they exist)
RUN mkdir -p /etc/applog


# Prepare for incoming logs
RUN mkdir -p /var/log/otel-collector

# Set the working directory to /app
WORKDIR /opt
COPY assets/startup.sh /opt/startup.sh
# Command to run the example program
RUN chmod a+x /opt/startup.sh
CMD ["/opt/startup.sh"]
#CMD ["bash"]
