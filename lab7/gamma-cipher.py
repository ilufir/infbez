def gamma(istr,key):
    output = ""
    for i in range(0,len(istr)):
        output += chr(ord(istr[i]) ^ ord(key[i]))
    return output

text = "С Новым годом!"
key =  "ABCDEFGHIJKLMN"
cipher = gamma(text,key)
print(text)
print(key)
print(cipher)
print(" ")
print(gamma(cipher,key))
print(gamma(cipher,text))
