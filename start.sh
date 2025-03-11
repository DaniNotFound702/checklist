#!/bin/bash

# Zorg ervoor dat main.py uitvoerbaar is
cd /home/$USER/checklist/
ls
chmod +x main.py
chmod +x prepare.py
python3 -m venv /home/$USER/checklist/.venv/
source /home/$USER/checklist/.venv/bin/activate
pip install -r requirements.txt
echo "everything is ready, you can now use the command '/home/$USER/checklist/.venv/bin/python3 /home/$USER/checklist/main.py' to start the program"