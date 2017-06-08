from tag import Tag
import json_io
import sys,datetime

argl = len(sys.argv)
server = sys.argv[1]
i=2
string = ""
while i < argl:
     string += sys.argv[i]+" "
     i+=1

data = Tag()

now = datetime.datetime.now()
data.addData("DateTime",str(now.date())+"_"+str(now.time()))
data.addData("Server", server)
data.addData("Data",string)

print(json_io.encodeJSON(data))
