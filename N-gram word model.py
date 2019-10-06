# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 23:10:36 2018

@author: Dell
"""
import nltk
import random
text="""If I burden myself with a little help mate during my adventures it is not out of sentiment or caprice, it is that he has many fine qualities of his own that he has overlooked in his obsession with me. Indeed any reputation I have for mental acuity and sharpness comes in truth from the extraordinary contrast John so selflessly provides. It is a fact I believe brides tend to favor exceptionally plain bridesmaids for their big day. There is a certain analogy there I feel. And contrast is, after all, God's own plan to enhance the beauty of his creation. Or it would be if God were not a ludicrous fantasy designed to provide a career opportunity for the family idiot."""

n=2
ngrams={}

words=nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram=' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram]=[]
    ngrams[gram].append(words[i+n])

#testing it out
currentGram=' '.join(words[0:n])
result=currentGram
for i in range(700):
    if currentGram not in ngrams.keys():
        break
    possib=ngrams[currentGram]
    nextItem=possib[random.randrange(len(possib))]
    result+=' '+nextItem
    rwords=nltk.word_tokenize(result)
    currentGram=' '.join(rwords[len(rwords)-n:len(rwords)])
    
print(result)
    
    