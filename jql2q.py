# from django.db.models import Q
import re
from tokenize import tokenizer 
from parser import parse

def jql_to_q(jql):
    # Tokenize JQL query
    tokens = tokenizer(jql)

    # Parse tokens into abstract syntax tree
    ast = parse(tokens)
    print(ast)

    # # Convert abstract syntax tree to Django Q expression
    # q = convert_to_q(ast)

    return None

# def convert_to_q(ast):
#     # Create empty Q object
#     q = Q()

#     # Iterate through nodes in abstract syntax tree
#     i = 0
#     while i < len(ast):
#         node = ast[i]

#         # If node is a field, add it to the Q object
#         if node['type'] == 'field':
#             field = node['value']

#             # Get operator and value from next two nodes
#             operator = ast[i+1]['value']
#             value = ast[i+2]['value']

#             # Add expression to Q object
#             if operator == '=':
#                 q &= Q(**{field: value})
#             elif operator == '!=':
#                 q &= ~Q(**{field: value})
#             elif operator == '>':
#                 q &= Q(**{field + '__gt': value})
#             elif operator == '<':
#                 q &= Q(**{field + '__lt': value})
#             elif operator == '>=':
#                 q &= Q(**{field + '__gte': value})
#             elif operator == '<=':
#                 q &= Q(**{field + '__lte': value})

#             i += 3

#         # If node is a boolean, add it to the Q object
#         elif node['type'] == 'boolean':
#             boolean = node['value']

#             # Add expression to Q object
#             if boolean:
#                 q &= convert_to_q(ast[i+1:])
#             else:
#                 q &= ~convert_to_q(ast[i+1:])

#             return q

#         # If node is a parentheses, skip it
#         elif node['type'] == 'parentheses':
#             i += 1

#         i += 1

#     return q

# Test JQL to Q conversion
jql = '$field1 = "value1" and $field2 >= 100'
q = jql_to_q(jql)
print(q,"q")