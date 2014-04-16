#!/usr/bin/python2.6

import subprocess
import urllib
import jcc
import os.path

linkdir = os.path.split(os.path.split(jcc.__file__)[0])[0]

subprocess.call('sudo ln -s ' + linkdir + '/libjcc.dylib ' + '/usr/local/lib',shell=True)

urllib.urlretrieve("https://github.com/ChristopherLucas/txtorg/archive/master.zip", "/tmp/master.zip")
import os
subprocess.call('sudo unzip /tmp/master.zip -d /tmp; cd /tmp/txtorg-master;  sudo sed "1s/python/python2\.6/" /tmp/txtorg-master/setup.py > /tmp/txtorg-master/newsetup.py; sudo mv /tmp/txtorg-master/newsetup.py /tmp/txtorg-master/setup.py; sudo python2.6 /tmp/txtorg-master/setup.py install',shell=True)
