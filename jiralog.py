# coding=utf-8
import argparse

from utils.git import *
from utils.jirautils import *
from utils.utils import *


# *** MAIN ***

def main():
    check_env()

    arg = parse_path()

    command = get_commit_log(arg.path)
    ids = parse_jira(command)
    tasks = fill_report(ids)
    # tasks = fill_report_stub(ids)

    print_changelog_header(get_app_name(arg), arg.version)
    groupby = {}
    tasks = sorted(tasks, key=lambda g: g.issuetype, reverse=False)

    for key, group in itertools.groupby(tasks, key=lambda element: element.issuetype):
        groupby[key] = list(group)
        # safe_print(key)

    print_block(groupby, TASK_TYPE_TASK)
    print_block(groupby, TASK_TYPE_BUG)
    print_block(groupby, TASK_TYPE_REFACTOR)
    print_block(groupby, TASK_TYPE_OTHER)

    print_changelog_footer(get_current_branch(), get_stat(arg.path))

    print ("\n*** DEBUG *** ")
    print (create_issues_link(list(map(lambda card: str(card.id), tasks))))


def parse_path():
    parser = argparse.ArgumentParser(description='Great Description To Be Here')
    parser.add_argument("--path", "-p", type=str, default="origin/master..HEAD",
                        help='Begin and end commits for git e.g. origin/master..HEAD')

    parser.add_argument("--version", "-v", type=str, default="5.xx")

    parser.add_argument("--appname", "-a", type=str)
    parser.add_argument("--skyeng", "-s", action='store_true')
    parser.add_argument("--teachers", "-t", action='store_true')

    return parser.parse_args()


def get_app_name(arg):
    appname = arg.appname
    if appname is not None:
        return appname

    if arg.skyeng:
        return "Skyeng"

    if arg.teachers:
        return "Teachers"

    return "Skyeng"


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interupted. Bye")
        exit(127)
