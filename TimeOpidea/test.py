import requests
import json
url="https://api.whenhub.com/api/users/me/schedules"

#response = requests.request("GET",url,headers={'Authorization': 'BxITBF5vUk5nntSSa1Eb1xrvLBgfFdCVvwKkctUFlyyBBMlvC2IqMcvn4CJGDpK5'})

id="5909e47cb4256e1c8032f45f"
url="https://api.whenhub.com/api/users/me/schedules/"+id+"/events"

#data = json.dumps({'period':'2016','startDate':'2016'})
data = {'period': '2016','startDate': '2016'}
when=[{'when':[{'period': 'year','startDate': '2017'}]}]
#print(when.period)
response = requests.post(url,headers={'Content-type': 'application/json', 'Accept': 'text/plain','Authorization': 'BxITBF5vUk5nntSSa1Eb1xrvLBgfFdCVvwKkctUFlyyBBMlvC2IqMcvn4CJGDpK5'},json=data)
print(response.content)


    




