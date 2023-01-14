#!/bin/bash

debug_app=$1

#comment when running on Docker for some reason
echo "starting virtual env"
python3 -m venv venv
source venv/bin/activate
echo "virtual env started"
#comment when running on Docker for some reason
echo "installing requirements..."
pip3 install -r requirements.txt
echo "requirements installed"
echo "exporting variables"
export FLASK_APP=./piip_ipn_api/piip_api.py
if [ -z $debug_app ] || [ $debug_app = 1 ]
then
    echo "debug enabled"
    export FLASK_DEBUG=true
else
    echo "debug disabled"
    export FLASK_DEBUG=false
fi
export FLASK_RUN_PORT=5000
export FLASK_RUN_HOST=0.0.0.0
echo "about to start flask"
python3 ./piip_ipn_api/piip_api.py
echo "flask started"
