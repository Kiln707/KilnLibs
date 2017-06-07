#Find the next instance of character
def charPos(char, string, pos=0):
        for i in range(pos+1, len(string)):
                if string[i] is char:
                        return i
        return -1

def substring(string, startpos=0, endpos=None):
        if endpos is None:
                endpos = len(string)
        return string[startpos : endpos]

def toNumeric(s, noError=False):
        if not isinstance(s, str) or not isNumeric(s):
                if noError:
                        return None
                else:
                       raise ValueError("Passed value is not a String or is not Numeric")
        if isInteger(s):
                return int(s)
        elif isFloat(s):
                return float(s)
        elif isComplex(s):
                return complex(s)

def isNumeric(s):
        return isInteger(s) or isFloat(s) or isComplex(s)

def isInteger(s):
        try:
                int(s)
                return True
        except ValueError:
                return False

def isFloat(s):
        try:
                float(s)
                return True
        except ValueError:
                return False

def isComplex(s):
        try:
                complex(s)
                return True
        except ValueError:
                return False
