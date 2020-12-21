from nltk.corpus import wordnet as wn 		# For finding the categories of nouns and verbs 
from textblob import TextBlob 			# For pos tagging to find nouns and verbs from the data
import matplotlib.pyplot as plt 		# For plotting frequency histograms
import spacy					# For entity recognition and relationship

# Opening book - 1 and reading its data in 'T1'
f1 = open('book1023.txt', 'r', encoding = 'utf-8')
T1 = f1.read()
# Opening book - 2 and reading its data in 'T2'
f2 = open('book2600.txt', 'r', encoding = 'utf-8')
T2 = f2.read()
# Converting the data in 't1' and 't2' to lower-case
t1 = T1.lower()
t2 = T2.lower()

# Identifying nouns and verbs from present in 't1', i.e., Book-1
noun1 = [w for (w, pos) in TextBlob(t1).pos_tags if pos[0] == 'N']
verb1 = [w for (w, pos) in TextBlob(t1).pos_tags if pos[0] == 'V']
# Identifying nouns and verbs from present in 't2', i.e., Book-2
noun2 = [w for (w, pos) in TextBlob(t2).pos_tags if pos[0] == 'N']
verb2 = [w for (w, pos) in TextBlob(t2).pos_tags if pos[0] == 'V']

# Creating an empty list that will contain the category of the noun for each word present in the list 'noun1' 
noun_wordnet1 = []
# Finding the category of noun for each word present in the list 'noun1' and appending it in the list 'noun_wordnet1'
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
# Finding the category of verb for each word present in the list 'verb1' and appending it in the list 'verb_wordnet1'
for x in range(len(verb1)):
	col = []
	for synset in wn.synsets(verb1[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		verb_wordnet1.append(col[0])
	else:
		verb_wordnet1.append("verb.stative")

# Creating an empty list that will contain the category of the noun for each word present in the list 'noun2' 
noun_wordnet2 = []
# Finding the category of noun for each word present in the list 'noun2' and appending it in the list 'noun_wordnet2'
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
# Finding the category of verb for each word present in the list 'verb2' and appending it in the list 'verb_wordnet2'
for x in range(len(verb2)):
	col = []
	for synset in wn.synsets(verb2[x]):
		col.append(synset.lexname())
	if len(col) != 0:
		verb_wordnet2.append(col[0])
	else:
		verb_wordnet2.append("verb.stative")

# Function for counting the frequency of a various categories of verb and noun
def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

# Histogram for categories of noun present in list 'noun1'
counted_noun1 = count_elements(noun_wordnet1)
plt.bar(counted_noun1.keys(), counted_noun1.values(), 0.7, color = 'g')
plt.xlabel("Categories of noun")
plt.xticks(rotation = 90)
plt.ylabel("Frequency for book-1")
plt.show()
print("Total number of categories of noun:", len(counted_noun1))
print("Count for different noun categories in book-1:\n", counted_noun1, "\n")

# Histogram for categories of verb present in list 'verb1'
counted_verb1 = count_elements(verb_wordnet1)
plt.bar(counted_verb1.keys(), counted_verb1.values(), 0.7, color = 'g')
plt.xlabel("Categories of verb")
plt.xticks(rotation = 90)
plt.ylabel("Frequency for book-1")
plt.show()
print("Total number of categories of verb:", len(counted_verb1))
print("Count for different verb categories in book-1:\n", counted_verb1, "\n")

# Histogram for categories of noun present in list 'noun2'
counted_noun2 = count_elements(noun_wordnet2)
plt.bar(counted_noun2.keys(), counted_noun2.values(), 0.7, color = 'g')
plt.xlabel("Categories of noun")
plt.xticks(rotation = 90)
plt.ylabel("Frequency for book-2")
plt.show()
print("Total number of categories of noun:", len(counted_noun2))
print("Count for different noun categories in book-2:\n", counted_noun2, "\n")

# Histogram for categories of verb present in list 'verb2'
counted_verb2 = count_elements(verb_wordnet2)
plt.bar(counted_verb2.keys(), counted_verb2.values(), 0.7, color = 'g')
plt.xlabel("Categories of verb")
plt.xticks(rotation = 90)
plt.ylabel("Frequency for book-2")
plt.show()
print("Total number of categories of verb:", len(counted_verb2))
print("Count for different verb categories in book-2:\n", counted_verb2, "\n")



# Loading the trainer for entity recognition and relationship
sp = spacy.load('en_core_web_sm')

# Splitting the data 'T1' paragraph-wise for entity recognition and putting the splitted data in the list 'data1'
data1 = T1.split("\n\n")
lg1 = len(data1)
# Iterating over every paragraph present in the list 'data1' for entity recognition
print("\t\t\t\t\tEntity recognition for BOOK-1:")
for i in range(lg1):
	doc = sp(data1[i])
	print("\n\tParagraph No. -", i+1)
	for ent in doc.ents:
		print(ent.text + ' - ' + ent.label_)

# Splitting the data 'T2' paragraph-wise for entity recognition and putting the splitted data in the list 'data2'
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
	dt1 = data1[i].split('.')												# Splitting the paragraph present in 'data1' to create a list(dt1) of sentences for entity relationships
	for j in range(len(dt1)):
		piano_doc = sp(dt1[j])
		print("\n\tParagraph No. -", i+1, ", sentence no. -", j+1)
		for token in piano_doc:
			print (token.text, token.tag_, token.head.text, token.dep_)						# Finding and printing relationship among entities present in a sentence

# Recognizing relationships among various entities present in book-2 sentence-wise for each paragraph using 'data2'
print("\n\t\t\t\t\tEntity Relationship for BOOK-2:")
for i in range(lg2):
	dt2 = data2[i].split('.')												# Splitting the paragraph present in 'data2' to create a list(dt2) of sentences for entity relationships
	for j in range(len(dt2)):
		piano_doc = sp(dt2[j])
		print("\n\tParagraph No. -", i+1, ", sentence no. -", j+1)
		for token in piano_doc:
			print (token.text, token.tag_, token.head.text, token.dep_)						# Finding and printing relationship among entities present in a sentence
