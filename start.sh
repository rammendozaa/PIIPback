#!/bin/bash

echo "installing requirements"
pip3 install -r requirements.txt
echo "requirements installed"
echo "exporting variables"
export FLASK_APP=./piip_ipn_api/piip_api.py
export FLASK_DEBUG=$1
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
echo "about to start flask"
python3 ./piip_ipn_api/piip_api.py
echo "flask started"
