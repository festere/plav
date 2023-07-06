# Table des matières
1. [Utilisation](#Utilisation)
2. [Création de l'image](#Créationdel'image)

<br>
<br>
<br>


## <a name="Utilisation">Utilisation:<a>
Server web django permettant le téléchargement de fichier ou dossier pour une analyse totalement locale par plusieurs antivirus de façons statiques.

<br>
<br>
<br>

## <a name="Créationdel'image">Création de l'image:<a>
### Mise à jour du systeme
```bash
apt update && upgrade -y
````
```bash
apt-get update
````

<br>

### Installation des applications:
```bash
apt-get install software-properties-common -y
````
```bash
apt install apache2 -y
````
```bash
apt install apache2-dev -y
````
```bash
apt install git -y
````
```bash
apt-get install rabbitmq-server -y
````
```bash
apt install docker.io -y
````
```bash
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
````
```bash
apt install -y python3-pip
````
```bash
apt-get install libapache2-mod-wsgi-py3
````

<br>

### Modification de Apache2:
```bash
cd etc/apache2/sites-available
````
```bash
nano 000-default.conf
````
remove everything and replace it with what's inside: "000-default.conf"

<br>

### Lancement des applications:
```bash
systemctl enable rabbitmq-server
````
```bash
service rabbitmq-server start
````
```bash
service rabbitmq-server status
````
```bash
dockerd
````
Si un problème survient lors du lancement de docker:
```bash
rm -rf /var/snap/docker/179/run/docker.pid
````
```bash
systemctl start docker
````

<br>

### Installation de la plateforme:
```bash
cd var/www/
````
```bash
git clone https://github.com/festere/plav.git
````

<br>

### Création et lancement de l'environnement virtuel:
```bash
pip install virtualenv
````
```bash
virtualenv venv
````
```bash
source venv/bin/activate
````
```bash
pip install -r requirements.txt
````
```bash
pip install django
````

<br>

### Installation de wsgi:
```bash
a2enmod wsgi
````

<br>

### Lancement de la plateforme:
```bash
systemctl restart apache2
````
```bash
celery -A PlateformeAntivirale worker -l info
````
```bash
python3 manage.py runserver
````
