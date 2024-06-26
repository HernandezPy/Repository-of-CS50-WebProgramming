import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = ('https://itunes.apples.com/search?entity=song&limiit=1&term=' + sys.argv[1])
print(response.json())
