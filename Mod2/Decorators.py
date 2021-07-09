import datetime

def log_function_call(func):
    def with_logging(*args, **kwargs):
        func(*args, **kwargs)
        print(func.__name__ + " was called at " + datetime.datetime.now().strftime("%d/%m/%Y,%H:%M:%S"))
    return with_logging

@log_function_call
def say_hello():
    print("HELLO")
    
say_hello()    