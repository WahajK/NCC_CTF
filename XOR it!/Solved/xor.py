key = "supersecretkeysupersecre"

flag='=63\x1e\nC\x17<\nU\x064\x1dI\x01*AVGKWZA\x18'
print(len(flag))
print(len(key))

#encryption scheme
encrypted_flag = ''.join([chr(ord(flag[i]) ^ ord(key[i])) for i in range(len(flag))])
print(encrypted_flag)
#encoded flag
