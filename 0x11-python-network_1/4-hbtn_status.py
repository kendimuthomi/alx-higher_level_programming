#!/usr/bin/python3
"""fetching a url using urllib"""
import requests
if __name__ == "__main__":
    re = requests.get("https://alx-intranet.hbtn.io/status")
    html = re.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
