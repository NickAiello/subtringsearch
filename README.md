# subtringsearch
Great word list: https://github.com/dwyl/english-words

Download: https://github.com/dwyl/english-words/blob/master/words.zip

# Problem
* Given a dictionary of words and a string of letters, find all matching substrings of the given letters
* Words matched may be shorter than or equal to the amount of letters.
* Given letter counts matter, so given letters "ehlo", the word "hello" would NOT match as it requires a second "l"
* Must accept comma, dash, single and double quotes, numbers

# My Solution
* Sort all letters of each word in the dictionary alphabetically such that the word "hello" becomes "ehllo"
** Dictionary words may be presorted and saved to reduce future run times
* Sort the given letters alphabetically
* create a regex string from the given letter in the form: /^arr[0]?arr[1]?arr[k]?$/
** k = number of given letters
** arr = array of the given letters in alphabetically order
** This regex anchors to the start of a string and makes all given characters optional
** Since all strings tested are pre sorted alphabetically, ordering may be enforced in the regex without losing matches
** bind to the end for a length limit
* Match against all words in the dictionary and return a list of matches
