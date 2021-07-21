from Crypto.Cipher import AES

msg = b"Hello World"
while len(msg) % 16:
	msg += b"#"

# print(msg)
key = b"Yellow Submarine"

aes = AES.new(key, AES.MODE_ECB)

#encrypted msg
enc_msg = aes.encrypt(msg)
print(enc_msg)

#decrypted msg
dec_msg = aes.decrypt(enc_msg)
print(dec_msg)