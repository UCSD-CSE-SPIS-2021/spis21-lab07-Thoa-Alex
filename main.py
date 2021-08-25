
def train (s):

    words = s.split ()
    
    # Creates a dictionary for the next words
    nextwords = dict()

    # For words in the sentence
    for i in range (len(words)):
        
        # First word has no previous word, proceed
        if i == 0:
            continue
        
        # if there is a word before that count that as i - 1
        else:
            previous = words [i-1]
            
        if previous not in nextwords:

            # If there is not a dictionary entry for the previous word make an empty list
            nextwords[previous] = []

            # Appends the current word to the list of the previous word
        nextwords[previous].append(words [i])

    return nextwords

    #Loop through the unique words, for every word, find all the possible words that came before it, each word has a dictionary entry and the entry is all the words that came after it
    
cardi_B = train ("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")

print (cardi_B)
# The function train (s) introduces s.split which splits the text that we provide. The following line of code creates an empty dictionary for us to store each unique word. The loop goes through each word of the text. Since the beginning of the text has no previous word, we continue to the next word. Since Baby has a previous word, the else statement in the loop allows us to take the previous word of Baby, which is Yeah. The if statement following that else statement then makes Yeah an entry into the dictionary and creates a list. And so finally, the line of code before the return statement appends baby into the Yeah list into the dictionary. Return nextwords (?) --> Point is the next iteration will go to "I" and repeat the process. 

def generate(model, first_word, num_words):
    import random
    sentence = first_word + " "
    keyword = first_word
    
    for i in range (num_words -1 ) :
        
        nextone = random.choice(model [keyword])
        sentence += (nextone + " ")
        keyword = nextone
    print(sentence)
generate (cardi_B, "I", 15)