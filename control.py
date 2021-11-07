def lookForIn(param, data,key = None):
    if key == None: 
        for x in data:
            if x == param:
                return True
    else:
        for x in data:
            if x[key] == param:
                return True
    return False

class Validate(object):
    def byGreaterLen(data,number):
        if len(data) > number:
            return True
        else:
            return False
    
    def bySmallerLen(data,number):
        if len(data) < number:
            return True
        else:
            return False
    def byChar(data,arg):
        count = 0
        for x in data:
            if x == arg:
                count += 1
        if count > 0:
            return True
        else:
            return False
    class simpleIf(object):
        def greaterThan(data,arg):
            if data > arg:
                return True
            else:
                return False

        def smallerThan(data,arg):
            if data < arg:
                return True
            else:
                return False
        
        def equalTo(data,arg):
            if data == arg:
                return True
            else:
                return False
