# dumps()- pyton->json str
# loads() -json-> pyton object str
# dump()save Pyton object- > file.json (file)
# load() file.json ->> Pyton (file)
import json

user = {"username":"sofia","age": 21,"is_admin":True}
json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "kristina",
    "password": "Aa123456!",
    "timeout": 20
}
with open("config.json", "w", encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)

with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print(config["url"])

def save_profile(name,age,city):
    profile = {
        "name":name,
        "age": age,
        "city":city
    }
    with open("profile.json","w",encoding="utf-8") as file:
        json.dump(profile,file,indent=2)
save_profile("Sofi","21","Bat yam")

