#!/bin/bash

# Zorg ervoor dat main.py uitvoerbaar is
cd /home/owhat/checklist/
chmod +x main.py
chmod +x save.py
chmod +x prepear.py
python3 -m venv /home/owhat/checklist/.venv/
source home/owhat/checklist/.venv/bin/activate
pip install -r requirements.txt
/home/owhat/checklist/.venv/bin/python3 /home/owhat/checklist/main.py # Voer het Python-script uit
