from tag import Tag
import json_io
import json

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
tag = Tag()
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

## Testing Subtag Function
sub = tag.addSubTag('subtag')

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

######################
# Testing adding a tag
#######################
sub2 = Tag()

sub2.addData('bool1', bool1)
sub2.addData('bool2', bool2)
sub2.addData('byte', byte)
sub2.addData('char', char)
sub2.addData('comp',comp)
sub2.addData('float',flt)
sub2.addData('integer',integer)
sub2.addData('string',string)
sub2.addData('dictionary',dic)
sub2.addData('set',st)
sub2.addData('frozenset',fst)
sub2.addData('tuple',tup)
sub2.addData('list',lst)

tag.addData('tag2', sub2)
sub.addData('t2',sub2) #Modified after adding to tag


#################################
# Tag / JSON Conversions
#################################

#To JSON
JSON = json_io.toJSONString(tag) #To JSON String
print('\nTag to JSON String:\n',JSON ,"\n\n")

JSON = json_io.encodeJSON(JSON) #JSON String to Formatted JSON
print("\nJSON String to Formatted JSON:\n",JSON ,"\n\n")

JSON = json_io.encodeJSON(tag) #Tag to Formatted JSON
print("\nTag to Formatted JSON:\n",JSON ,"\n\n")

#From JSON
a = json_io.decodeJSON(JSON)

#Print Tag Contents
print('Tag Contents:\n')
a.print()

print(json_io.encodeJSON(a))# == JSON)

