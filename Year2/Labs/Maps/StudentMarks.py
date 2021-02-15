import sys

def make_map():
    Dict = {}
    for lines in sys.stdin.read().split("\n"):
        if len(lines) > 0:
            lines = lines.strip().split()
            Dict[lines[0]] = lines[-1]
    return Dict