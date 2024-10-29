import re


def parse(html):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(?P<video_id>[a-zA-Z0-9_-]+)[^"]*"', html)
    if match:
        video_id = match.group("video_id")
        return f"https://youtu.be/{video_id}"


def main():
    html = input("HTML: ")

    result = parse(html)
    if result:
        print(result)
    else:
        return None


if __name__ == "__main__":
    main()
