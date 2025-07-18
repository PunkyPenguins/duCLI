#!/usr/bin/env python

# https://docs.python.org/3.6/library/argparse.html#required
import argparse
import json
parser = argparse.ArgumentParser(description='Give me a white russian')
parser.add_argument('--list-path', metavar='Games List Path', type=str, help='Path containing the List of Games', dest="listPath", required=True)
args = parser.parse_args()
# open resout les chemins relatifs en fonction du PWD
targetGamesFileDescriptor= open(args.listPath, 'r')
content = targetGamesFileDescriptor.read()
print (content)
targetGamesFileDescriptor.close()
loadedcontent = json.loads(content)
#print (loadedcontent["games"][1]["title"])
def list_games(games):
    for item in games:
        result = f"I own {item['title']} released in {item['release_year']} for {", ".join(item['platforms'])}"
        print (result)
  
list_games(loadedcontent["games"])
# path-exist = cat {args.listPath}
# if
#   path-exist = True
#   print (f"The file is located in {args.listPath}")
# else
#   path-exist = error
#   exit 1
# pas de "with"

# Cat le path, si pas error alors print si error exit 1

# Ouvrir le fichier pour obtenir une str contenant le contenu du fichier
# Parser le fichier de json vers un dict python
# Parcourir le dict python et afficher les valeurs 