from Serialization import SerializationTag
import sys, json
###############
#Test Values:
###############
testValues={
    "bool1":True,
    "bool2":False,
    "byte":int(255).to_bytes(2,'big', signed=True ),
    "chr":chr(65),
    "complex":complex(976418),
    "float":354.264,
    "int":int(689),
    "string":"This is a value",
    "dict":{'Yoho': "A bottle of rum", "sumval": 45},
    "set":{1,2,3,4,5},
    "frozenset":frozenset({1,2,3,4,5}),
    "tuple":(1,2,3,4,5),
    "list":[1,2,3,4,5,6,7,8,9,0]
    }

def buildTag():
    tag = SerializationTag()
    for key,val in testValues.items():
        tag.addData(key,val)
    sub = SerializationTag()
    for key,val in testValues.items():
        sub.addData(key,val)
    tag.addData("sub1",sub)
    sub2=SerializationTag(sub)
    tag.addData("sub2",sub2)
    return tag

def validTag(tag, verbose=False):
    assert isinstance(tag, SerializationTag), "Tag needs to be of instance SerializationTag"
    for key in tag._getDict().keys():
        if not (key in testValues or key == "sub1" or key == "sub2" or key == 'DATATYPE'):
            print("Tag not created by SerializationTagTest. Cannot Validate!", key)
            return False
    validated = True
    testKeys = testValues.keys()
    for key in tag._getDict().keys():
        if key == 'sub1' or key == 'sub2':
            if verbose: print("Testing SerializationTag for Key:", key)
            if validTag(tag.getSerializationTag(key)):
                if verbose: print("SerializationTag value validated successfully!")
            else:
                if verbose: print("SerializationTag vlaue did not Validate!")
                validated = False
        elif key == "bool1" or key == "bool2":
            if testValues[key] == tag.getBool(key):
                if verbose: print("Boolean value validated!")
            else:
                validated = False
                if verbose: print("Boolean value failed to Validate!")
        elif key == "byte":
            if testValues[key] == tag.getBytes(key):
                if verbose: print("Byte value validated!")
            else:
                validated = False
                if verbose: print("Byte value failed to Validate!")
        elif key == "chr":
            if testValues[key] == tag.getChr(key):
                if verbose: print("Character value validated!")
            else:
                validated = False
                if verbose: print("Character value failed to Validate!", key, type(testValues[key]), type(tag,getChr(key)))
        elif key == "complex":
            if testValues[key] == tag.getComplex(key):
                if verbose: print("Complex value validated!")
            else:
                validated = False
                if verbose: print("Complex value failed to Validate!")
        elif key == "float":
            if testValues[key] == tag.getFloat(key):
                if verbose: print("Float value validated!")
            else:
                validated = False
                if verbose: print("Float value failed to Validate!")
        elif key == "int":
            if testValues[key] == tag.getInt(key):
                if verbose: print("Integer value validated!")
            else:
                validated = False
                if verbose: print("Integer value failed to Validate!")
        elif key == "str":
            if testValues[key] == tag.getStr(key):
                if verbose: print("String value validated!")
            else:
                validated = False
                if verbose: print("String value failed to Validate!")
        elif key == "dict":
            if testValues[key] == tag.getDict(key):
                if verbose: print("Dictionary value validated!")
            else:
                validated = False
                if verbose: print("Dictionary value failed to Validate!")
        elif key == "set":
            if testValues[key] == tag.getSet(key):
                if verbose: print("Set value validated!")
            else:
                validated = False
                if verbose: print("Set value failed to Validate!")
        elif key == "frozenset":
            if testValues[key] == tag.getFrozenset(key):
                if verbose: print("FrozenSet value validated!")
            else:
                validated = False
                if verbose: print("FrozenSet value failed to Validate!")
        elif key == "tuple":
             if testValues[key] == tag.getTuple(key):
                 if verbose: print("Tuple value validated!")
             else:
                 validated = False
                 if verbose: print("Tuple value failed to Validate!")
        elif key == "list":
            if testValues[key] == tag.getList(key):
                if verbose: print("List value validated!")
            else:
                validated = False
                if verbose: print("List value failed to Validate!")
    return validated


def printTagData(tag):
    assert isinstance(tag, SerializationTag), "Tag needs to be of instance SerializationTag"
    print(tag.getKeys())
    for key, val in tag._getDict().items():
        if type(val) is bytes:
            print(key+": "+val)
        else:
            print(key+": "+str(val))
        if isinstance(val, SerializationTag):
            print("--------------START TAG-------------------")
            printTagData(val)
            print("---------------END TAG--------------------")



#################################
# Testing SerializationTag
#################################

print(type( testValues["byte"]), testValues["byte"])
tag = buildTag()
if validTag(tag):
    print("Tag validated successfully against itself!")
else:
    print("Tag failed to validate against itself!")
    sys.exit(1)
JSONDATA = SerializationTag.encodeJSON(tag)
try:
    json.loads(JSONDATA)
    print(JSONDATA)
    print("Tag convertion to JSON validated successfully!")
except ValueError:
    print("Tag convertion to JSON failed to validate!")

if validTag(SerializationTag.decodeJSON(JSONDATA)):
    print("Tag validated successfully after encoding/decoding through JSON!")
else:
    print("Tag failed to validate after encoding/decoding through JSON!")
    sys.exit(1)
