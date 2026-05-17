import json
user_profile = {
    "user_id": 123,
    "username": "coder2025",
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(user_profile, f, indent=4, ensure_ascii=False)

# txt = {1:"Я лучший, среди худших"}
# with open("profile.json", "w", encoding="utf-8") as file:
#     json.dump(txt, file)