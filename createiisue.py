import requests
import json
url="https://honey13.atlassian.net//rest/api/2/issue"
heardrs={
    "Accept":"application/json",
    "content-Type":"application/json"
}
pt=json.dumps (
    {
        "fields": {
            "project":
             {
                 "key":"HC"
             },
             "summary":input(),
             "description":input(),
            #  "Due date":input(),
            #  "Start date":input(),
             "issuetype": {
                 "name": "Task"
             }   
        }
    }
)
result=requests.post(url,headers=heardrs,data=pt,auth=("honey22@navgurukul.org","2hIFgdy5RHYaUTJnWK6Z172D"))
print(result.text)
