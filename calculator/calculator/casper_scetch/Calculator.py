# package calculator


# from calculator.calculator.tobias_scetch.calculator import postfix
from math import nan
from enum import Enum
from multiprocessing.sharedctypes import Value
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

    
    

MISSING_OPERAND:  str = "Missing or bad operand"
DIV_BY_ZERO:      str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND:     str = "Operator not found"
OPERATORS:        str = "+-*/^"
NO_EXPRESSION: str = "HELLO!? WHERE IS EXPRESSION"

    


def infix_to_postfix(tokens: list):
    """Sets infix to postfix
    """
    op_stack = Stack()
    #inpus is an array ive looked lol
    #may need to ouput stack. like num>num>op>op 
    output = []
    #runs for all tokens
    for token in tokens:
        token_method(token,op_stack,output)        


 #TODO ----Escape this------
    #pops the last of the operator to the outpout
    append_remaining_items(op_stack,output)
            
    return output


# -----  Evaluate RPN expression -------------------
def append_remaining_items(op_stack: Stack, expression_list: list[str]):
    """Appends the last remaining items in the stack to the expression list
    """
    while not  op_stack.is_empty():
        #checs so thats there arent any parentheses left
        if op_stack.head.value in "()":
            raise ValueError(MISSING_OPERATOR +  ". Too many parentheses")
        else:
            expression_list.append(op_stack.pop())
    
            
def eval_postfix(postfix_tokens: list[str]) -> int:
    """Evaluates the postfix expression
    """
    #TODo ----------fix-----------
    stack = Stack()
    for token in postfix_tokens:
        do_operation_list = []
        make_operations(stack, token, do_operation_list)
    return stack.head.value

# Method used in REPL
def eval_expr(expr: str):
    """Evaluates the entire expression in input
    """
    if len(expr) == 0:
        raise ValueError(NO_EXPRESSION)
    tokens = tokenize(expr)
    postfix_tokens = infix_to_postfix(tokens)
    
    return eval_postfix(postfix_tokens)


def apply_operator(op: str, d1: float, d2: float) -> float:
    """Applies operator to given operands
    """
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


def get_precedence(op: str) -> int:
    """Returns the precedence of a given operation"""
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4,
        "(":0,
        ")":0,

    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


def get_associativity(op: str) -> Assoc:
    """Returns the associativity of the given operator"""
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


# ---------- Tokenize -----------------------
def tokenize(expr: str): #BEGINNING OF TOKENIZE, NEED TO IMPLEMENT SO THAT IT ONLY PRINTS OPERANDS (numbers), OPERATORS AND PARENTHESES
    list_of_tokens = []
    current_number = ''

    for i, token in enumerate(expr, start = 0):
        if token.isdigit() or token == ".":
            current_number += token
            #mod length to not get overflow in index
            next_token = expr[(i+1) % len(expr)]
            
            if not (next_token.isdigit() or next_token == ".") or i == len(expr)-1:
                list_of_tokens.append(current_number)
                current_number = ''
    
        elif token in OPERATORS or token in "()":
            list_of_tokens.append(current_number)
            list_of_tokens.append(token)
            current_number = ''

            

    return list_of_tokens

# TODO Possibly more methods
def make_operations(stack: Stack, token: str, operations: list[str]):
    """Makes all operations according to the stack order
    """
    if is_number(token):
        stack.push(token)
    elif token in OPERATORS:
        
        try:
            #This one throws error when missiong operand because stack cant pop in function
            fill_op_list(stack, operations)
            #this one throws error when mussing operand by design
            result = apply_operator(token, operations[0], operations[1])

            #These might also throw index error since youre looking fro specific indexes 
        except ValueError:
            raise ValueError(MISSING_OPERAND)
        except IndexError:
            raise ValueError(MISSING_OPERAND)
        except ZeroDivisionError:
            raise ValueError(DIV_BY_ZERO)
        
        
        stack.push(result)
    
def fill_op_list(stack: Stack, list_to_be_filled: list):
    """Fills the list with operators and operands to be executed
    """
    for i in range(2):

        popped_token = stack.pop()
        list_to_be_filled.append(float(popped_token))

def token_method(token:str, op_stack:Stack, list:list) -> list:
    """Adds tokens in different orders depending on their types
    """
    if is_number(token):
        list.append(token)
    #checks if token is operator
    elif token in OPERATORS and not token == "":
       
        add_operator_to_stack(op_stack, token, list)          
    #if the token is an open parentheses we push it onto the stack
    elif token == "(":
        op_stack.push(token)
    #if it is a closed parentheses we check if the stack isnt empty and then we pop all the operator until we find an open parentheses
    elif token == ")":
        add_items_in_parentheses(op_stack, list)

def add_items_in_parentheses(op_stack:Stack, list:list):
    """Adds items thats are inside of a given parentheses. Works after a close paren until an open paren
    """
    if not op_stack.is_empty():
        while not op_stack.is_empty() and not op_stack.head.value == "(":
            list.append(op_stack.pop())
        # pops the left parenthises from the stack if its there or raises an erro if it isnt
        check_for_and_discard_left_parentheses(op_stack)
    else:
        #if the operator stack is empty when you open up a paren youre doing something wrong
        raise ValueError(MISSING_OPERATOR + " in parentheses")

def check_for_and_discard_left_parentheses(op_stack: Stack):
    """Discards opening parentheses from the stack if found
    """
    try:
        if op_stack.head.value == "(":
            op_stack.pop()
    except AttributeError:
        #WHy would you close a parentheses when you havent opened one???
        raise ValueError(MISSING_OPERATOR + ". No open paren??? why???")


def has_greater_precedence(op1:str, op2:str) -> bool:
    """Check which operator has greater precedence
    """
    if get_precedence(op1) > get_precedence(op2):
        return op1
    elif get_precedence(op1) == get_precedence(op2):
        return None
    else:
        return op2

def add_operator_to_stack(op_stack:Stack, token:str, list:list) -> list:
    """Adds operator to the stack of operations
    """
    if not op_stack.is_empty():
        while not op_stack.is_empty() and (has_greater_precedence(op_stack.head.value, token) == op_stack.head.value or (has_greater_precedence == None and  get_associativity(token) == 1)):
                    list.append(op_stack.pop()) 
                #then we push the token onto the stack
    op_stack.push(token)
    
def is_number(string: str) -> bool:
    """Check if string is a number both float and int
    """
    output = None
    for letter in string:
        if letter == "." or letter.isdigit():
            output = True
        else:
            output = False
    return output

# print(infix_to_postfix(["3", "+", "3"]))
