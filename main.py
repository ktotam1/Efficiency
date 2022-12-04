import os
import sys
import requests
import json

def main():
    
   
    java_code = open('./App.java').read()
    url = "https://b77b-2001-620-618-5a0-2-80b3-0-5fa.eu.ngrok.io/predict_code"
   # h1 = http.client.HTTPConnection(url)
    
    #print(java_code)
    resp = requests.post(url, json={'code': java_code})
    print("predicted running time:")
    ans = json.loads(resp.content.decode())
    print("carbon cost: " + ans["carbon_cost"])
    print("carbon comparison: " + ans["carbon_comparison"])
    print("electricity cost: " + ans["electricity_cost"])
    print("cost: " + ans["monetary_cost"])
    print("region recommendation: " + ans["server_region_recommendation"])
    print("hardware recommendation: " + ans["hardware_recommendation"])


    
    sys.exit(0)


if __name__ == "__main__":
    main()
