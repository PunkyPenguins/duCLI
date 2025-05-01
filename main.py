#!/usr/bin/env python

# https://docs.python.org/3.6/library/argparse.html#required
import argparse
parser = argparse.ArgumentParser(description='Give me a white russian')
parser.add_argument('--list-path', metavar='Games List Path', type=str, help='Path containing the List of Games', dest="listPath", required=True)
args = parser.parse_args()
# open resout les chemins relatifs en fonction du PWD
targetGamesFileDescriptor= open(args.listPath, 'r')
content = targetGamesFileDescriptor.read()
print (content)
targetGamesFileDescriptor.close()
print (content)
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