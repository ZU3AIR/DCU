def get_plural(w):
    es = ("ch", "sh", "x", "s", "z", "o")
    v = "aeiou"
    if w.endswith(es):
        return w + "es"
    if w.endswith("f"):
        return w[:-1] + "ves"
    if w.endswith("fe"):
        return w[:-2] + "ves"
    if w[-1] == "y" and w[-2] not in v:
        return w[:-1] + "ies"
    if w.endswith("o"):
        return w + "es"
    return w + "s"

print(get_plural("boy"))