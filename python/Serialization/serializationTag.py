class SerializationTag:
    error=("Argument for key is already in use. key=",
    "Argument tag must be None or an instance of SerializationTag",
    "Value for argument value must be one of the following types: bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag",
    "Key does not exist. key=",
    "Stored value is of incorrect type."
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
        else:   #Creating a copy of SerializationTag
            self.dict = tag.getDict()

    '''
    'Insert data with key
    ' TODO: Change to addType, maybe
    '''
    def addData(self, key, value):
        allowedValues = (bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag)
        assert type(value) in allowedValues, SerializationTag.error[2]
        assert not self.keyExists(key), SerializationTag.error[0]+key
        if type(value) is bytes:
            self.dict[key] = value.decode('utf-8')
        elif type(value) is dict and 'DATATYPE' in value:
                self.dict[key] = SerializationTag(value)
        elif type(value) is complex:
            t = {'DATATYPE':'COMPLEX', 'REAL':value.real, 'IMAG':value.imag}
            self.dict[key] = SerializationTag(t)
        elif type(value) is set:
            t = {'DATATYPE':'SET', 'VALUES':list(value)}
            self.dict[key] = SerializationTag(t)
        elif type(value) is frozenset:
            t = {'DATATYPE':'FROZENSET', 'VALUES':list(value)}
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
        assert type(self.dict[key]) is bool, SerializationTag.error[4]
        return bool(self.dict[key])

    def getBytes(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        return self.dict[key].encode('utf-8')

    def getChr(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is chr, SerializationTag.error[4]
        return chr(self.dict[key])

    def getComplex(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists['DATATYPE'] and self.dict[key].getData['DATATYPE'] == 'COMPLEX', SerializationTag.error[4]
        return complex(self.dict[key].getData['REAL'],self.dict[key].getData['IMAG'])

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
        assert self.dict[key].keyExists['DATATYPE'] and self.dict[key].getData['DATATYPE'] == 'FROZENSET', SerializationTag.error[4]
        return frozenset(self.dict[key].getData['VALUES'])

    def getSet(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert isinstance(self.dict[key], SerializationTag), SerializationTag.error[4]
        assert self.dict[key].keyExists['DATATYPE'] and self.dict[key].getData['DATATYPE'] == 'SET', SerializationTag.error[4]
        return set(self.dict[key].getData['VALUES'])

    def getTuple(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is tuple, SerializationTag.error[4]
        return tuple(self.dict[key])

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
    'getKeys
    'Get a list of keys that are registered with the tag_name.
    'Can be used for traversing a tag with unknown named keys.
    '''
    def getKeys(self):
        return self.dict.keys()

    def keyExists(self, key):
        if key in self.dict.keys():
            return True
        return False

    '''
    '   __getDict:
    ' Get the dictionary of the tag, used to make a copy of Tag
    ' Should not be used normally
    '''
    def getDict(self):
        return dict(self.dict) #Return a copy of the dictionary
