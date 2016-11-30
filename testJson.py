import json

def returnInfoWithJson():
	data = {}
	data["status"]=500
	data["result"]=[]
	data["result"].insert(0,{"que_id":12,"que_des":"qwe"})
	data["result"].insert(1,{"que_id":34,"que_des":"asd"})
	data = json.dumps(data)
	return data

def getInfoFromJson(data):
	return data["result"][0]["q1"]

data = {"status":200, "id":"123456", "result":[{"q1":"q1","a1":"a2"},{"q2":"q2"}]}
data = json.dumps(data)
data = json.loads(data)
print returnInfoWithJson()

