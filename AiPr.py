from Co import c
from Ha import Hash
from Fs import FileSave
from Re import r
from Fc import FileCreate


try:
    from Dt85 import Name, Password
except Exception as e:

    print(c(0, 255, 150, "Bienvenue sur AiPg! \nAvant de découvrit la plateforme, inscrivez vous!"))

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

    FileSave("__DATA__", \
f"""
#The content of this file may change frequely. If any changes are applied manually, the program may no longer work properly.
Name = "{tmp_002}"
Password = "{Hash(tmp_003)}"
""")
    
if True is True:
    try:
        from Dt85 import Name, Password
    except Exception as e:
        print(c(255, 0, 0, f"[ERREUR ADANFE] Vous ne possédez pas de comptes sur cette session.\nUne description plus détaillée de l'erreur suit:\n{c(255, 255, 100, f'{e}')}"))
        exit("ERREUR ADANFE")

    from Dt85 import Name, Password

    print(c(0, 255, 150, "\n\nBienvenue sur AiPg!\n"))

    print(c(0, 255, 150, "Entrez votre nom d'utilisateur:"))
    tmp_006 = input("> ")
    if Name == tmp_006:
        i = 1

        while True:
            print(c(0, 255, 150, "Entrez votre mot de passe:"))
            print(c(200, 100, 255, f"[DEBUG] {str(i)}"))

            tmp_007 = input("> ")

            if str(Hash(tmp_007)) == Password:
                """Suite"""
                break

                
            else:
                i = i + 1

            if i > 3:
                print(r("[ERREUR IPETMT] Vous avez entré un mauvais mot de passe à trop nombreuses reprises!"))
                print(c(0, 255, 150, "Si vous avez oublié votre mot de passe: faites ") + c(255, 255, 0, "o") + c(0, 255, 150, ", sinon, faites [ENTRÉE]"))
                tmp_008 = input("> ")

                if tmp_008 == "o":

                    while True:

                        print(c(0, 255, 150, "Entrez votre mot de passe:"))  
                        tmp_003 = input("> ")

                        if tmp_003 == "s":
                            exit()

                        print(c(0, 255, 150, "Confirmez votre mot de passe:"))
                        tmp_004 = input("> ")

                        if tmp_003 == tmp_004:
                            print(c(0, 255, 150, "Votre mot de passe a été enregistré!"))
                            i = 1
                            break

                        else:
                            print(c(150, 255, 0, "Oups! On dirait que vous avez mal entré votre mot de passe... Réessayez à nouveau\nPour sortir, faites 's'"))

                    tmp_005 = Hash(tmp_003)

                    FileSave("__DATA__", \
                             
        
f"""
#The content of this file may change frequely. If any changes are applied manually, the program may no longer work properly.
Name = "{tmp_006}"
Password = "{Hash(tmp_003)}"
""")
    else:
        print(r("Oups! Ce compte n'existe pas sur cette session...\nSi vous pensez que c'est une erreur de votre part, redémarrez le programme, sinon, faites o"))

        tmp_009 = input("> ")

        if tmp_009 == "o":

            

            print(c(0, 255, 150, "Entrez un mon d'utilisateur:"))
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
Name = "{tmp_002}"
Password = "{Hash(tmp_003)}"
""")        
         
