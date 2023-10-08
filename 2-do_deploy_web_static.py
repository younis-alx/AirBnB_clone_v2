#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers"""
from fabric.api import *
from os import path


env.hosts = ['100.26.235.153', '52.91.118.87']


def do_deploy(archive_path):
    """deploys the archives to server"""
    try:
        if not (path.exists(archive_path)):
            return False

        # uploading the archive
        put(archive_path, "/tmp/")

        # uncompress the archive
        parts = archive_path.split('_')
        time_stamp = parts[2].split(".")[0]
        sudo("sudo rm -rf /data/web_static/releases/\
web_static_{}".format(time_stamp))
        sudo("sudo mkdir -p /data/web_static/releases/\
web_static_{}".format(time_stamp))
        sudo("sudo tar -xvf /tmp/web_static_{}.tgz -C /data/\
web_static/releases/web_static_{}".format(time_stamp, time_stamp))

        # delete the archive from web_server
        sudo("sudo rm -rf /tmp/web_static_{}.tgz".format(time_stamp))

        # delete the symbolic link
        sudo("sudo rm -rf /data/web_static/current")

        # create a new symblolic link
        sudo("sudo ln -sf /data/web_static/releases/\
web_static_{} /data/web_static/current".format(time_stamp))

        return True
    except Exception as e:
        return False
