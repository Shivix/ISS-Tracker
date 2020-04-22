import requests

posRequest = requests.get("http://api.open-notify.org/iss-now.json")
whoRequest = requests.get("http://api.open-notify.org/astros.json")

if posRequest.status_code == 200:
    posReply = posRequest.json()
    
    if type(posReply) == dict:
        print("Latitude:", posReply['iss_position']['latitude'] + ",",
              "Longitude:", posReply['iss_position']['longitude'], "\n")
    else:
        print("Error class type:", type(posReply), "\n")
else:
    print("Error:", posRequest.status_code, "\n")

if whoRequest.status_code == 200:
    whoReply = whoRequest.json()
    if type(whoReply) == dict:
        print("There are", whoReply['number'], "people in space\n\nThey are:")
        for i in range(0, whoReply['number']):
            print(whoReply['people'][i]['name'], "on the", whoReply['people'][i]['craft'])
    else:
        print("Error class type:", type(whoReply))
else:
    print("Error:", whoRequest.status_code)
