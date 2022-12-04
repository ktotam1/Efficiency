import os
import sys
import requests


def main():
    
   
    java_code = open('./App.java').read()
    url = "https://b77b-2001-620-618-5a0-2-80b3-0-5fa.eu.ngrok.io/predict_code"
   # h1 = http.client.HTTPConnection(url)
    
    print(java_code)
    resp = requests.post(url, json=java_code)
    print("predicted running time:")
    print(resp.content)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
