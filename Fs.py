from e85 import e85

def FileSave(TargetName = None, Content = None, Encryption = None):
    """Encrypt on currenly avalible:
    None"""

    if Encryption == "85": _Content = e85(Content)
    else: _Content = Content

    if TargetName == "__DATA__": TargetName = "Dt85.py"


    with open(TargetName, "w") as Fs_o:
        Fs_o.write(_Content)
        Fs_o.close()
