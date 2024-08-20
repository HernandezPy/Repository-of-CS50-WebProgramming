def main():
    user_input = input('input: ').strip()
    print(shorten(user_input))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([char for char in word if char.lower() not in vowels])
    return result

if __name__ == '__main__':
    main()
