import sys
import json
import os

json_string = sys.argv[1]
json_data = json.loads(json_string)
versionToCheck = sys.argv[2]
def get_version(version):
    for i in json_data["viewer"]["packages"]["nodes"][0]["versions"]["nodes"]:
        if (i["version"] == version) and ("GITHUB_OUTPUT" in os.environ):
            with open(os.environ["GITHUB_OUTPUT"], "w") as f :
                f.write('value=true')
get_version(versionToCheck)
