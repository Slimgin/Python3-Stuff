address = "123 north anywhere street"
direction = {"NORTH":"N", "SOUTH":"S" }

for word, initial in direction.items():
    address = address.replace(word.lower(), initial)
print address

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#translate = {'a':'c', 'c':'e', 'b':'d', 'e':'g', 'd':'f', 'g':'i', 'f':'h', 'i':'k', 'h':'j', 'k':'m', 'j':'l', 'm':'o', 'l':'n', 'o':'q', 'n':'p', 'q':'s', 'p':'r', 's':'u', 'r':'t', 'u':'w', 't':'v', 'w':'y', 'v':'x', 'y':'a', 'x':'z', 'z':'b'}
translate = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h', 'g':'i', 'h':'j', 'i':'k', 'j':'l', 'k':'m', 'l':'n', 'm':'o',
		     'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 't':'v', 'u':'w', 'v':'x', 'w':'y', 'x':'z', 'y':'a', 'z':'b' }

for key, value in translate.items():
	input = input.replace(key, value.lower())
print input