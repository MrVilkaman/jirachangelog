# coding=utf-8
from .utils import run_command

def get_commit_log(range):
    return run_command("git log --pretty=format:\"%s\" {}".format(range))

def get_stat(range):
    return str(list(run_command("git diff --shortstat {}".format(range)))[0])

def get_current_branch():
    return str(list(run_command('git rev-parse --abbrev-ref HEAD'))[0])
