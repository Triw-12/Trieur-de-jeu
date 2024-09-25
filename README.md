# Trieur-de-jeu

Utilisation d'un CT debian 12 avec proxmox

## Installation

```sh
apt update
apt install git python3 python3-pip python3-venv
git clone https://github.com/Triw-12/Trieur-de-jeu.git
cd Trieur-de-jeu/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Lancer le serveur

```py
python3 manage.py migrate
python manage.py runserver
```
