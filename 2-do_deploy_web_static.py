#!/usr/bin/pyton3
""" fabfiles to stramline data to """

import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ['100.26.235.153', '52.91.118.87']

def do_deploy(archive_path):
y(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if sudo("rm /tmp/{}".format(file)).failed is True:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/current").failed is True:
        return False
    if sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
