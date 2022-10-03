import string
import matplotlib.pyplot as plt

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    s=''
    with open(filename, 'r', encoding='utf-8') as f:
        while True:                                # Read till end of file
            c = f.read(1)                          # Read one character at a time
            if c:
                if ord(c)>=97 and ord(c)<=122:     # Unicode for letters a-z
                    s=s+c
                elif ord(c)>=65 and ord(c)<=90:    # Unicode for letters A-Z
                    s=s+chr(ord(c)+32)
            else:
                break
    return s

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d = {}
    for c in s:
        if c in d.keys():
            d[c]+=1
        else:
            d[c] = 1
    return d

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    new_s = ''
    for char in s:
        if char in d:
            new_s+=d[char]
    return new_s

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    d = {val:key for key,val in d.items()}            # Reverse the dictionary used for encryption
    new_s = ''
    for char in s:
        if char in d:
            new_s+=d[char]
    return new_s

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    dist = letter_distribution(s)
    max_letter = max(dist, key=lambda x:dist[x])    # Find the letter with the highest frequency in ciphertext
    key = ord(max_letter) - ord('e')                # 'e' is the most common letter in text (From plaintext letter distribution)
                                                    # Thus, we can find the difference between highest occuring letter in ciphertext
                                                    #  and 'e' to get the Caesar Cipher key.
    pred_decrypt = ''
    for char in s:
        pred_decrypt+= chr((ord(char)-97-key+26)%26 + 97)   # Calculate the unicode for each letter
    return pred_decrypt

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    len_pass = len(password)
    vig_enc = ''
    i=0
    for char in s:
        vig_enc+= chr(97+(ord(char) -97 + ord(password[i]) -97)%26)     
        i=(i+1)%len_pass    # Keep repeating the letters of the password
                            # till plaintext is exhausted.
    return vig_enc

def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    len_pass = len(password)
    vig_dec = ''
    i=0
    for char in s:
        vig_dec+= chr(97+(ord(char) - ord(password[i])+26)%26)  # Same logic as above but now we subtract instead of add.
        i=(i+1)%len_pass
    return vig_dec

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    rotated = s[-r:]+s[:-r]               # Rotate the string by r
    collisions = 0
    for c1,c2 in list(zip(s,rotated)):
        if c1==c2:                        # Count collision if characters match
            collisions+=1                

    return collisions/len(s)

def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    sub_s = ['']*k
    for i in range(len(s)):
        sub_s[i%k]+=s[i]

    final_decrypted = []
    for caesar in sub_s:                                            # Extract all sub ciphers encrypted using the same letter.
        final_decrypted.append(cryptanalyse_substitution(caesar))   # Assumption here is that for a long enough cipher
                                                                    # the frequency distribution remains the same. So each
                                                                    # sub cipher extracted can be decrypted using substitution.
    
    max_len = len(max(final_decrypted, key=lambda x:len(x)))
    vig_dec_fin = ''
    for i in range(max_len):                                        # Re join all sub ciphers
        for j in final_decrypted:
            if i < len(j):
                vig_dec_fin+=j[i]

    return vig_dec_fin

def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    X = list(range(1,100))
    y = [rotate_compare(s,1)]
    first_flag = True
    y_prev = y[-1]
    key_length = -1
    for i in range(2,100):
        y.append(rotate_compare(s,i))
        if y_prev == 0.0:                  # If y of previous is zero, then take the difference because product will always be 0. 
            if y[-1] - y_prev > 0.04 and first_flag:
                first_flag = False
                key_length = i
        else:                              # If y of current is more than 1.5 times(rough observation) the previous,
                                           # then this is the key length.
            if y[-1] > y_prev*1.5 and first_flag:
                first_flag = False
                key_length = i
        y_prev = y[-1]
    plt.bar(X, y)                         # The plot shows that the collision proportion spikes at 
    plt.show()
    return key_length

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    key_length = cryptanalyse_vigenere_findlength(s)            # Use cryptanalyse_vigenere_findlength() to get the length
    vig_dec = cryptanalyse_vigenere_afterlength(s, key_length)  # Use cryptanalyse_vigenere_afterlength() to decrypt
    return vig_dec


# String functions
s='plaksha'
print(s.find('p'))
print(s.replace('pl','r'))

#1
s = textstrip('sherlock.txt')
print("Lowercase:", s)

#2
dist = letter_distribution(s) 
print("Distribution:", dist)

#3
n = 8
d = {chr(i):chr(97+((i-97+n)%26)) for i in range(97,123)}
sub_encrypted = substitution_encrypt(s,d)
print("Substitution Encrypted:", sub_encrypted)

#4
sub_decrypted = substitution_decrypt(sub_encrypted, d)
print("Substitution Decrypted:", sub_decrypted)

#5
sub_decrypted_no_key = cryptanalyse_substitution(sub_encrypted)
print("Decrypted No Key:", sub_decrypted_no_key)

#6
password = 'russia'
vigenere_encrypted = vigenere_encrypt(s, password)
print("Vigenere Encrypted:", vigenere_encrypted)

#7
vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, password)
print("Vigenere Decrypted:", vigenere_decrypted)

#8
collision_proportion = rotate_compare(vigenere_encrypted, 1)
print("Collision Proportion for 1 rotation:", collision_proportion)

#9
vig_decrypt_len = cryptanalyse_vigenere_afterlength(vigenere_encrypted, len(password))
print("Vigenere Cryptanalyze With Length:", vig_decrypt_len)

#10
key_length = cryptanalyse_vigenere_findlength(vigenere_encrypted)
print("Key Length:", key_length)

#11
vig_decrypt_no_key = cryptanalyse_vigenere(vigenere_encrypted)
print("Vigenere Decrypted No Key:", vig_decrypt_no_key)
