import requests
import json

resp = requests.get("https://localhost:5000/mission/1")
print(f'Status code = {resp.status_code}')
d = json.loads(resp.content)
print(d)
print(f'id = {d["id"]}')

# now let's create a class
class Mission:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result

    resp = requests.post("https://localhost:5000/mission",
                         data='{"id": 4, "title": "name2"}',
                         headers={"Content-type": "application/json"});
    print(f'Status code = {resp.status_code}');

    # how to check if a GET response returned empty??
    if resp.content.decode('utf8').replace("'", '"') == '':
        print('empty result')
    else:
        print('not empty result')

t = Mission(d)
print(t.userId)
print(t.id)
print(t.title)