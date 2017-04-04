#!/usr/intel/bin/python3.3.1
# -*- coding: utf-8 -*-
import json

class Language:
	#This method, convert from x alphabet to y alphabet, given an text input with json, it will convert the input text to according to the json -dictionary- given in the second arugment
    def replaceToNewLanguage(self,text, json):
        output = ""
        currentLetter = ""
        for t in text:
            currentLetter += t
            if currentLetter in json:
                output += json[currentLetter]
                currentLetter = ""
        return output
		
	#This method will calculate how many different words there is in any text string given 
    def count_words_fast(self,text):
        text = text.lower()
        skips = [".",",",";",":","'",'"']
        for ch in skips:
            text = text.replace(ch,"")
		
        word_counts = {}
        for word in text.split(" "):
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return word_counts

	#this will convert from language to another, almost as same as replaceToNewLanguage but with different uses as shown in the examples below
    def replace_language(self,text,json):
        for fLetter, sLetter in json.items():
            text = text.replace(fLetter,sLetter)
        return text

	#will count how many times the word exists in text.
    def count_word(self,text,word):
        counter = 0
        for word2 in text.split(" "):
            if word2 == word:
                counter +=1
        return counter


lang = Language()

##################################
dnaFilePath = "dna/json"
inputFilePath = "dna/input"
with open(dnaFilePath) as data_file:    
        jsonFile = json.load(data_file)
	
with open(inputFilePath) as data_file:    
        dataText = data_file.read()

print(lang.replaceToNewLanguage(dataText,jsonFile))
##################################
articleFilePath = "article/input"
with open(articleFilePath) as data_file:    
        articleString = data_file.read()

print(lang.count_words_fast(articleString))
##################################
dnaFilePath = "language/json"
inputFilePath = "language/input"
with open(dnaFilePath) as data_file:    
        jsonFile = json.load(data_file)
	
with open(inputFilePath) as data_file:    
        dataText = data_file.read()
print(lang.replace_language(dataText,jsonFile))
##################################
print(lang.count_word("hi , this is an example input, I will be calculating how many hi exists in this string.","hi"))
