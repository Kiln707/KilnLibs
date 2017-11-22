import json
from .serializationTag import SerializationTag

error=("Argument Tag must be instance of SerializationTag")

class SerializationTagEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, SerializationTag):
            return json.dumps(obj.getDict(), cls=SerializationTagEncoder)
        return json.JSONEncoder.default(self, obj)

def encodeJSON(tag):
    assert isinstance(tag, SerializationTag), error[0]
    return json.dumps(tag.getDict(), cls=SerializationTagEncoder)

def decodeJSON(tag):
    pass
