import sys
import re


def parse(html):
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)[^"]*"', html)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None


def main():
    if len(sys.argv) == 2:
        html = sys.argv[1]
    else:
        html = input("HTML: ")

    result = parse(html)
    if result:
        print(result)
    else:
        print("No YouTube video found.")


if __name__ == "__main__":
    main()
