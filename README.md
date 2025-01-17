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
git submodule update --init --remote #uniquement si vous avez accès au répertoire images
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Pour mettre à jour le répertoire

```sh
git submodule update --remote #uniquement si vous avez accès au répertoire images
git pull
```

## Lancer le serveur

```sh
cd website/
python3 manage.py migrate
python3 manage.py add_games # Si toujours pas ajouté
python3 manage.py add_extensions # Idem
python3 manage.py runserver
```
