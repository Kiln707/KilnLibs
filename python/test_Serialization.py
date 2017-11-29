from Serialization import SerializationTag
from Serialization import json_io

values = {}

def printTagData(tag):
    assert isinstance(tag, SerializationTag), "Tag needs to be of instance SerializationTag"
    print(tag.getKeys())
    for key, val in tag.getDict().items():
        print(key+": "+str(val))
        if isinstance(val, SerializationTag):
            print("--------------START TAG-------------------")
            printTagData(val)
            print("---------------END TAG--------------------")

<<<<<<< Updated upstream
def createTagData(values):
    tag = SerializationTag()
    print(values)
    for key,val in values.items():
        tag.addData(key,val)
    tag.addData('breaking?', "[date time] [Info] This line should not be broken up")

    sub = SerializationTag()
    for key,val in values.items():
        sub.addData(key,val)
    sub.removeData("bool1")
    tag.addData("sub1",sub)

    sub2=SerializationTag(sub)
    tag.addData("sub2",sub2)
    return tag


=======
def primeTag(tagDict):


###############
#Test Values:
###############
bool1 = True
bool2 = False
byte = bytes(35)
char = chr(65)
comp = complex(976418)
flt = 354.264
integer = int(689)
string = "This is a value"
dic = {'Yoho': "A bottle of rum", "sumval": 45}
st = {1,2,3,4,5}
fst = frozenset(st)
tup = (1,2,3,4,5)
lst = [1,2,3,4,5,6,7,8,9,0]

>>>>>>> Stashed changes
###############
#Test Values:
###############
testValues={
    "bool1":True,
    "bool2":False,
    "byte":bytes(35),
    "char":chr(65),
    "comp":complex(976418),
    "flt":354.264,
    "integer":int(689),
    "string":"This is a value",
    "dict":{'Yoho': "A bottle of rum", "sumval": 45},
    "set":{1,2,3,4,5},
    "fset":frozenset({1,2,3,4,5}),
    "tup":(1,2,3,4,5),
    "lst":[1,2,3,4,5,6,7,8,9,0]
    }
tag = createTagData(testValues)

#################################
# Testing SerializationTag
#################################
printTagData(tag)
print('JSON:')
JSONDATA = json_io.encodeJSON(tag)
print(JSONDATA)
print("DECODE:")
printTagData(json_io.decodeJSON(JSONDATA))
