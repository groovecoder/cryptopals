def strxor(str1, str2):
    return "%x" % (int(str1, 16) ^ int(str2, 16))

print strxor('1c0111001f010100061a024b53535009181c',
             '686974207468652062756c6c277320657965')
