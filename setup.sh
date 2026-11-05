#!/bin/bash

# create virtual environment
python3 -m venv .venv

# activate virtual environment 
source .venv/bin/activate

echo -e "[INFO:] Installing necessary requirements..."

# install reqs
python3 -m pip install -r requirements.txt

# deactivate env 
deactivate

echo -e "[INFO:] Setup complete!"