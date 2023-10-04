#!/usr/bin/env bash
# Script to install and configure file structure

# update/upgrade either way
sudo apt-get -y update && sudo apt-get -y upgrade

# checks if nginx installed if not, install
if [[ ! $(command -v nginx &> /dev/null) ]];
then
    sudo apt-get install -y nginx
else if [[ $(sudo nginx -t &> /dev/null) ]];
then
    sudo service nginx start
fi

# creates all directories if not exists
mkdir -p /data/web_static/releases/test /data/web_static/shared

# creates and re/write to index.html
cat << EOF > /data/web_static/releases/test/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Nginx</title>
</head>
<body>
    <h1>This is a Test for Nginx config<h1>
</body>
</html>

EOF

# replace sylink if found 
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi

ln -sf /data/web_static/releases/test/ /data/web_static/current

# ownership and group (assuming both exists)
sudo chown -hR ubuntu:ubuntu /data/

# update nginx config to serve the content of /data/web_static/current to URL /hbnb_static path
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart