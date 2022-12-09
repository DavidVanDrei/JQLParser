from jira import JIRA
from parser_1 import parser
from django.db.models import Q
from tokenizer import tokenizer


def signIn():
# Create a JIRA instance
    jira = JIRA(server="https://jira.atlassian.com")

    # Search for issues
    jql = "project = ANALYTICS"
    issues = jira.search_issues(jql)
    q = parser(tokenizer(jql))

    print(q)

    # Print the issue keys
    for issue in issues:
        print(issue.key)

signIn()


