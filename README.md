![](https://img.shields.io/badge/AV-red?style=for-the-badge)
![](https://img.shields.io/badge/linux-green?style=for-the-badge)
![](https://img.shields.io/badge/unix-gray?style=for-the-badge)

<br>

# Table of contents
1. [Disclaimer](#Disclaimer)
2. [Description](#Description)
3. [Installation](#Installation)
   
<br>
<br>
<br>
<br>

# <a name="Disclaimer">Disclaimer:</a>
<span style="color:red">Before using any of our application(s) and/or sevice(s), please ensure that you have read and understood our license, terms of use (in the license), and copyright policy (in the license). By using our application(s) and/or sevice(s), you agree to comply with all applicable laws and regulations, and to be bound by our license, terms of use, and copyright policy. If you do not agree with any part of these documents, you must not use our app or services. Please note that our license, terms of use, and copyright policy are subject to change without notice, and it is your responsibility to periodically review these documents for any updates or changes.</span>
   
<br>
<br>
<br>
<br>

# <a name="Description">Description:<a>
Django web server with apache to analyze files thanks to multiple AV in static.

<br>
<br>
<br>
<br>

# <a name="Installation">Installation:<a>

```bash
sudo su
````
```bash
if [ ! -d "/var/www" ]; then mkdir /var/www; fi
````
```bash
apt install git -y
````
```bash
git clone https://github.com/festere/plav.git /var/www/plav
````
```bash
cd /var/www/plav/
````
```bash
chmod +x download.sh
````
```bash
./download.sh
````
