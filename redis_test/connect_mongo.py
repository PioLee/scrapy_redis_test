import json
from collections import defaultdict

from pymongo import MongoClient
import datetime
import csv

post = defaultdict(list)
# client = MongoClient()
# db = client.test
# collection = db.mytest
# collection.insert_one({"name": "lee"})
# res = collection.update_one({"asin": 'B0000003'}, {"$set": post}, upsert=True)
# print(res)
# print(res.matched_count, res.modified_count)
# for i in collection.find():
#     print(i)
# w = 299
# client = MongoClient()
# db = client.oalur
# collection = db.foamlogistics
# collection.insert_one(post)
# pid = collection.find()
# for p in pid:
#     print(p)
trans_dict = dict()
with open('trans.json', "r", encoding='utf-8')as rf:
    data = json.loads(rf.read())['RECORDS']
for k in data:
    trans_dict[k['id']] = k['shorthand']
# print(trans_dict)
with open('freight.csv', 'r', encoding='utf-8-sig')as f:
    reader = csv.reader(f)
    for i in reader:
        item = defaultdict(list)
        weight = dict()
        content = dict()
        content.setdefault('ship', '')
        content.setdefault('country', [])
        content['ship'] = trans_dict[int(i[1])]
        # weight[i[2]] = [i[3], i[4], i[5], i[6]]
        # item[i[0]].append(weight)
        # content['country'].append(item)
        post['data'].append(content)
print(post)



