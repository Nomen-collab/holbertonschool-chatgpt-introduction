#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    print("Arguments fournis :")
    for i, arg in enumerate(sys.argv[1:], start=1):  # Exclut le nom du script
        print(f"{i}: {arg}")
else:
    print("Aucun argument fourni.")
