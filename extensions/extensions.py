def get_media_type(filename):
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'

    }

    filename = filename.lower()

    for ext in media_types:
        if filename.endswith(ext):
            return media_types[ext]

    return 'application/octet-stream'


def main():
    filename = input('File name: ').strip()
    media_type = get_media_type(filename)
    print(media_type)


if __name__ == '__main__':
    main()

