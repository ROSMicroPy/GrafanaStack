FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive  

RUN apt update -y
RUN apt install -y apt-transport-https software-properties-common wget w3m nano

RUN mkdir -p /etc/apt/keyrings/
RUN wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | tee /etc/apt/keyrings/grafana.gpg > /dev/null
RUN echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | tee -a /etc/apt/sources.list.d/grafana.list

# Updates the list of available packages
RUN apt -y update

# Installs the latest OSS release:
RUN apt install -y mimir

COPY assets/mimir-config.yaml /etc/mimir/mimir-config.yaml

#CMD ["mimir"]
CMD ["mimir", "-config.file", "/etc/mimir/mimir-config.yaml"]
