from Co import c
from Ha import Hash
from Fs import FileSave

import difflib

print(c(0, 255, 150, "Bienvenue sur AiPg!"))
print(c(0, 255, 150, "Avez vous un compte? (o/n)"))

tmp_001 = input("> ")

if "o":
    print(c(0, 255, 150, "Entrez un nom d'utilisateur:"))
    tmp_002 = input("> ")

    while True:

        print(c(0, 255, 150, "Entrez votre mot de passe:"))  
        tmp_003 = input("> ")
        if tmp_003 == "s":
            exit()

        print(c(0, 255, 150, "Confirmez votre mot de passe:"))
        tmp_004 = input("> ")

        if tmp_003 == tmp_004:
            print(c(0, 255, 150, "Votre mot de passe a été enregistré!"))
            break

        else:
            print(c(150, 255, 0, "Oups! On dirait que vous avez mal entré votre mot de passe... Réessayez à nouveau\nPour sortir, faites 's'"))

    tmp_005 = Hash(tmp_003)

    FileSave("__DATA__", \
f"""
#The content of this file may change frequely. If any changes are applied manually, the program may no longer work properly.
Name = {tmp_002}
Password = {Hash(tmp_003)}
""", "85")

    
    
