# Trieur-de-jeu
Utilisation d'un CT debian 12 sous proxmox.

# Installation des packets primaires
apt install python3-django python3 python3-pip mariadb-common python3-venv mariadb-server pkg-config


mkdir webserver
cd webserver/
python3 -m venv .

bin/pip install mysqlclient
