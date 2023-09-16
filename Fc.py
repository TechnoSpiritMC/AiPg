from d85 import d85

def FileCreate(OriginName = None, Targetname = None, Content = None, Decryption = None):
    """Decryption currenly avalible:
    Ascii84"""

    if OriginName == "__DATA__":
        Targetname == "Dt85.temp.py"
        Decryption == "85"

    if Decryption == "85":
        
        with open(OriginName, "r") as OriginOpen:
            OriginContent = OriginOpen.readlines()
            OriginOpen.close()

        _Content = d85(OriginContent)



    else: _Content == Content


    with open(Targetname, "w") as Fs_o:
        Fs_o.write(_Content)
        Fs_o.close()
