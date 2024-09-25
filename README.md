# Trieur-de-jeu

## But

Créer un site web pour ajouter, supprimer, chercher et recommander des jeux du CJ de Télécom SudParis.

## Matériel

Le site est hébergé en CT Debian 12 avec Proxmox

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
cd website/
python3 manage.py migrate
python3 manage.py runserver
```
