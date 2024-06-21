def extensions():
    insensitively = extensions.lower().strip()
    valid_extensions = {
        ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']
    }
    if valid_extensions in insensitively:
        print(f'image/{valid_extensions})
              else:
              print('application/octet-stream')


def valid_extensions():
    answer_input = input('File name: ')
    result = extensions(answer_input)

if __name__ == '__main__':
 main()
