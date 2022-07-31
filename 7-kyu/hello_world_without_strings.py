# https://www.codewars.com/kata/584c7b1e2cb5e1a727000047
# 
# You need to create a function, helloWorld, that will return the String Hello, World! without actually using raw strings. This includes quotes, double quotes and template strings. You can, however, use the String constructor and any related functions.
# You cannot use the following:
# "Hello, World!"
# 'Hello, World!'
# `Hello, World!`

# my solution using module __hello__
import sys, io
def hello_world():
    sys.stdout = mystdout = io.StringIO()
    import __hello__
    return mystdout.getvalue().strip().capitalize()
  
# yet another clever:
import inspect
def hello_world():
    # Hello, World!
    return inspect.getsource(hello_world)[25:38]


# coding: unicode_escape
def hello_world():
    return \x27Hello, World!\x27

  
import sys,string
def hello_world():
    name = sys._getframe().f_code.co_name
    return string.capwords(name[:5]) + chr(44) + chr(32) + string.capwords(name[6:]) + chr(33)
