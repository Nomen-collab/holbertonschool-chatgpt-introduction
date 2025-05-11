#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Ajout de cette ligne pour décrémenter n
    return result

if len(sys.argv) < 2:
    print("Usage: python3 factorial.py <entier>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Erreur : La factorielle n'est pas définie pour les nombres négatifs.")
        sys.exit(1)
    elif num == 0:
        print(1)
    else:
        f = factorial(num)
        print(f)
except ValueError:
    print("Erreur : L'argument doit être un entier valide.")
    sys.exit(1)
