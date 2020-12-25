#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"
CWD=$PWD

# Create venv
cd "${CWD}"
virtualenv -p /usr/bin/python3 .env
source .env/bin/activate

# Install requirements
cd "${CWD}"
pip3 install --upgrade pip
python3 --version
pip3 --version
pip3 install -r requirements.txt

echo "SETUP SUCCESSFUL!"
