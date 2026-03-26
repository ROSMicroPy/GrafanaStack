#!/bin/sh

echo "starting otelcol"
#source /etc/otelcol.env
env
/bin/otelcol-contrib --config=/etc/otelcol/config.yaml 
wait
echo "otelcol terminated"