import json

json_data = {
    "name": "bgakingo",
    "lockfileVersion": 2,
    "requires": 'true',
    "packages": {
        "": {
            "dependencies": {
                "bootstrap": "^5.1.0"
            },
        },
    },

}

data = []
with open('package-lock.json', 'r') as json_file:
    for d in json_file:
        data.append(d)

print(data)
