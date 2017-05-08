import requests
import json


def createSchedule(name):

    uid='59003c0e5467923f8478d1d7'
    data=[
      {
        'name': name,
        'scope':'public'
       }
     ]
    url="https://api.whenhub.com/api/users/"+uid+"/schedules"

    response = requests.post(url,headers={'Content-type': 'application/json', 'Accept': 'text/plain','Authorization': 'BxITBF5vUk5nntSSa1Eb1xrvLBgfFdCVvwKkctUFlyyBBMlvC2IqMcvn4CJGDpK5'},json=data)
    print(response.content)
    return response.content

def addEvent(sId,year,desc):
          
    url="https://api.whenhub.com/api/users/me/schedules/"+sId+"/events"
    data=[
     {
      "when":{
      "period":"year",
      "startDate":year
        },
       "name":year,
       "description":desc,
          
     }
    ]
    response = requests.post(url,headers={'Content-type': 'application/json', 'Accept': 'text/plain','Authorization': 'BxITBF5vUk5nntSSa1Eb1xrvLBgfFdCVvwKkctUFlyyBBMlvC2IqMcvn4CJGDpK5'},json=data)
    return response.content.id
def addWhencast(id,name):

    url="https://api.whenhub.com/api/users/me/schedules/"+id+"/whencasts"
    data=[
        {
          "name": name,
         "defaultWhencast": true  
  
        }
    ]
    response = requests.post(url,headers={'Content-type': 'application/json', 'Accept': 'text/plain','Authorization': 'BxITBF5vUk5nntSSa1Eb1xrvLBgfFdCVvwKkctUFlyyBBMlvC2IqMcvn4CJGDpK5'},json=data)
    return response.content.id

