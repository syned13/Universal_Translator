def getUnit(letter):
    l = letter.lower()
    if l == "km":
        return 1000
    elif l == "m":
        return 1
    elif l == "cm":
        return 0.01
    elif l == "mm":
        return 0.001
    elif l == "dam":
        return 10
    elif l == "dm":
        return 10
    elif l == "hm":
        return 100

def convert(magnitude,current,future):

    #llevar a metros
    measure = magnitude * current

    #llevar de metros a target
    measure = measure / future

    return measure
