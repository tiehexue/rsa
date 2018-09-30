# padding chars with fixed width
def padding(i, length):
    return ("%0" + str(length) + "d") % i


# numbers split to max length as "len(rsa.m) - 1"
def chunk_string(string, length):
    return list(string[0+i:length+i] for i in range(0, len(string), length))
