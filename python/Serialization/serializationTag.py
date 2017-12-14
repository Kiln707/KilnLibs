import codecs, base64, json

class SerializationTag:
    error=("Argument for key is already in use. key=",
    "Argument tag must be an instance of SerializationTag, Dict, or None",
    "Value for argument value must be one of the following types: bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag",
    "Key does not exist. key=",
    "Stored value is of incorrect type. Stored value is of Type:"
    )
    #Constructor for new SerializationTag serialization
    def __init__(self,tag=None):
        assert isinstance(tag, SerializationTag) or type(tag) is dict or tag is None, SerializationTag.error[1]
        if tag is None: #Creating a new instance of SerializationTag
            self.dict = {'DATATYPE':'SerializationTag'}
        elif type(tag) is dict:
            if not ( 'DATATYPE' in tag ):
                tag['DATATYPE'] = 'SERIALIZATIONTAG'
            self.dict = dict(tag)
        elif isinstance(tag, SerializationTag):   #Creating a copy of SerializationTag
            self.dict = dict(tag._getDict())

    '''
    'Insert data with key
    ' TODO: Change to addType, maybe
    '''
    def addData(self, key, value):
        allowedValues = (bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag)
        assert type(value) in allowedValues, SerializationTag.error[2]
        assert not self.keyExists(key), SerializationTag.error[0]+key
        if type(value) is bytes:
            self.dict[key] = codecs.encode(value, 'base64').decode('utf-8')
        elif type(value) is dict and 'DATATYPE' in value:
            self.dict[key] = SerializationTag(value)
        elif type(value) is complex:
            t = {'DATATYPE':'COMPLEX', 'REAL':int(value.real), 'IMAG':int(value.imag)}
            self.dict[key] = SerializationTagt)
        elif type(value) is set:
            t = {'DATATYPE':'SET', 'VALUES':list(value)}
            self.dict[key] = SerializationTag(t)
        elif type(value) is frozenset:
            t = {'DATATYPE':'FROZENSET', 'VALUES':list(value)}
            self.dict[key] = SerializationTag(t)
        elif type(value) is tuple:
            t = {'DATATYPE':'TUPLE', 'VALUES':list(value)}
            self.dict[key] = SerializationTag(t)
        else:
            self.dict[key] = value
        return self

    '''
    getData, the main idea. Replaced with methods that should be used. getbool, etc.
    def getData(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        return self.dict[key]
    '''

    def getBool(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is bool, SerializationTag.error[4]+type(self.dict[key])
        return bool(self.dict[key])

    def getBytes(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        return codecs.decode(self.dict[key].encode('utf-8'), 'base64')

    def getChr(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is str and len(self.dict[key]) == 1, SerializationTag.error[4]+str(type(self.dict[key]))
        return chr(ord(self.dict[key]))

    def getComplex(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists('DATATYPE') and self.dict[key]._getDict()['DATATYPE'] == 'COMPLEX', SerializationTag.error[4]
        return complex(self.dict[key].getInt('REAL'),self.dict[key].getInt('IMAG'))

    def getFloat(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is float, SerializationTag.error[4]
        return float(self.dict[key])

    def getInt(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is int, SerializationTag.error[4]
        return int(self.dict[key])

    def getStr(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is str, SerializationTag.error[4]
        return str(self.dict[key])

    def getDict(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        return dict(self.dict[key])

    def getFrozenset(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists('DATATYPE') and self.dict[key]._getDict()['DATATYPE'] == 'FROZENSET', SerializationTag.error[4]
        return frozenset(self.dict[key].getList('VALUES'))

    def getSet(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists('DATATYPE') and self.dict[key]._getDict()['DATATYPE'] == 'SET', SerializationTag.error[4]
        return set(self.dict[key].getList('VALUES'))

    def getTuple(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists('DATATYPE') and self.dict[key]._getDict()['DATATYPE'] == 'TUPLE', SerializationTag.error[4]
        return tuple(self.dict[key].getList('VALUES'))

    def getList(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is list, SerializationTag.error[4]
        return list(self.dict[key])

    def getSerializationTag(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        return SerializationTag(self.dict[key])

    '''
    removeData
    Used to remove data by name from tag.
    Data is not returned upon removal.
    Setting parameter reportSuccess to True will return if data was removed
    from the given key.
    Setting parameter keyCheck with raise an exception if key doesnt exist.
    '''
    def removeData(self, key, reportSuccess=False, keyCheck=False):
        if keyCheck:
            assert self.keyExists(key), SerializationTag.error[0]+tag_name
        if reportSuccess:
            if self.keyExists(key):
                del self.dict[tag_name]
                return True
            else:
                return False
        else:
            del self.dict[key]

    '''
    ' getKeys
    ' Get a list of keys that are registered with the tag_name.
    ' Can be used for traversing a tag with unknown named keys.
    '''
    def getKeys(self):
        return self.dict.keys()

    def keyExists(self, key):
        if key in self.dict.keys():
            return True
        return False

    '''
    ' getDict:
    ' Get the dictionary of the tag, used to make a copy of Tag
    ' Should not be used normally
    '''
    def _getDict(self):
        return dict(self.dict) #Return a copy of the dictionary

    JSONerror=("Argument Tag must be instance of SerializationTag",
            "Argument json must be a string value.")

    class SerializationTagEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, SerializationTag):
                return obj._getDict()
            return json.JSONEncoder.default(self, obj)

    class SerializationTagDecoder(json.JSONDecoder):
        def decodeSerializationTag(value):
            assert type(value) is dict, "Invalid argument type. Needs to be type dict."
            if 'DATATYPE' not in value:
                return value
            for key, val in value.items():
                if type(val) is dict:
                    value[key]=SerializationTag.SerializationTagDecoder.decodeSerializationTag(val)
            return SerializationTag(value)

        def decode(self, obj):
            data = json.JSONDecoder.decode(self, obj)
            if type(data) is dict:
                return SerializationTag.SerializationTagDecoder.decodeSerializationTag(data)
            return data

    def encodeJSON(tag):
        assert isinstance(tag, SerializationTag), JSONerror[0]
        return json.dumps(tag ,cls=SerializationTag.SerializationTagEncoder, indent=4 )

    def decodeJSON(jsonDATA):
        assert type(jsonDATA) is str, JSONerror[1]
        return SerializationTag(json.loads(jsonDATA, cls=SerializationTag.SerializationTagDecoder))
