from cryptography.fernet import Fernet


file = open('key.txt', 'rb')
key = file.read()
file.close()

message = "bruh"
encoded = message.encode()
print(key)
f = Fernet(key)
print(f)
print(encoded)

encrypt = f.encrypt(encoded)
print(encrypt)
print("-----------")
file = open('key.txt', 'rb')
key2 = file.read()
file.close()

f2 = Fernet(key2)
print(key2)
print(f2)
decrypted = f2.decrypt(encrypt)
print(decrypted)