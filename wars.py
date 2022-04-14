from __future__ import unicode_literals
import requests, sqlite3
import json
from requests.auth import HTTPBasicAuth
import datetime

database = sqlite3.connect("dantedata.db")
cursor = database.cursor()

def json_serial(obj):

    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

try:
    cursor.execute("SELECT * FROM onatable ");
    rows = cursor.fetchall()
    time_var = (rows[-1][-1])
except:    
    time_var = json_serial(datetime.datetime(1970,1,1))

table_id = 661447

ona_url ='https://api.ona.io/api/v1/data/'

auth_set = ('dantekariuki','Kariyki6996@')


query_str ={"_submission_time":{"$gte":time_var}}

request_url = ona_url+str(table_id)+'?query='+json.dumps(query_str)

response = json.loads(requests.get(
    request_url,
    auth=auth_set
).text)

print(response)
print(time_var)

for i in response:
    name = (i.get('Name'))
    age = (i.get('Age'))
    gender = (i.get('Gender'))
    submission_date = (i.get('_submission_time'))
  
    cursor.execute("INSERT INTO onatable (name, age, gender,submission_date ) VALUES (?,?,?,?);", (name,age,gender,submission_date))
    database.commit()