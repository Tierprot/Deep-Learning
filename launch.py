#!/usr/bin/python3

import subprocess

subprocess.call("docker run -i --rm -v $(pwd):/home/playground -p 127.0.0.1:8080:8765 base_nn", shell=True)
subprocess.call("docker stop $(docker ps -a -q)", shell=True)
