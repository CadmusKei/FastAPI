
# first on wrappers and passing functions as variables

def greet(name):
    return f"hello {name}"

def shouty_greet(name):          # the wrapper
    result = greet(name)         # call the original
    return result.upper()        # do something extra with the result

#print(shouty_greet("kei"))       

# But what if we wanted to dynamicallyt add wrappers?
# Since making 50 wrappers for 50 functions is tedious

# My wrapper function
def shout(func):
    def wrapper(text: str):
        result = func(text).upper()
        return result
    return wrapper

@shout
def new_greet(name):
    return ("Hello " + name)

@shout
def different_greet(name):
    return ("Wassup " + name)

print(new_greet("john"))
print(different_greet("Alex"))
