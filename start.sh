#!/bin/bash

source ./piip_ipn_api/venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=./piip_ipn_api/api.py
export FLASK_DEBUG=$1
flask run
