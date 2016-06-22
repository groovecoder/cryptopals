import string

hexstr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

for char in string.ascii_letters:
    print "%x" % (int(hexstr, 16) ^ int(char.encode('hex'), 16))
