#!/usr/bin/env python
#*_* coding=utf8 *_*
import os
from publisher import settings, git_update
from publisher.ssh import SSH
from publisher.scp import SCPClient


def pack_update(project="default"):
    # clear old files
    for the_file in os.listdir(settings.export_path):
        file_path = os.path.join(settings.export_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e

    git_update.get_diff(project)


def upload(project="default"):
    files = os.listdir(settings.export_path)
    if len(files) == 0:
        print '---Non file going to upload.'
        return

    print 'SSH BEGIN'
    ssh = SSH(settings.Applications[project]['server_ip'],
              settings.Applications[project]['server_name'],
              settings.Applications[project]['server_passwd'])
    ssh.connect()
    ssh.execute("rm", settings.server_data_path + "/*")
    scp = SCPClient(ssh.ssh.get_transport())
    scp.put(settings.export_path, settings.server_path, recursive=True)
    ssh.close()


def start(argv):
    project = argv[0] if len(argv) else 'default'
    pack_update(project)
    upload(project)

if __name__ == '__main__':
    start()
