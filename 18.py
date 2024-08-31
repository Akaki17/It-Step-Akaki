#1

def positive_number_check(func):
    def wrapper(number):
        if number < 0:
            raise ValueError("The number must be positive.")
        else:
            result = func(number)
            print(f"Result: {result}")
            return result
    return wrapper

@positive_number_check
def return_number(number):
    return number

# Example usage:
return_number(5)   # This will print "Result: 5"
# return_number(-3)  # This will raise a ValueError with the message "The number must be positive."


#2

class PositiveNumberFunctor:
    def __call__(self, number):
        if number < 0:
            raise ValueError("The number must be positive.")
        else:
            print(f"Result: {number}")
            return number

# Example usage:
positive_functor = PositiveNumberFunctor()
positive_functor(10)  # This will print "Result: 10"
# positive_functor(-5)  # This will raise a ValueError with the message "The number must be positive."



#3
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time:.4f} seconds")
        return result
    return wrapper

@time_it
def example_function(seconds):
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

# Example usage:
example_function(2)  # This will print the time taken to sleep for 2 seconds.



#4

class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, attrs)

class ExampleClass(metaclass=LoggingMeta):
    pass

# Example usage:
example = ExampleClass()  # This will print "Creating class: ExampleClass"



