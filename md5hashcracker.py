import hashlib
import time

Hash = 'cd92817e63ec2784b09f9072537fa483'

f = open('passwordlist','r')
Data1 = f.read().splitlines()
passList=[]


for line in Data1:
    passList.append(line)

for word in passList:
    guess = hashlib.md5(word.encode('utf-8')).hexdigest()
    if guess.upper() == Hash or guess.lower() == Hash:
        print(f'Password found: {word}')
        exit(0)
    else:
        print(f'Guess: {word} incorrect... {guess}')
print(f'Password not found in wordlist...')
