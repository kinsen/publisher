#!/usr/bin/env python
#*_* coding=utf8 *_*
import os
import re
from publisher import command, settings

packages = settings.git_projects

def get_diff():
    for top_path, pkgs in packages.items():
        for pkg in pkgs:
            git_path = os.path.join(top_path, pkg)
            os.chdir(git_path)
            result = command.execute("git", "status")
            print '----------------------------------------------------'
            # regex=re.compile(r'modified:\s+([\w/\.]+)\n#')
            regex = re.compile(r'#\t(.+)\n')
            m = regex.findall("".join(result))
            files = map(lambda x: re.sub(r'\w+:\s+', '', x), m)
            if len(files):
            	target_path = os.path.join(settings.export_path, "%s.tar.gz" % pkg)
            	command.execute("tar", "-czf", target_path, *files)


if __name__ == '__main__':
    get_diff()
