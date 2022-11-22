from json import load

def get(filename: str):
    try:
        with open(filename, "r", encoding="utf8") as f:
            return str(load(f))
    except:
        return None