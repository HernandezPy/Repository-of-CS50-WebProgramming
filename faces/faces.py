print('Hello 🙂')
print('Goodbye :(')
print('Hello 🙂 Goodbye 🙁')

def convert(input_str):
    emoji_str = input_str.replace(':)', '🙂').replace(':(', '🙁')
    return emoji_str


def main():
    user_emoji = input('Please enter your text: ')
    converted_text = convert(user_emoji)
    print(converted_text)

if __name__ == '__main__':

   main()
