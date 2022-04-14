
from __future__ import unicode_literals
import requests, sqlite3
import json
from requests.auth import HTTPBasicAuth
import datetime

database = sqlite3.connect("onadata.db")
cursor = database.cursor()


cursor.execute("SELECT * FROM onatable ");
rows = cursor.fetchall()
print(rows[-1])
print(rows[-1][-1])

