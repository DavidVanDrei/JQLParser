from tokenizer import tokenizer
from django.db.models import Q



def parser(tokens):

        # JQL format -> field operator value | jql
    fields = ['project']
    operators = ['=', '>=', '<=']

    jqlField2QField = {
        'project': 'project__key'
    }

    query_dict = {
   'project__key': 'PROJ',
    }

    if len(tokens)<3: return None
    field = tokens[0]
    operator = tokens[1]
    value = tokens[2]

    if operator == '=':
        query_dict = {
            jqlField2QField[field]: value
        }

    return Q(**query_dict)  

        




# jql_string = "project = PROJ"
# q = parser(tokenizer(jql_string))


