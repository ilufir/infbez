def gamma(istr,key):
    output = ""
    for i in range(0,len(istr)):
        output += chr(ord(istr[i]) ^ ord(key[i]))
    return output

text1 = "С Новым годом!"
text2 = "S_Novym_Godom."
key =  "ABCDEFGHIJKLMN"

cipher1 = gamma(text1,key)
cipher2 = gamma(text2,key)

print(cipher1)
print(cipher2)

print(gamma(cipher1,key))
print(gamma(cipher2,key))

print(gamma(gamma(cipher2,cipher1),text2))

print(gamma(cipher2,cipher1))
