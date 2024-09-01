
def main():
    numbers = [1, 2, 3, 4, 5]
    squares = [n ** 2 for n in numbers]
    print(squares)

    words = ["ball", "fuck", "nigga"]
    word_lengths = {word: len(word) for word in words}
    print(word_lengths)

    unique_squares = {n ** 2 for n in [1, 2, 2, 3, 4, 5]}
    print(unique_squares)

    add = lambda x, y: x + y
    print(add(2, 4))

    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!!")

    say_hello()

    def shout(text):
        return text.upper()
    
    def whisper(text):
        return text.lower()
    
    print(shout('Hello'))

    def greet(func):
        greeting = func("""Hi, I am created by a function passed as an argument. """)
        print(greeting)

    greet(shout)
    greet(whisper)

    def create_adder(x):
        def adder(y):
            return x + y
        return adder
    
    add_15 = create_adder(15)
    print(add_15(10))


    def hello_decorator(func):
        def inner1():
            print("Hello, this is before function executed")
            func()
            print("This is after functin executed")
        return inner1
    
    @hello_decorator
    def function_to_be_used():
        print("This is inside the fucntion!!")

    function_to_be_used()
    
if __name__ == "__main__":
    main()


