import json
from .serializationTag import SerializationTag

error=("Argument Tag must be instance of SerializationTag",
        "Argument json must be a string value.")

class SerializationTagEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SerializationTag):
            return obj.getDict()
        return json.JSONEncoder.default(self, obj)

class SerializationTagDecoder(json.JSONDecoder):
    def decode(self, obj):
        data = json.JSONDecoder.decode(self, obj)
        if type(data) is dict and 'DATATYPE' in data:
            for key, val in data.items():
                print(key, val)
                if type(val) is dict:
                    data[key]=SerializationTag(val)
            return SerializationTag(data)
        return data

def encodeJSON(tag):
    assert isinstance(tag, SerializationTag), error[0]
    return json.dumps(tag ,cls=SerializationTagEncoder, indent=4 )

def decodeJSON(jsonDATA):
    assert type(jsonDATA) is str, error[1]
    return SerializationTag(json.loads(jsonDATA, cls=SerializationTagDecoder))
