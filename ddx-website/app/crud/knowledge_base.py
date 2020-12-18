import json


# returns json object based on given json file
def get():
    with open("app/engine/resources/kb_inverted_index.json", "r") as json_file:
        return json.load(json_file)


