import hashlib
import sys
import os

# Set colours for better visuals
red = "\033[91m"
green = "\033[92m"    

# Define banner
banner = """%s
   _  _                       _    
 _| || |_                    | |   
|_  __  _| ___ _ __ __ _  ___| | __
 _| || |_ / __| '__/ _` |/ __| |/ /
|_  __  _| (__| | | (_| | (__|   < 
  |_||_|  \___|_|  \__,_|\___|_|\_\\
                                                                       
""" % green

# Create a list of supported hash
supported_hashes = ["sha1", "sha224", "sha256", "sha384", "sha512", "md5"]

print(banner)
# Get hash type from user
hashtype = input("%sEnter your hash type: " % green)
hashtype = hashtype.casefold()

# Sanitize input and check if hashtype is supported
if hashtype.isspace():
    print("\n%s[-] Invalid input!" % red)
    sys.exit(1)

elif hashtype not in supported_hashes:
    print("\n%s[-] {} is not supported by this program".format(hashtype) % red)
    sys.exit(1)

# Get hash value and check if its a valid hash
hashvalue = input("%sEnter your hash: " % green)
hashvalue = hashvalue.casefold()

if hashtype=="md5" and len(hashvalue)!=32:
    print("\n%s[-] Invalid md5 hash" % red)
    sys.exit(1)

elif hashtype=="sha1" and len(hashvalue)!=40:
    print("\n%s[-] Invalid sha1 hash" % red)
    sys.exit(1)

elif hashtype=="sha224" and len(hashvalue)!=56:
    print("\n%s[-] Invalid sha224 hash" % red)
    sys.exit(1)

elif hashtype=="sha256" and len(hashvalue)!=64:
    print("\n%s[-] Invalid sha256 hash" % red)
    sys.exit(1)

elif hashtype=="sha384" and len(hashvalue)!=96:
    print("\n%s[-] Invalid sha384 hash" % red)
    sys.exit(1)

elif hashtype=="sha512" and len(hashvalue)!=128:
    print("\n%s[-] Invalid sha512 hash" % red)
    sys.exit(1)

# Get path to wordlist
wordlist = input("%s Provide path to wordlist: " % green)
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, wordlist)

try:

    print("\n%s[+] Trying to crack the hash..." % green)
    # Open words from wordlist
    for words in open(abs_file_path, "r", encoding="ISO-8859-1"):
        # Encode each word and compare them with given hash until match found
        if hashtype=="md5":
            currenthash=hashlib.md5(words.replace("\n", "").encode()).hexdigest()
            if currenthash==hashvalue:
                print("\n%s[+] Hash cracked: {}".format(words.replace("\n", "")) % green)
                sys.exit(0)

        elif hashtype=="sha1":
            currenthash=hashlib.sha1(words.replace("\n", "").encode()).hexdigest()
            if currenthash==hashvalue:
                print("\n%s[+] Hash cracked: {}".format(words.replace("\n", "")) % green)
                sys.exit(0)
        
        elif hashtype=="sha256":
            currenthash=hashlib.sha256(words.replace("\n", "").encode()).hexdigest()
            if currenthash==hashvalue:
                print("\n%s[+] Hash cracked: {}".format(words.replace("\n", "")) % green)
                sys.exit(0)
        
        elif hashtype=="sha384":
            currenthash=hashlib.sha384(words.replace("\n", "").encode()).hexdigest()
            if currenthash==hashvalue:
                print("\n%s[+] Hash cracked: {}".format(words.replace("\n", "")) % green)
                sys.exit(0)

        elif hashtype=="sha512":
            currenthash=hashlib.sha512(words.replace("\n", "").encode()).hexdigest()
            if currenthash==hashvalue:
                print("\n%s[+] Hash cracked: {}".format(words.replace("\n", "")) % green)
                sys.exit(0)
        
    # If match found print cracked hash else print wordlist exhausted and exit
    print("\n%s[-] Wordlist exhausted hash not found!" % red)
    sys.exit(1)

# Exception if path is undefined or incorrect 
except Exception as e:
    print("\n%s[-] {}".format(e) % red)
    sys.exit(1)
