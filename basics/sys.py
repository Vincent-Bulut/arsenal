""" sys library
1. sys.argv
2. sys.exit()
3. sys.stdin, sys.stdout, sys.stderr
4. sys.path
"""

import sys

if __name__ == '__main__':
    # 1. sys.argv
    # liste qui contient les arguments passés au script python depuis la ligne de cmd
    # le premier arg est le nom du script
    print("Arguments:", sys.argv)

    # 2. sys.exit
    # couramment utilisé pr quitter un pg en cas d'erreur ou lorsqu'une c° est remplie
    # sys.exit("Error: smth went wrong.")

    # 3. sys.stdin, sys.stdout, sys.stderr
    sys.stdout.write("this is standard output\n")
    sys.stderr.write("This is an error message\n")

    # 4. sys.path
    # liste qui spécifie les répertoires où python va chercher les modules à importer.
    # pratique pour ajouter des répertoires personnalisés."""
    # sys.path.append('/my/custom/path')

    # 5. sys.executable
    # cet attribut est utile pour savoir quel interpréteur python est utilisé dans le script

    # 6. sys.platform
    """ retourne une chaine qui donne le nom du système d'exploitation sur lequel python
    est en cours d'exécution."""

    # 7. sys.version
    # infos détaillées sur la version de python en cours d'exécution
    print(sys.version)

