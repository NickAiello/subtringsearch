import re
import sys

#Run against a dicitonary where the words are not presorted
def unsorted_dictionary_match(s,d):
    #generate the regex search string, anchor to start
    regex = "^"
    #add each letter sorted as optional
    for i in sorted(s):
        regex += i + "?"
    #anchor to end of string
    regex += "$"
    matches = []
    for i in d:
        #sort each word into letters alphabetically and regex match sorted word
        if (re.match(regex,''.join(sorted(i)))):
            matches.append(i)
    return (matches)

#run against a dictionary where the words are presorted
def sorted_dictionary_match(s,d):
    #generate the regex search string, anchor to start
    regex = "^"
    #add each letter sorted as optional
    for i in sorted(s):
        regex += i + "?"
    #anchor to end of string
    regex += "$"
    matches = []
    for i in d:
        #regex match presorted word
        if (re.match(regex,i)):
            matches.append(i)
    return (matches)

#Need one arg
if (len(sys.argv) != 2):
    print ("Needs one arg set of letters")
    sys.exit(1)

#read dictionary file
#reads whole file at once, very memory intensive, could easily be read and matched at same time
with open("words.txt") as f:
    d = f.read().splitlines()
f.close()

#run substring search
matches = unsorted_dictionary_match(sys.argv[1],d)
print (matches)