import re
from django.db.models import Q
from collections import defaultdict


def tokenizedExpression_2_QExpression(expression):
    jql2qFields = {
            'project': 'project__name',
        }
    # jql2qFields = defaultdict('jiracustomfieldvalue',jql2qFields)
    if expression:
        field = jql2qFields[expression[0] ]if expression[0] in jql2qFields else 'jiracustomfieldvalue__field__name'
        operator = expression[1]
        value = expression[2:]
        print(f'Field: {field}')
        print(f'Operator: {operator}')
        print(value)

    return Q()

# function to build a Q object from the tokens
def build_q(tokens):
    # create an empty stack to keep track of parentheses
    stack = []

    # build a Q object from the tokens
    q = Q()
    expression = []
    inFlag  = False
    # iterate over the tokens and build the Q object
    for token in tokens:
        if token.lower() == 'and':
            q &= tokenizedExpression_2_QExpression(expression)
            expression = []
        elif token.lower() == 'or':
            q |= tokenizedExpression_2_QExpression(expression)
            expression = []

        elif token.lower() == 'not':
            q = ~q
        elif token == '(':
            if not inFlag:
                # push the current Q object onto the stack
                stack.append(q)
                # reset the Q object
                q = tokenizedExpression_2_QExpression(expression)
                expression = []

        elif token == ')':
            if inFlag:
                inFlag = False
            else:
                # pop the Q object from the stack
                prev_q = stack.pop()
                # combine the previous Q object with the current one
                q = prev_q & q
        else:
           expression.append(token)
           if token == 'in':
                inFlag = True

    return q

# tokenize the JQL query
tokens = ['(', 'project', '=', 'FOO', 'or', 'project', '=', 'BAR', ')', 'and', '"Work Type"', 'in', '(', 'High', ',', 'Medium', ')', 'and', 'resolution', '=', 'Fixed']

# parse the tokens into a Q object
q = build_q(tokens)

# print the Q object
print(q)