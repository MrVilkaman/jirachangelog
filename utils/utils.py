# coding=utf-8
import os
import subprocess


def check_env():
    if not (os.getenv('_JIRA_LOGIN') and os.getenv('_JIRA_PASSWORD')):
        print("E: LOGIN or PASSWORD is empty")
        print("E: do `source ./env.sh`")
        exit(1)

# return массив строк
def run_command(command):
    # type: (object) -> object
    p = subprocess.Popen(command.split(),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    strip_ = lambda line: line.decode('UTF-8', errors='ignore').strip().strip("\"")
    return map(strip_, iter(p.stdout.readline, b''))


def safe_print(data):
    # can also use 'replace' instead of 'ignore' for errors= parameter
    print(str(data).encode('UTF-8', errors='ignore').decode('cp1251', errors='ignore'))
