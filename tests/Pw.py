def c(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"

def r(text):
    r = 255
    g = b = 50
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"


def g(text):
    g = 255
    r = b = 50
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"


def b(text):
    b = 255
    r = g = 100
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"
import hashlib, difflib


str = ""



result = hashlib.sha512(str.encode()) 

print(result.hexdigest())

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
            break()

        else:
            print(c(150, 255, 0, "Oups! On dirait que vous avez mal réentré votre mot de passe... Réessayez à nouveau\nPour sortir, faites s"))
