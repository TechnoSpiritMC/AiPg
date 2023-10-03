from d85 import d85
from Co import c

def FileCreate(_OriginName = None, Targetname = None, Content = None, Decryption = None):
    """Decryption currenly avalible:
    Ascii84"""

    _Content = ""

    if _OriginName == "__DATA__":
        Targetname = "Dt85.temp.py"
        OriginName = "Dt85"

    if _OriginName == "__DATA__":
        
        with open("Dt85", "r") as OriginOpen:
            OriginContent = OriginOpen.readlines()
            OriginOpen.close()




    else: _Content == OriginContent


    with open(Targetname, "w") as Fs_o:
        Fs_o.write(_Content)
        Fs_o.close()
