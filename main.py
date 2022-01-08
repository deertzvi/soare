# -*- coding: utf-8 -*-
"""
load in the prerequisite info
"""
#%%
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#%%import the list of solutions
solutionsList = open("solutionList.txt","r")
solutions = solutionsList.read().split(', ')
solutionsList.close()
#%%import the herrings list
herringsList=open("herringList.txt","r")
herrings=herringsList.read().split(',')
herringsList.close()
#%%add the letters to test
commonLetters = [str(x) for x in input("Enter test letters, separated by commas: ").split(",")] 
#%%fix entries with spaces or caps
x=0
for item in commonLetters:  
   commonLetters[x]=item.strip(' ').lower()
   x=x+1
#%%find how many of the letters in each solution word match one of the defined common letters
commonCount={
} #create an empty dictionary to store the counts in
x=0
for x in solutions: #for every word in the solution list
  c=0 #start a counter at 0
  for y in range(5): #for every letter of the word
      currLetter=str(x[y])
      for z in commonLetters:
          testLetter=z
          if currLetter==z:
              c=c+1 #add one to the count of word letters matching a test letter 
          else:c=c    
  commonCount[x]=c #add the word (key) and the number of its letters which are also in the set (value) to the dictionary
#%%find the number of words with some number (n) or fewer of its letters matching letters in the test set
uncommonSolutions=[] #create an empty list for words that meet the criteria
minMatches=int(input("Enter the maximum number of characters (up to 5) in a possible \nsolution that can match a letter in the test set:\n"))
for key, value in commonCount.items():
    if value < minMatches:
        uncommonSolutions.append(key) #add that word to a new list
print('\nWords with fewer than',minMatches,'character(s) matching a test letter:\n',len(uncommonSolutions),' out of ',len(solutions),'\n')
wantList= input("Would you like to see the words? \nEnter 'yes' or 'no':\n").strip(' ').lower()
if wantList=='yes':
    print(*uncommonSolutions,sep=', ')
#%%     
##find the number of times each letter occurs in the uncommon word list
uncommonCount={
    }
for a in alphabet:#for each letter
  u=0 #start a new counter
  for x in uncommonSolutions:#for every word in the new list
    for y in range(5): #for every letter in the word
      if x[y]==a: #if it matches the current letter
          u=u+1 #increase the letter count by one
  uncommonCount[a]=u #add the letter (key) and number of instances in the new list (value) to a dictionary called uncommonCount
#%% sort uncommonCount by value, from highest to lowest 
uncommonFrequencies = sorted(uncommonCount.items(), key=lambda x: x[1], reverse=True)
#%%find the number of words in the uncommon word list containing each letter
uncommonAlpha={
    }
for a in alphabet:#for every letter
    w=0 #start a counter
    for x in uncommonSolutions: #for every word in the new list
        testWord=str(x)
        if testWord.find(a) != -1:#if the letter is in that word
            w=w+1 #increment the counter
    uncommonAlpha[a]=w #save the final count to uncommonAlpha
#%%sort word count
alphaFrequencies = sorted(uncommonAlpha.items(), key=lambda x: x[1], reverse=True)
#%%option to display frequency 
wantFreq= input("\nWould you like to see the most common letters in the new list? \nEnter 'yes' or 'no':\n").strip(' ').lower()
if wantFreq=='yes':
    print('\nTotal occurrences in new wordlist: \n')
    for i in uncommonFrequencies:
         print(i[0],':', i[1])
    print('\nUnique words containing each letter: \n')
    for i in alphaFrequencies:
         print(i[0],':', i[1])
wantAlph= input("\nWould you like these lists alphabetized?\nEnter 'yes' or 'no':\n").strip(' ').lower()
if wantAlph=='yes':
  print('\nTotal occurrences in new wordlist: \n')
  for key, value in uncommonCount.items():
    print(key,':',value)
  print('\nUnique words containing each letter: \n')
  for key, value in uncommonAlpha.items():
    print(key,':',value)
