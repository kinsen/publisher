import sys
import os
from subprocess import call
from datetime import datetime

TOP_DIR = os.path.dirname(__file__)
if TOP_DIR == "":
    TOP_DIR = os.getcwd()

DATA_DIR = os.path.join(TOP_DIR, "data")  # you can set other path too.
TARGET_DIR = sys.argv[1] if \
    len(sys.argv) >= 2 else '/home/solidai/install/install'  # this path is the web app's install path
BACKUP_DIR = os.path.join(TOP_DIR, "backup")  # you can set other path too.

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def backup(project):
    current_version = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = "%s_%s.tar.gz" % (project_name, current_version)
    backup_dir = os.path.join(BACKUP_DIR, backup_name)
    call(['tar', '-czf', backup_dir, '-C', TARGET_DIR, project_name])  # backup

tar_list = [filename for filename in os.listdir(DATA_DIR)
            if filename.endswith("tar.gz")]

for tar in tar_list:
    project_name = ".".join(tar.split(".")[:-2])
    target_dir = os.path.join(TARGET_DIR, project_name)
    tar_path = os.path.join(DATA_DIR, tar)
    backup(project_name)
    call(["mkdir", "-p", target_dir])
    call(["tar", "-xf", tar_path, "-C", target_dir])


################ INSTALL PACKAGES ######################

apt_packages = ["python-setuptools", "python-eventlet", "python-mysqldb",
                "python-redis"]

for pkg in apt_packages:
    call(["apt-get", "-y", "install", pkg])


packages = ['solidai_sdk', 'solidai_api_sdk', 'solidai_bill',
            'solidai_dash', 'solidai_invest', 'solidai_notice',
            'solidai_ucenter', 'solidai_web', 'solidai_items',
            'solidai_ucenter_web']

for pkg in packages:
    target_dir = os.path.join(TARGET_DIR, pkg)
    if os.path.exists(target_dir):
        os.chdir(target_dir)
        call(["python", "setup.py", "develop"])

