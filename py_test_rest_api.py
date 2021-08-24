
import requests
import json
import pytest

class RestObject:
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

def test_rest_api_get_mission():

    resp = requests.get("https://localhost:5000/mission/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.userId == 1
    assert t.title == 'name 1'
    assert t.completed == False


