import json
from .serializationTag import SerializationTag

error=("Argument Tag must be instance of SerializationTag")

def encodeJSON(tag):
    assert isinstance(tag, SerializationTag), error[0]
    return json.dumps(tag.getDict())

def decodeJSON(tag):
    pass
