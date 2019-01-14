# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:04:46 2019

@author: k.radheshyam.yadav
"""

##web scrping a website and getting th emost frequently appearing words form the book
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sb

#getting the data
def get_word_frequency(url):
    
    #url = 'https://www.gutenberg.org/files/2701/2701-h/2701-h.htm'
    data = requests.get(url)
    
    #lets check the type of data
    
    #print(type(data))
    # -> <class 'requests.models.Response'> it's a response object
    
    html = data.text
    # we'll use BeautifulSoup to wrangle the data
    
    #get a bs object
    
    soup = BeautifulSoup(html,'html5lib')
    #print(type(soup)) 
    
    #now you can get any tag from the html page(as a string also)
    
    #print(soup.title.string)
    
    #print(soup.findAll('a')[:8])
    
    #use the get_text() method to etxract the text from the html pages
    text = soup.get_text()
    #print(text)
    
    #Extract Words from your Text with NLP
    #pattern = r'\w+'
    #tokens = re.findall(pattern, text)
    #print(tokens[:8])
    
    # you can also do this with nltk
    
    #create tokenizer
    tokenizer  = RegexpTokenizer('\w+')
    
    #create tokens
    tokens = tokenizer.tokenize(text)
    #print(tokens[:8])
    
    #convert all the words to lower to neutralize uppercase and lowercase
    
    words = []
    
    for word in tokens:
        words.append(word.lower())
        
    print(words[:8])    
    
    # remove stop words
    
    sw = nltk.corpus.stopwords.words('english')
    #print(sw)
    
    #now you'll need a list with all the words excluding the stopwords
    
    word_ns = []
    
    for word in words:
        if word not in sw:
            word_ns.append(word)
            
    print(word_ns[:5])        
    #you can plot the freuency distribution to get the most frequently appearing word
    sb.set()
    
    freqdist1 = nltk.FreqDist(word_ns)
    freqdist1.plot(25)
    #print(freqdist1.max())
    #print(freqdist1.keys())
get_word_frequency('https://www.gutenberg.org/files/2701/2701-h/2701-h.htm')