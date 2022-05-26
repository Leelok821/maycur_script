# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""
import json

import requests

# 获取压测公司
header = {
    'tokenid': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJtYXljdXJfand0X3VhdF9pZCIsInN1YiI6IlVJMjEwOTAxWFMwV1NHMiIsImlhdCI6MTY1MzU1MjQ3NiwiYXVkIjoiQk9TUyIsImV4cCI6MTY1MzU1OTY3Nn0.APJx2Y4XJPmJOYm5YuLNAdz-1lK0nrJ_NBzANbulsOY',
    'user': 'UI210901XS0WSG2',
    'Content-type': 'application/json'
}
body = {
  "pageSize": 100,
  "currentPage": 1,
  "product": "MAYCUR_V2",
  "keyword": "a111",
  "sort": {
    "createAt": False,
    "licenceEndAt": False
  },
  "isolation": True,
  "categories": [
    "PROBATION",
    "PAY",
    "FREE"
  ],
  "licenseDurationStart": "",
  "createStart": ""
}

url = 'https://boss-uat.maycur.com/backend/enterprises'


def add_serve(ent_code):
    url = 'https://boss-uat.maycur.com/backend/capi/v1/enterprise/optional/service/capacity'
    header = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJ0cnVzdCJdLCJleHAiOjE2NTM2MDc1OTMsImp0aSI6ImQ5ZDU1YTVlLWE2NzYtNDU2MC1iMzEzLTk0ZmU2YzIzMjA2NiIsImNsaWVudF9pZCI6ImxlZV9tYXljdXJfcGFhcyJ9.z9DNG2IjAJURaTx1Sj9hbuc7d02QWLqSjTnvuiAP2sw',
        'Content-type': 'application/json'
    }
    data = {
        "serviceCode": "INVOICE",
        "entCode": ent_code,
        "capacity": 100,
        "operator": "",
        "optType": "ADD",
        "unlimited": False,
        "durationStart": 1611210528000,
        "durationEnd": 1781210528000}
    requests.request(
        method='put',
        url=url,
        headers=header,
        data=json.dumps(data),
    )


def add_usage(ent_code):
    url = 'https://boss-uat.maycur.com/backend/capi/v2/enterprise/invoice/identify/capacity'
    header = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJ0cnVzdCJdLCJleHAiOjE2NTM2MDc1OTMsImp0aSI6ImQ5ZDU1YTVlLWE2NzYtNDU2MC1iMzEzLTk0ZmU2YzIzMjA2NiIsImNsaWVudF9pZCI6ImxlZV9tYXljdXJfcGFhcyJ9.z9DNG2IjAJURaTx1Sj9hbuc7d02QWLqSjTnvuiAP2sw',
        'Content-type': 'application/json'
    }
    data = {"code": "INVOICE", "entCode": ent_code, "used": 10, "operator": ""}
    requests.request(
        method='put',
        url=url,
        headers=header,
        data=json.dumps(data),
    )


for i in range(15, 75):
    body['currentPage'] = i
    req = requests.request(
        method='post',
        url=url,
        headers=header,
        data=json.dumps(body),
    ).json()
    for data in req['payload']['data']:
        ent = data['code']
        print(ent)
        if ent.startswith('a'):
            add_serve(ent)
            add_usage(ent)

