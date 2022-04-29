import requests
import json
import subprocess

def Information():
    url = "http://localhost:5000/hello"

    r = requests.get(url)
    print(r.text)

def postImage():
    url = "http://localhost:5000/image"

    payload = {'data': "CSUSM CS Department"}
    headers = {
        'Content-Type': 'application/json'
        }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.text, response.status_code)


if __name__ == "__main__":
    userInput = ""
    while userInput != "exit":
        userInput = input(">>")
        args = userInput.split(" ")
        if userInput == "client":
                Information()
        elif userInput == "client myhand.jpg":
                postImage()

