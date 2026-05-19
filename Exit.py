import json
def exit(txt):
    with open("per.json", "w", encoding="utf-8") as file:
        json.dump(txt, file)
