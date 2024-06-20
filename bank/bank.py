def greeting_response(hello):
    greeting = hello.strip().lower()
    if greeting_response == 'hello':
        return 0
    elif greeting_response == 'h':
        return 20
    else:
        return 100


def main():
    while True:
        user_greeting = input("Greeting (or type 'exit' to quit): ")
        if user_greeting == 'exit':
            print('Exiting the program')
            break
        result = greeting_response(user_greeting)
        print(f'{result}')


if __name__ == '__main__':
    main()



