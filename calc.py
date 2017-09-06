#!/bin/env python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('cal.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error('Tried to divide by zero')
    else:
        return result
def mod(x,y):

    return x % y

num1=10
num2=0


add_result = add(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = sub(num1, num2)
logger.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))

mul_result = mul(num1, num2)
logger.debug('Mul: {} X {} = {}'.format(num1, num2, mul_result))

divide_result = divide(num1, num2)
logger.debug('divide: {} / {} = {}'.format(num1, num2, divide_result))

mod_result = mod(num1, num2)
logger.debug('Mod: {} % {} = {}'.format(num1, num2, mod_result))
