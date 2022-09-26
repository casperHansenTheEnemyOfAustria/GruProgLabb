# package calculator

from math import nan
from enum import Enum
from collections import deque

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"


def infix_to_postfix(tokens: list):
    stack = deque()
    postfix_list = []
    for token in tokens:
        if token.isdigit():
            postfix_list.append(token)
        elif token == "+" or token == "-" or token == "*" or token == "/" or token == "^":
            if len(stack) == 0:
                stack.append(token)
            else:
                top_of_stack = stack[-1]
                if get_precedence(token) > get_precedence(top_of_stack):
                    stack.append(token)
                elif get_precedence(token) == get_precedence(top_of_stack):
                    if get_associativity(token) == 1:
                        popped_token = stack.pop()
                        postfix_list.append(popped_token)
                        stack.append(token)
                    else:
                        stack.append(token)
                else:
                    popped_token = stack.pop()
                    postfix_list.append(popped_token)
                    stack.append(token)
        else:
            if token == "(":
                stack.append(token)
            else:
                for operator in reversed(stack):
                    if operator != ")":
                        popped_token = stack.pop()
                        postfix_list.append(popped_token)
                    else:
                        popped_token = stack.pop()
                        postfix_list.append(popped_token)
                        break
    postfix_result = postfix_list + list(stack)
    return postfix_result


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    stack = deque()
    do_operation_list = []
    for token in postfix_tokens:
        if token.isdigit():
            stack.append(token)
        elif token == "+" or token == "-" or token == "*" or token == "/" or token == "^":
            for i in range(2):
                popped_token = stack.pop()
                do_operation_list.append(int(popped_token))
            result = apply_operator(token, do_operation_list[0], do_operation_list[1])
            stack.append(result)
    return int(stack[0])


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    tokens = tokenize(expr) # tokenize(expr) instead ?
    postfix_tokens = infix_to_postfix(tokens)
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str): #BEGINNING OF TOKENIZE, NEED TO IMPLEMENT SO THAT IT ONLY PRINTS OPERANDS (numbers), OPERATORS AND PARENTHESES
    list_of_tokens = []
    number = ''
    i = 0
    for token in expr:
        if token.isdigit():
            number += token
            if not expr[(i+1) % len(expr)].isdigit()or i == len(expr)-1:
                list_of_tokens.append(number)
                number = ''
            i += 1
        elif token == "+" or token == "-" or token == "*" or token == "/"\
                or token == "^" or token == "(" or token == ")":
            list_of_tokens.append(number)
            list_of_tokens.append(token)
            number = ''
            i += 1

    return list_of_tokens
# TODO Possibly more methods




#------- TEST ----------


def test():
    print()