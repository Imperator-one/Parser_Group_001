import json
def exit(txt):
    with open("text.txt",'w',encoding="utf-8") as file:
        json.dump(txt,file)