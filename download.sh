# Update the system:
apt update && upgrade -y
apt-get update 

# Download the apps:
apt-get install software-properties-common -y
apt install apache2 -y
apt install apache2-dev -y
apt-get install rabbitmq-server -y
apt install docker.io -y
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
apt install python3-pip -y
apt-get install libapache2-mod-wsgi-py3 -y

# Modify Apach2:
source_file="000-default.conf"
destination_folder="/etc/apache2/sites-available"
cp "$source_file" "$destination_folder/000-default.conf"
systemctl restart apache2

# Start the apps:
systemctl enable rabbitmq-server
service rabbitmq-server start
rm -rf /var/snap/docker/179/run/docker.pid
systemctl start docker

# Create the virtual env for the plateforme:
pip install virtualenv
virtualenv venv

source_path="venv/bin/activate"
if [ -f "$source_path" ]; then
    # Execute the activation script directly
    . "$source_path"
    echo "Virtual environment activated."
else
    echo "Virtual environment not found."
fi

pip install --upgrade pip
pip install -r requirements.txt

# Install wsgi:
a2enmod wsgi

# Enable Apache mods
sudo a2enmod proxy
a2enmod proxy_http
