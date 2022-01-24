from ast import operator
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:    
            #Increase
            worddict[word] +=1
        else:
            #add to the dictionary
            worddict[word] = 1
    sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

            
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddict':sortedword})

def about(request):
    return render(request, 'about.html')
