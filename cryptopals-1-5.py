#! /usr/bin/env Python3

'''
stanza = 'This is a stanza'
stanza_hex = stanza.encode('utf-8').hex()
'''
 
def xor(plaintext, key):
	plaintext_hex = plaintext.encode('utf-8').hex()
	key_hex = key.encode('utf-8').hex()
	return key_hex, plaintext_hex
print(xor(plaintext, key))







plaintext = input('Please input a plaintext stream to be encrypted: ')
key = input('Please input a key value to encrypt plaintext: ')