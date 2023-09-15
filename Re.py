def r(text):
    r = 255
    g = b = 50
    return f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m"