#!/bin/bash
set -e

python3 -m pip install --upgrade pip
pip install paver coverage radon

paver
