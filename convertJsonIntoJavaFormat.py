#!/usr/bin/env python3
import json
import os

dataString = '''{
    "id": "1",
    "description": "description of gist",
    "public": true,
    "comments": 0,
    "created_at": "2010-04-14T02:15:15Z",
    "updated_at": "2011-06-20T11:34:15Z"
  }''';
data = json.loads(dataString);



STRING = "String"
BOOLEAN = "boolean"
INT = "int"

with open("converjava.txt", mode="w", encoding="utf-8") as a_file:
    for k, v in data.items():
        print(k)
        typeStr = "";
        if isinstance(v, bool):
            typeStr = BOOLEAN
        elif isinstance(v, int):
            typeStr = INT
        elif isinstance(v, str):
            typeStr = STRING
        else:
            typeStr = STRING
        
        format = "private {} {};\n"
        text = format.format(typeStr, k)
        a_file.write(text)

