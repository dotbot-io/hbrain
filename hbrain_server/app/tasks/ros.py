from Flask import current_app
from .. import sse

from . import celery
import subprocess

class RosEnv:
    def __init__(self, sp):
        import json
        source = 'source ' + sp
        dump = 'python -c "import os, json;print json.dumps(dict(os.environ))"'
        pipe = subprocess.Popen(['/bin/bash', '-c', '%s && %s' %(source,dump)], stdout=subprocess.PIPE, env={})
        env_info =  pipe.stdout.read()
        self._env = json.loads(env_info)

    def get_env(self):
        return self._env

env = RosEnv('/opt/ros/indigo/setup.bash')

@celery.task()
def run_shell(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env.get_env())
    while True:
        line = p.stdout.readline()
        if line != '':
            line = line.rstrip()
            sse.publish({"message": line}, type=cmd[0])
        else:
            sse.publish({"message": 'STOP'}, type=cmd[0])
            break
