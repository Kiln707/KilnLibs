import codecs, json, pickle


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
            self.dict = {}
        elif type(tag) is dict:
            self.dict = dict(tag)
        elif isinstance(tag, SerializationTag):   #Creating a copy of SerializationTag
            self.dict = dict(tag._getDict())

    ####################################
    # Insert data with key
    # This section handles converting the
    # data into usable structures.
    ###################################
    def addData(self, key, value):
        convertionTypes = (bytes, complex, set, frozenset, tuple)
        assert type(value) in (bool, chr, float, int, str, dict, list)+convertionTypes or isinstance(value, SerializationTag), SerializationTag.error[2]
        assert not self.keyExists(key), SerializationTag.error[0]+key
        if type(value) in convertionTypes or isinstance(value, SerializationTag):
            if type(value) is bytes:
                self.dict[key] = codecs.encode(value, 'base64').decode('utf-8')
            elif type(value) is complex:
                t = {'DATATYPE':'COMPLEX', 'REAL':int(value.real), 'IMAG':int(value.imag)}
                self.addData(key, t)
            elif type(value) is set:
                t = {'DATATYPE':'SET', 'VALUES':list(value)}
                self.addData(key, t)
            elif type(value) is frozenset:
                t = {'DATATYPE':'FROZENSET', 'VALUES':list(value)}
                self.addData(key, t)
            elif type(value) is tuple:
                t = {'DATATYPE':'TUPLE', 'VALUES':list(value)}
                self.addData(key, t)
            elif isinstance(value, SerializationTag):
                self.addData(key, value._getDict())
        else:
            self.dict[key] = value
        return self

    ###################################
    #
    ###################################
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
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        assert 'DATATYPE' in self.dict[key] and self.dict[key]['DATATYPE'] == 'COMPLEX', SerializationTag.error[4]
        return complex(self.dict[key]['REAL'],self.dict[key]['IMAG'])

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
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        assert 'DATATYPE' in self.dict[key] and self.dict[key]['DATATYPE'] == 'FROZENSET', SerializationTag.error[4]
        return frozenset(self.dict[key]['VALUES'])

    def getSet(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        assert 'DATATYPE' in self.dict[key] and self.dict[key]['DATATYPE'] == 'SET', SerializationTag.error[4]
        return set(self.dict[key]['VALUES'])

    def getTuple(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        assert 'DATATYPE' in self.dict[key] and self.dict[key]['DATATYPE'] == 'TUPLE', SerializationTag.error[4]
        return tuple(self.dict[key]['VALUES'])

    def getList(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is list, SerializationTag.error[4]
        return list(self.dict[key])

    def getSerializationTag(self, key):
        assert self.keyExists(key), SerializationTag.error[3]+key
        assert type(self.dict[key]) is dict, SerializationTag.error[4]
        return SerializationTag(self.getDict(key))

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
    '''
    Serialization Section
    '''
    serialError=("Argument Tag must be instance of SerializationTag.",
            "Argument json must be a string value.",
            "Argument byteData must be a bytes value.")

    '''
    JSON SECTION
    '''
    def encodeJSON(tag, jsonindent=0):
        assert isinstance(tag, SerializationTag), serialError[0]
        return json.dumps(tag._getDict(),indent=jsonindent)

    def decodeJSON(jsonDATA):
        assert type(jsonDATA) is str, serialError[1]
        return SerializationTag(json.loads(jsonDATA))

    '''
    PICKLE SECTION
    '''
    def encodePickle(tag):
        assert isinstance(tag, SerializationTag), serialError[0]
        return pickle.dumps(tag._getDict(), protocol=pickle.DEFAULT_PROTOCOL)

    def decodePickle(byteData):
        assert type(byteData) is bytes, serialError[2]
        return SerializationTag(pickle.loads(byteData))
