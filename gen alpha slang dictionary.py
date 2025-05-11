None
name = input ("what is your name")
print("hello,this is a gen alpha slang dictionary.")
meme_dict = {"Skibidi toilet": "a persons head sticking out of a toilet",
             "Aura": "a person's overall vibe, energy, or how cool they are perceived to be", "Sigma":"something is cool, awesome, or the best","Rizz":"short for charisma and refers to someone's ability to attract or charm others, especially in a flirtatious way"}
word = input("type in the word that you dont understand")
if word in meme_dict.keys():
    print (meme_dict [word])
else:
    print ("word not found")
    
