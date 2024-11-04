import re

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.node_type == 'operator':
            return f'({self.left} {self.value} {self.right})'
        else:
            return f'{self.value}'

def create_rule(rule_string):
    rule_string = rule_string.replace('(', '( ').replace(')', ' )')
    tokens = rule_string.split()

    def parse_expression(tokens):
        if tokens[0] == '(':
            tokens.pop(0)
            left = parse_expression(tokens)
            operator = tokens.pop(0)
            right = parse_expression(tokens)
            tokens.pop(0)
            return Node('operator', value=operator, left=left, right=right)
        else:
            return parse_condition(tokens.pop(0))

    ast = parse_expression(tokens)
    return ast

def parse_condition(condition):
    tokens = re.split(r'([<>=]+)', condition)
    return Node('operand', value=(tokens[0].strip(), tokens[1].strip(), tokens[2].strip()))

def evaluate_condition(condition, data):
    field, operator, value = condition
    value = int(value) if value.isdigit() else value
    if operator == '>':
        return data[field] > value
    elif operator == '<':
        return data[field] < value
    elif operator == '=':
        return data[field] == value
    return False

def evaluate_ast(node, data):
    if node.node_type == 'operand':
        return evaluate_condition(node.value, data)
    elif node.node_type == 'operator':
        left_result = evaluate_ast(node.left, data)
        right_result = evaluate_ast(node.right, data)
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result
    return False

def evaluate_rule(rule_string, data):
    ast = create_rule(rule_string)
    return evaluate_ast(ast, data)
