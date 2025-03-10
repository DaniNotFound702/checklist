#!/bin/bash

# Zorg ervoor dat main.py uitvoerbaar is
chmod +x main.py
chmod +x save.py
chmod +x prepear.py
python3 -m venv checklist
/home/owhat/checklist/.venv/bin/python3 /home/owhat/checklist/main.py # Voer het Python-script uit
