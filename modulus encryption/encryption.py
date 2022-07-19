def encrypt(flag):
	enc_flag = ""
	for i in range(len(flag)):
		enc_flag += chr(ord(flag[i]) + i % 5)
		
	return enc_flag
	
flag = open('flag.txt', 'r+').read()

print(encrypt(flag))