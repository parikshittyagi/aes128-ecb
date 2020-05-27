import os,binascii
from Crypto.Cipher import AES

randNumber = binascii.b2a_hex(os.urandom(7))
randNumber = randNumber + '00'
print("Challenge -> "+randNumber)

key = '354226452948404D635166546B576E5B'
cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.encrypt(randNumber)
msg = msg.encode("hex")
msg += '000000000000'
print("Response - > " + msg)
