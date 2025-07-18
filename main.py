#!/usr/bin/env python

# https://docs.python.org/3.6/library/argparse.html#required
import argparse
import json
parser = argparse.ArgumentParser(description='Give me a white russian')
parser.add_argument('--list-path', metavar='Games List Path', type=str, help='Path containing the List of Games', dest="listPath", required=True)
args = parser.parse_args()

def list_games(games):
    for item in games:
        result = f"I own {item['title']} released in {item['release_year']} for {", ".join(item['platforms'])}"
        print (result)

def extract_games(pathlist):
    targetGamesFileDescriptor= open(pathlist, 'r')
    content = targetGamesFileDescriptor.read()
    targetGamesFileDescriptor.close()
    loadedcontent = json.loads(content)
    return loadedcontent["games"]

games = extract_games(args.listPath)
list_games(games)
# path-exist = cat {args.listPath}
# if
#   path-exist = True
#   print (f"The file is located in {args.listPath}")
# else
#   path-exist = error
#   exit 1
# pas de "with"

# Cat le path, si pas error alors print si error exit 1
