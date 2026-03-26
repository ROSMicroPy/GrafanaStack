# Use the official Python image from Docker Hub as a base
FROM ubuntu:22.04
run apt -y update && apt -y upgrade && apt install -y python3 pip

RUN pip3 install \
    flask \
    opentelemetry-sdk \
    opentelemetry-api \
    opentelemetry-exporter-otlp \
    opentelemetry-instrumentation \
    opentelemetry-instrumentation-requests \
    opentelemetry-instrumentation-flask \
    opentelemetry-distro \   
    opentelemetry-instrumentation-sqlalchemy

RUN opentelemetry-bootstrap -a install

WORKDIR /opt
COPY assets/frontend_app.py /opt/frontend_app.py
COPY assets/backend_app.py /opt/backend_app.py


COPY assets/runAll.sh /opt/runAll.sh
COPY assets/run_FE_App.sh /opt/run_FE_App.sh
COPY assets/run_BE_App.sh /opt/run_BE_App.sh
RUN chmod a+x /opt/run*

# # Command to run the example program
#CMD ["bash", "/opt/runApp.sh"]
CMD ["bash"]
