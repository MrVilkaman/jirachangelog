# coding=utf-8

import itertools
import re

from .models import *
from .utils import safe_print


def print_changelog_header(appNamem, versionName):
    safe_print("Сборка: :android: {} `{}` доступна в Firebase.".format(appNamem, versionName))
    print()
    safe_print("Список изменений:")


def type_as_emoji(self):
    type = str(self).strip()

    return {
        "Task": TASK_TYPE_TASK,
        "Задача": TASK_TYPE_TASK,
        "▒стория": TASK_TYPE_TASK,
        "История": TASK_TYPE_TASK,
        "Ошибка": TASK_TYPE_BUG,
        "Bug": TASK_TYPE_BUG,
        "Bug subtask": TASK_TYPE_BUG,
        "Refactoring task": TASK_TYPE_REFACTOR
    }.get(type, TASK_TYPE_DONT_KNOW)


def print_block(groupby, type_task):
    task_ = groupby.get(type_task, None)

    if task_ is None:
        return
    safe_print(get_type_block_title(type_task))
    print("```")

    for line in task_:
        safe_print(line)

    print("```")
    print()


def get_type_block_title(type):
    title = {TASK_TYPE_TASK: "Фичи", TASK_TYPE_BUG: "Баги", TASK_TYPE_REFACTOR: "Рефакторинг", TASK_TYPE_DONT_KNOW: "Остальное"}.get(type, None)

    if title is None:
        return "Другое"

    return "{} {}".format(type, title)


def print_changelog_footer(branch_name, stat):
    safe_print("*Собрано из:* `{}`".format(branch_name))
    safe_print(stat)
    print()
    safe_print("*Тестирует:* @mobile-qa-team")
    safe_print("сс @ak @golubtsov @mobile-platform-android @zykova @mobilesupport")


def __find_jira(line):
    jira = re.findall("\[(?:.*?)\]|(?:(?:MV|MOB|MP|COM|VIM)-\d{1,5})", line)
    if not jira:
        return RawGitItem(EMPTY_ID, line)

    return RawGitItem(filter_git_id(jira[0]), line)


def parse_jira(p_line):
    gitItems = sorted(map(__find_jira, p_line), key=lambda g: g.id, reverse=True)

    groupby = []
    for key, group in itertools.groupby(gitItems, key=lambda item: item.id):
        if key is not EMPTY_ID:
            groupby.append(list(group)[0])

    for item in gitItems:
        if item.id is EMPTY_ID:
            groupby.append(item)

    return groupby


def is_valid_git_comment(rawStr, type):
    if type == TASK_TYPE_OTHER:
        if re.search("Merge (pull request|remote-tracking branc|branch)", rawStr):
            return False

        if re.search("Попривил тесты", rawStr):
            return False

        if re.search("fix", rawStr):
            return False

    return True


def filter_git_comment(rawStr):
    return re.sub("(\[Android\]|Android:)|^:", "", rawStr)

def filter_git_id(rawStr):
    sub = re.sub("\[", "", rawStr)
    return re.sub("\]", "", sub)