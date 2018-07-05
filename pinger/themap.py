#!/usr/bin/env python

import re
import os
import sys
from argparse import ArgumentParser
from pymongo import MongoClient
import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import asyncio
from aiohttp import ClientSession
import resource
import subprocess

"""

python3 themap.py -c='netpro:password'

"""

parser = ArgumentParser(description="Pull gelocations from mongodb and ingest into elastic")
parser.add_argument("-c", "--credentials", dest="credentials", default='netpro:password',
                    help="user name and password", metavar="USER PASS")                     
parser.add_argument("-a", "--addressport", dest="addressport", default='10.254.253.100:27017',
                    help="server address and port", metavar="SERVER ADDRESS AND PORT")
                    

args = parser.parse_args()
index = 'index-pinger'
pipeline = 'pinger'
credentials = args.credentials
addressport = args.addressport
mongo='mongodb://' + credentials + '@' + addressport
data='meteor'
coll='robo'

#https://coderwall.com/p/ptq7rw/increase-open-files-limit-and-drop-privileges-in-python
#print(resource.getrlimit(resource.RLIMIT_NOFILE))
resource.setrlimit(resource.RLIMIT_NOFILE, (1500, 1500))
#print(resource.getrlimit(resource.RLIMIT_NOFILE))
#print(subprocess.check_output("whoami; ulimit -n", shell=True))


try:
    client = MongoClient(
      host=mongo,
      unicode_decode_error_handler='ignore'
      )
except:
    quit("Conenction error")    

db = client[data]
robo=db[coll]
# test
# pprint.pprint(robo.find_one({"Name":"Irek-11"}))


"""
pymongo_cursor = db.collection.find()
all_data = list(pymongo_cursor)
print(type(all_data))
"""

"""
https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
"""
async def hello(url,data,headers):
    async with ClientSession() as session:
        async with session.put(url, json=data, headers=headers) as response:
            response = await response.read()
            #print(response)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {'Content-type': 'application/json'}
print(robo.count())
cursor = robo.find({}, { u'Ext': 1, u'Name': 1, u'_id': 0 })
#cursor = robo.find({})
loop = asyncio.get_event_loop()
tasks = []
for shield in cursor:
      #https://stackoverflow.com/questions/1254454/fastest-way-to-convert-a-dicts-keys-values-from-unicode-to-str
      # shield = {str(k):(str(v) if isinstance(v, unicode) else v) for k,v in shield.items()}
      shield = {str(k): str(v) for k, v in shield.items()}
      #print(shield['Name'],shield['Ext'])
      data = {"message":shield['Ext']}
      url = 'http://10.254.253.144:9200/'+ index + '/_doc/' + shield['Name'] + '?pipeline='+pipeline 
      #r = requests.put(url, data=json.dumps(data), headers=headers)
      task = asyncio.ensure_future(hello(url,data,headers))
      tasks.append(task)
      #print(r.text)
loop.run_until_complete(asyncio.wait(tasks))








