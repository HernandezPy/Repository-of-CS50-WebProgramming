def announce(f):
    def wrapper():
        print("About to run the funtion...")
        f()
        print("Done with the funtion.")
    return wrapper

@announce
def hello():
    print("Hello, word")

hello()
