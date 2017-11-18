from Serialization import SerializationTag
from Serialization import json_io

def printTagData(tag):
    assert isinstance(tag, SerializationTag), "Tag needs to be of instance SerializationTag"
    print(tag.getKeys())
    for key, val in tag.getDict().items():
        print(key+": "+str(val))
        if isinstance(val, SerializationTag):
            print("--------------START TAG-------------------")
            printTagData(val)
            print("---------------END TAG--------------------")

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

print(set(list(st)))


###############
# Tag Test
###############
tag = SerializationTag()
tag.addData('bool1', bool1)
tag.addData('bool2', bool2)
tag.addData('byte', byte)
tag.addData('char', char)
tag.addData('comp',comp)
tag.addData('float',flt)
tag.addData('integer',integer)
tag.addData('string',string)
tag.addData('dictionary',dic)
tag.addData('set',st)
tag.addData('frozenset',fst)
tag.addData('tuple',tup)
tag.addData('list',lst)
tag.addData('breaking?', "[date time] [Info] This line should not be broken up")

## Testing Subtag Function
#Depreciated
#sub = tag.addSubTag('subtag')
sub = SerializationTag()

sub.addData('bool1', bool1)
sub.addData('bool2', bool2)
sub.addData('byte', byte)
sub.addData('char', char)
sub.addData('comp',comp)
sub.addData('float',flt)
sub.addData('integer',integer)
sub.addData('string',string)
sub.addData('dictionary',dic)
sub.addData('set',st)
sub.addData('frozenset',fst)
sub.addData('tuple',tup)
sub.addData('list',lst)

#Testing remove data
sub.removeData('bool1')
tag.addData('sub1', sub)

######################
# Testing adding a tag
#######################
sub2 = SerializationTag(sub)

sub2.addData('xbool1', bool1)
sub2.addData('xbool2', bool2)
sub2.addData('xbyte', byte)
sub2.addData('xchar', char)
sub2.addData('xcomp',comp)
sub2.addData('xfloat',flt)
sub2.addData('xinteger',integer)
sub2.addData('xstring',string)
sub2.addData('xdictionary',dic)
sub2.addData('xset',st)
sub2.addData('xfrozenset',fst)
sub2.addData('xtuple',tup)
sub2.addData('xlist',lst)

tag.addData('tag2', sub2)
sub.addData('t2',sub2) #Modified after adding to tag


#################################
# Testing SerializationTag
#################################
printTagData(tag)

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

bool1test = tag.getBool('bool1')
bool2test = tag.getBool('bool2')
bytetest = tag.getBytes('byte')

print(json_io.encodeJSON(tag))
