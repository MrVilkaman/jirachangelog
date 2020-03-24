# coding=utf-8

TASK_TYPE_TASK = ":metal:"
TASK_TYPE_BUG = ":buggy:"
TASK_TYPE_REFACTOR = ":gear:"
TASK_TYPE_OTHER = ""

EMPTY_ID = ""

class RawGitItem:
    def __init__(self, id, comment):
        self.id = id
        self.comment = comment

    def __str__(self):
        return "[{}] == {}".format(self.id, self.comment)


class ReportItem:
    def __init__(self, id, summary, issuetype):
        self.id = id
        self.summary = summary
        self.issuetype = issuetype

    def __str__(self):
        if self.id == EMPTY_ID or self.issuetype == TASK_TYPE_OTHER:
            return self.summary

        return "[{}] {}".format(self.id, self.summary)
