import emoji

def emojize_text(text):
    return emoji.emojize(text, language='alias')


def main():
    user_input = input('Input: ')
    emojized_text = emojize_text(user_input)
    print(f'Output: {emojized_text}')


if __name__ == '__main__':
    main()
