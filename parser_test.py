from parser_1 import parser
from django.db.models import Q
from tokenizer import tokenizer

def project_test():
    jql_string = "project = PROJ"
    q = parser(tokenizer(jql_string))
    q1 = Q(project__key = 'PROJ')

    assert q1==q
    print('JQL Parser - Project test success')

project_test()
    