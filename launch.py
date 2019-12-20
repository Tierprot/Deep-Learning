#!/usr/bin/python3
import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--image')

args = parser.parse_args()

subprocess.call("docker run -i --rm -v $(pwd):/home/playground -p 127.0.0.1:8080:8765 {}".format(args.image), shell=True)
subprocess.call("docker stop $(docker ps -a -q)", shell=True)
