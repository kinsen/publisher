#!/usr/bin/env python
#*_* coding=utf8 *_*

import paramiko


class SSH(object):

    def __init__(self, ip, username, passwd, timeout=5):
        self._ip = ip
        self._username = username
        self._passwd = passwd
        self._timeout = timeout

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self._ip,
                         22,
                         self._username,
                         self._passwd,
                         timeout=self._timeout)

    def execute(self, *cmd):
        command = " ".join(cmd)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        out = stdout.readlines()
        for line in out:
            print line
        return out

    def close(self):
        print '%s\t SSH CLOSE\n' % self._ip
        try:
            self.ssh.close()
            self.ssh = None
        except Exception, e:
            print e

    def __del__(self):
        if self.ssh:
            self.close()


if __name__ == '__main__':
    from publisher.scp import SCPClient
    print 'begin'
    ssh = SSH('solidai.net', 'solidai', '1234567890)(*&^%$#@!')
    ssh.connect()
    scp = SCPClient(ssh.ssh.get_transport())
    scp.put('/home/kong/project/publisher/data',
            'publisher/data', recursive=True)
    # ssh.execute("cal")
    # ssh.execute("touch hello.txt")
    ssh.close()
