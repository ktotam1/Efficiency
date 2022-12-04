import os
import sys
import requests


def main():
    
   
    java_code = open('./App.java').read()
    url = "https://fd3d-2001-620-618-5a0-2-80b3-0-5fa.eu.ngrok.io"
    print(java_code)
    resp = requests.post(url, json=java_code)
    
    print(resp)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
