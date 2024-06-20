def greeting_response(hello):
    greeting = hello.strip().lower()
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


def main():
    user_input = input('Greeting: ')
    result = greeting_response(user_input)
    print(f'{result}')

if __name__ == '__main__':
    main()



