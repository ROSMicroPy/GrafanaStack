#FROM grafana/tempo:latest
FROM ubuntu:22.04
ARG TEMPO_VER=2.10.5

RUN mkdir -p /etc/tempo

#COPY assets/tempo/tempo.yml /etc/tempo/config.yml

RUN apt -y update && apt -y upgrade
RUN apt -y install dpkg curl wget nano iputils-ping systemd 


WORKDIR /opt
RUN curl -Lo tempo_${TEMPO_VER}_linux_aarch64.deb https://github.com/grafana/tempo/releases/download/v${TEMPO_VER}/tempo_${TEMPO_VER}_linux_arm64.deb
RUN curl -Lo tempo_${TEMPO_VER}_linux_x86_64.deb https://github.com/grafana/tempo/releases/download/v${TEMPO_VER}/tempo_${TEMPO_VER}_linux_amd64.deb
RUN dpkg -i tempo_${TEMPO_VER}_linux_`uname -m`.deb

COPY assets/config.yml /etc/tempo/config.yml
COPY assets/config.yml /opt/config.yml

WORKDIR /opt
COPY assets/runTempo.sh /opt/runTempo.sh
RUN chmod a+x /opt/runTempo.sh
CMD ["bash", "/opt/runTempo.sh"]
