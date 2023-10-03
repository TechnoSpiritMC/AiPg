def b(text):
    b = 255
    r = g = 100
    return f"\033[38;2;{r};{g};{b}m{text}\033[38;2;255;255;255m"