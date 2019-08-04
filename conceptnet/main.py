import requests

def concept(word):
  obj = requests.get("http://api.conceptnet.io/c/en/"+word).json()
  # print(obj.keys())
  print("related terms")
  for i in range(len(obj["edges"])):
    print(obj["edges"][i]["surfaceText"])
    print(obj["edges"][i]["weight"])
    print("\n")

concept("water")
