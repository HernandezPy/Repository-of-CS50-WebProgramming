import emoji

def emojize_text(text):
    return emoji.emojize(text, language='alias')


def min():
    user_input = input('Input: ')
    emojized_text = emojize_text(user_input)
    print('Output: ', emojize_text)


if __name__ == '__main__':
    main()
