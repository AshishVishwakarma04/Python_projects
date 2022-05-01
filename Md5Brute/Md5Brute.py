from base64 import encode
import hashlib

def openfile(wordlist):
    try:
        file = open(wordlist, "r")
        return file
    except:
        print("[-] File not found")
        quit()
        
passwordhash = input("[+] Enter your MD5 Hash value :  ")      
wordlist = input("[+] Enter location of your wordlist : ")
file = openfile(wordlist)


for word in file:
    print("[+] Trying: " + word.strip('\n'))
    encodeword  = word.encode('UTF-8')
    md5hash = hashlib.md5(encode.strip()).hexdigest()
    
    if md5hash == encodeword:
      print("[+] Password found !" + word)
    else:
       pass
print("[+] Password not in list !")   
           