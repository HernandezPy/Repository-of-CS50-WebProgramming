def remove_vowels(input_str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''.join([char for char in input_str if char.lower() not in vowels])
    return result

if __name__ == '__main__':
    user_input = input('input: ').strip()
    print(remove_vowels(user_input))
