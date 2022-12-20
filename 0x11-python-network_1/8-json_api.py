#!/usr/bin/python3
"""script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {"q": letter}
    response = requests.post(url, data=value)
    try:
        res = response.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
