# coding=utf-8
import os
import subprocess
from collections import Iterator


def run_command(command: str) -> Iterator:
    p = subprocess.Popen(command.split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    strip_ = lambda line: line.decode('UTF-8', errors='ignore').strip().strip("\"")
    return map(strip_, iter(p.stdout.readline, b''))


def safe_print(data: object):
    print(str(data))
