def extensions():
    insensitively = extensions.lower().strip()
    valid_extensions = {
        ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']
    }
    if valid_extensions in insensitively:
         return valid_extensions
    else:
         print('application/octet-stream')


def main():
    answer_input = input('File name: ')
    result = valid_extensions(answer_input)
    printcla(f'image/{valid_extensions}')

if __name__ == '__main__':
 main()
