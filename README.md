# Table des matières
1. [Utilisation](#Utilisation)
2. [Création de l'image](#Créationdel'image)
3. [Installation de l'image](#Installationdel'image)

<br>
<br>
<br>


## <a name="Utilisation">Utilisation:<a>
Server web django permettant le téléchargement de fichier ou dossier pour une analyse totalement locale par plusieurs antivirus de façons statiques.

<br>
<br>
<br>

## <a name="Créationdel'image">Création de l'image:<a>
### Création du docker:
```bash 
apt install docker.io
```
```bash 
sudo dockerd
```
```bash 
docker pull debian
```
```bash
docker run -t -p 8000:8000 --privileged --name plateforme-antiviral debian
```
```bash 
docker exec -it Plateforme-Antiviral /bin/bash
```

<br>
<br>

### Installation de git:
```bash 
apt install git
```
```bash 
git clone https://github.com/festere/Plateforme-Antivirale.git
```

<br>
<br>

### Installation et lancement de Rabbit-mq
```bash 
apt-get install rabbitmq-server -y
```

<br>

```bash 
systemctl enable rabbitmq-server
```
```bash 
systemctl start rabbitmq-server
``` 
```bash 
systemctl status rabbitmq-server
``` 
OR
```bash 
service rabbitmq-server start
``` 
```bash 
service rabbitmq-server status
```

<br>
<br>

### Installation et lancement de Docker:
```bash
apt install docker.io
```

<br>

```bash 
systemctl start docker
``` 
```bash
systemctl status docker
```
OR
```bash 
sudo dockerd
```

<br>
<br>

### Installation de pip et des librairies python:
```bash 
apt install pip -y
```
```bash
cd Plateforme-Antiviral
```
``` bash
pip install -r requirements.txt
```

<br>
<br>
<br>

## <a name="Installationdel'image">Installation de l'image:<a>
### Création du docker:
```bash 
apt install docker.io
```
```bash 
sudo dockerd
```
```bash 
docker pull festere/plateforme-antiviral
``` 
```bash 
docker run -t -p 8000:8000 --privileged --name plateforme-antiviral festere/plateforme-antiviral
``` 
```bash 
docker exec -it plateforme-antiviral /bin/bash
```

<br>
<br>

### Pour démarer le server il faut:
```bash 
sudo dockerd
```
```bash 
cd Plateforme-Antiviral
```
```bash 
celery -A PlateformeAntivirale worker -l info
```
```bash 
python3 manage.py runserver
```
