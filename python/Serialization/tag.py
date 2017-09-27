class SerializationTag:
    error=("Argument for tag_name is already in use. tag_name=",
    "Argument tag must be None or an instance of SerializationTag",
    "Value for argument value must be one of the following types: bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag"
    )
    #Constructor for new SerializationTag serialization
    def __init__(self,tag=None):
        assert isinstance(tag, SerializationTag) or tag is None, error[1]
        if tag is None: #Creating a new instance of SerializationTag
            self.dict = {}
        else:   #Creating a copy of SerializationTag
            self.dict = tagInfo

    def createSubSerializationTag(self, tag_name):
        assert not self.keyExists(tag_name), errors[0]+tag_name
        self.dict[tag_name] = SerializationTag()
        return self.dict[tag_name]

    def addData(self, tag_name, value):
        allowedValues = (bool, bytes, chr, complex, float, int, str, dict, frozenset, set, tuple, list, SerializationTag)
        assert type(value) in allowedValues, error[2]
        assert not self.keyExists(tag_name), errors[0]+tag_name
        self.dict[tag_name] = value
        return value

    def getData(self, tag_name):
        return self.dict[tag_name]

    def deleteData(self, tag_name, reportSuccess=False, tagCheck=False):
        if tagCheck:
            assert self.keyExists(tag_name), errors[0]+tag_name
        if reportSuccess:
            if self.keyExists(tag_name):
                del self.dict[tag_name]
                return True
            else:
                return False
        else:
            del self.dict[tag_name]

    def getKeys(self):
        return self.dict.keys()

    def keyExists(self, key):
        if key in self.dict:
            return True
        return False

    def __getDict(self):
        return self.dict
