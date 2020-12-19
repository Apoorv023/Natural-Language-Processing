from nltk.corpus import wordnet as wn 	# Import wordnet from the NLTK
from textblob import TextBlob 			# For pos tagging
import matplotlib.pyplot as plt 		# For wordcloud as well
import spacy							# For entity recognition and relationship
from spacy import displacy				# For visualization of realationships among enities with the help of browser

# Opening book - 1 and reading its data in 'T1'
f1 = open('book1023.txt', 'r', encoding = 'utf-8')
T1 = f1.read()
# Opening book - 2 and reading its data in 'T2'
f2 = open('book2600.txt', 'r', encoding = 'utf-8')
T2 = f2.read()
# Converting the data in 't1' and 't2' to lower-case
t1 = T1.lower()
t2 = T2.lower()

# Identifying nouns and verbs from present in 't1'
noun1 = [w for (w, pos) in TextBlob(t1).pos_tags if pos[0] == 'N']
verb1 = [w for (w, pos) in TextBlob(t1).pos_tags if pos[0] == 'V']
# Identifying nouns and verbs from present in 't2'
noun2 = [w for (w, pos) in TextBlob(t2).pos_tags if pos[0] == 'N']
verb2 = [w for (w, pos) in TextBlob(t2).pos_tags if pos[0] == 'V']

# Creating an empty list that will contain the category of the noun for each word present in the list 'noun1' 
noun_wordnet1 = []

# Finding the category of noun for each word present in the list 'noun1'
for x in range(len(noun1)):
	col = []
	for synset in wn.synsets(noun1[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		noun_wordnet1.append(col[0])
	else:
		noun_wordnet1.append("noun.person")

# Creating an empty list that will contain the category of the verb for each word present in the list 'verb1' 
verb_wordnet1 = []

# Finding the category of verb for each word present in the list 'verb1'
for x in range(len(verb1)):
	col = []
	for synset in wn.synsets(verb1[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		verb_wordnet1.append(col[0])
	else:
		verb_wordnet1.append("Category not found")
print(verb_wordnet1)
# Creating an empty list that will contain the category of the noun for each word present in the list 'noun2' 
noun_wordnet2 = []

# Finding the category of noun for each word present in the list 'noun2'
for x in range(len(noun2)):
	col = []
	for synset in wn.synsets(noun2[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		noun_wordnet2.append(col[0])
	else:
		noun_wordnet2.append("noun.person")

# Creating an empty list that will contain the category of the verb for each word present in the list 'verb2' 
verb_wordnet2 = []

# Finding the category of verb for each word present in the list 'verb2'
for x in range(len(verb2)):
	col = []
	for synset in wn.synsets(verb2[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		verb_wordnet2.append(col[0])
	else:
		verb_wordnet2.append("Category not found")

# Loading the trainer for entity recognition and relationship
sp = spacy.load('en_core_web_sm')

# Splitting the data 'T1' paragraph-wise for entity recognition and put the splitted data in list 'data1'
data1 = T1.split("\n\n")
lg1 = len(data1)
# Iterating over every paragraph present in the list 'data1' for entity recognition
print("\t\t\t\t\tEntity recognition for BOOK-1:")
for i in range(lg1):
	doc = sp(data1[i])
	print("\n\tParagraph No. -", i+1)
	for ent in doc.ents:
		print(ent.text + ' - ' + ent.label_)

# Splitting the data 'T2' paragraph-wise for entity recognition and put the splitted data in the list 'data2'
data2 = T2.split("\n\n")
lg2 = len(data2)
# Iterating over every paragraph present in the list 'data2' for entity recognition
print("\n\t\t\t\t\tEntity recognition for BOOK-2:")
for i in range(lg2):
	doc = sp(data2[i])
	print("\n\tParagraph No. -", i+1)
	for ent in doc.ents:
		print(ent.text + ' - ' + ent.label_)

# Recognizing relationships among various entities present in book-1 sentence-wise for each paragraph using 'data1'
print("\n\t\t\t\t\tEntity Relationship for BOOK-1:")
for i in range(lg1):
	dt1 = data1[i].split('.')												# Splitting the paragraph present in 'data1' to create a list(dt1) of sentences
	for j in range(len(dt1)):
		piano_doc = sp(dt1[j])
		print("\n\tParagraph No. -", i+1, ", sentence no. -", j+1)
		for token in piano_doc:
			print (token.text, token.tag_, token.head.text, token.dep_)		# Finding relationship among entities present in a sentence

# Recognizing relationships among various entities present in book-2 sentence-wise for each paragraph using 'data2'
print("\n\t\t\t\t\tEntity Relationship for BOOK-2:")
for i in range(lg2):
	dt2 = data2[i].split('.')												# Splitting the paragraph present in 'data2' to create a list(dt2) of sentences
	for j in range(len(dt2)):
		piano_doc = sp(dt2[j])
		print("\n\tParagraph No. -", i+1, ", sentence no. -", j+1)
		for token in piano_doc:
			print (token.text, token.tag_, token.head.text, token.dep_)		# Finding relationship among entities present in a sentence