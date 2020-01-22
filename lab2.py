# receives message from user

msg = input("Type in your message here! ")
print (msg)

# changes all characters to uppercase letters

code = str.upper(msg)

# changes one letter to its secret value

num_code = ord(code) + 1

chr_code = chr(num_code)

print (letter, chr_code)

# solves "Z" problem

num_code = ord(code)
if num_code >= 90:
    num_code = num_code - 26
    print (num_code)

num_code = num_code + 1

chr_code = chr(num_code)

print (chr_code)

#encodes entire message

for char in num_code:
    print (char)
    print (ord(char))

    numcode = ord(char) + 1
    print (numcode)
    
    print (chr(numcode))

