import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    #no parenthesis
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello! ")

@delay_decorator
def say_goodbye():
    print("Goodbye! ")

#@delay_decorator
def say_greeting():
    print("How are you? ")

#say hello and say goodbye will both delay by two seconds
# due to the delay decorator
say_hello()
say_goodbye()

#say greeting will not wait two seconds before executing
say_greeting()

#say greeting will execute a second time,
# the second time it will wait two seconds
decorated_function = delay_decorator(say_greeting)
decorated_function()
