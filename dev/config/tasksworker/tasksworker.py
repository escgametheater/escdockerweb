#!/usr/bin/python

import setproctitle
import subprocess
import os
import pwd
import sys

# Change title for ps and monitoring
setproctitle.setproctitle('gearman-manager')
# Change user to gcweb
uid = pwd.getpwnam('www-data').pw_uid
os.setuid(uid)
# Run stuff
cmd = ['/usr/local/bin/php',
       '/home/escweb/core/domain/scripts/gearman-manager.php',
       '-c', '/etc/gearman-manager.ini']
cmd.extend(sys.argv[1:])
subprocess.call(cmd)
