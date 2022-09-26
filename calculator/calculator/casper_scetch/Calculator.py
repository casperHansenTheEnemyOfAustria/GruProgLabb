# package calculator


from math import nan
from enum import Enum
from re import A

from Stack import *

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

OPERATOR_ORDER: dict = {
    "^":1,
    "*":2,
    "/":2,
    "+":3,
    "-":3,
    "(":4,
    ")":4
}
    
    

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"

#TODO -------------- MAKE T>HIS WORK OPERATORS ARE IN WRONG ORDERI THINK 
def infix_to_postfix(tokens: list):
    op_stack = Stack()
    #inpus is an array ive looked lol
    #may need to ouput stack. like num>num>op>op 
    output = []
    #runs for all tokens
    for token in tokens:
        #checks if tokesn is digit
        if token.isdigit():
            print(token)
            output.append(token)
        #checks if token is operator
        elif token in OPERATORS:
            #if the operator stack is not mpty and the current token has a lower precedence than the nearest operator in the stack we pop the nearest operator into the output
            while not op_stack.is_empty() and OPERATOR_ORDER[op_stack.head.value] <= OPERATOR_ORDER[token] :
                output.append(op_stack.pop())
            #then we push the token onto the stack
            
            op_stack.push(token)
            print(f"pushed token {token}")
            
        #if the token is an open parentheses we push it onto the stack
        elif token == "(":
            op_stack.push(token)
        #if it is a closed parentheses we check if the stack isnt empty and then we pop all the operator until we find an open parentheses
        elif token == ")":
            if not op_stack.is_empty():
                print(f"found close paren and digs are {op_stack}")
                while not op_stack.head.value == "(":
                    print(op_stack.head.value)
                    output.append(op_stack.pop())
                # pops the left parenthises from the stack if its there or raises an erro if it isnt
                if op_stack.head.value == "(":
                    #when done the parentheses is discarded
                    op_stack.pop()
                else:
                    raise MISSING_OPERATOR
            else:
                #error if the stack has no operators
                raise MISSING_OPERATOR
              
    #pops the last of the operator to the outpout
    while not  op_stack.is_empty():
        #checs so thats there arent any parentheses left
        if op_stack.head.value in ["()"]:
            raise MISSING_OPERATOR
        else:
    
            output.append(op_stack.pop())
            
            
    return output


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    
    
    
    return 0  # TODO


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    tokens = expr.split()
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
def tokenize(expr: str):
    return None   # TODO

# TODO Possibly more methods

print(infix_to_postfix(["(","1", "+", "2",")","*","3"]))
