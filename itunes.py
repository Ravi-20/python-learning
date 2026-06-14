# This program takes a search term as a command-line argument and then queries the iTunes Search API for songs matching that term. It retrieves the results in JSON format, parses it, and prints the track names of the songs found.
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
