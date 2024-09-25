# Trieur-de-jeu
Utilisation d'un CT debian 12 avec proxmox.

# Installation des packets primaires
apt update
apt install python3 python3-pip python3-venv git


mkdir webserver
cd webserver/

python3 -m venv .

bin/pip install django


django-admin startproject mysite


# Launch the server
python manage.py runserver