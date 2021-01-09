#!/bin/bash
#coding=utf-8

set -euo pipefail

# to enable remote execution
cd "$(dirname "$0")"
CWD=$PWD

source .env/bin/activate
python src/main.py
