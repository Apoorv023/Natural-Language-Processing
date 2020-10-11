import re
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
import csv
import nltk
from collections import Counter

# Opening book - 01 (http://www.gutenberg.org/ebooks/2600)
B1 = open('book2600.txt', 'r', encoding = 'utf-8')
t1 = B1.read()

# Opening book - 02 (http://www.gutenberg.org/ebooks/1023)
B2 = open('book1023.txt', 'r', encoding = 'utf-8')
t2 = B2.read()

# Tokenizing first book, i.e., B1 without removing the stopwords
t1 = t1.lower() 				# Converting all the letters to lower case
t1 = re.sub("[^\w]", ' ',t1) 	# Replacing all the special characters with a space
T1 = t1.split() 				# Converting t1 from string datatype to a list of words and storing it in T1

# Tokenizing second book, i.e., B2 without removing the stopwords
t2 = t2.lower() 			 	# Converting all the letters to lower case
t2 = re.sub("[^\w]", ' ',t2) 	# Replacing all the special characters with a space
T2 = t2.split() 				# Converting t2 from string datatype to a list of words and storing it in T2

# Converting the list T1 into DataFrame df1 with each word's count associated with itself
df1 = pd.DataFrame( {'Token':T1})
df1 = pd.crosstab( index = df1['Token'], columns = 'count')
df1 = df1.sort_values( by = 'count')	# Sorting dataframe in ascending order based on the count of each word
print("\nDataFrame df1 for book - 1 before removing stopwords")
df1.to_csv('B1_Tokens.csv')				# Storing the dataframe df1 in a CSV file called B1_Tokens.csv
print(df1)

# Creating word cloud for first book B1 without removing stopwords
print("\nGenerating WordCloud for T1...")
wordcloud=WordCloud(width=1000,height=1000,background_color="white").generate(t1)		# Generating WordCloud for book B1
plt.figure(figsize=(40,40))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

# Converting the list T2 into DataFrame df2 with each word's count associated with itself
df2 = pd.DataFrame( {'Token':T2})
df2 = pd.crosstab( index = df2['Token'], columns = 'count')
df2 = df2.sort_values( by = 'count')			# Sorting dataframe in ascending order based on the count of each word
print("\nDataFrame df2 for book - 2 before removing stopwords")
df2.to_csv('B2_Tokens.csv')						# Storing the dataframe df2 in a CSV file called B2_Tokens.csv
print(df2)

# Creating word cloud for second book B2 without removing stopwords
print("\nGenerating WordCloud for T2...")
wordcloud=WordCloud(width=1000,height=1000,background_color="white").generate(t2)		# Generating WordCloud for book B2
plt.figure(figsize=(40,40))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

# List of all the considered stopwords in English language
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", 
			 "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 
			 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 
			 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
			 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 
			 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 
			 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
			 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 
			 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 
			 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 
			 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 
			 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
			 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 
			 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 
			 'didn',"didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', 
			 "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', 
			 "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', 
			 "weren't", 'won', "won't", 'wouldn', "wouldn't"]

T11 = [ word for word in T1 if not word in stopwords]		# Removing all the stopwords from the list of words(T1) present in book B1
T21 = [ word for word in T2 if not word in stopwords]		# Removing all the stopwords from the list of words(T2) present in book B2

# Converting the list T11 into DataFrame df11 with each word's count associated with itself
df11 = pd.DataFrame( {'Token':T11})
df11 = pd.crosstab( index = df11['Token'], columns = 'count')
df11 = df11.sort_values( by = 'count')						# Sorting dataframe in ascending order based on the count of each word
print("\nDataFrame df11 for book - 1 after removing stopwords")
df11.to_csv('B1_Stopwords_Tokens.csv')						# Storing the dataframe df11 in a CSV file called B1_Stopwords_Tokens.csv
print(df11)

# Creating word cloud for first book B1 after removing stopwords
print("\nGenerating WordCloud for T11...")
t11 = ' '.join(T11)				# Converting the list of words of book B1 not containing stopwords to string for generating WordCloud without stopwords
wordcloud=WordCloud(width=1000,height=1000,background_color="white").generate(t11)		# Generating WordCloud for T11
plt.figure(figsize=(40,40))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

# Converting the list T21 into DataFrame df21 with each word's count associated with itself
df21 = pd.DataFrame( {'Token':T21})
df21 = pd.crosstab( index = df21['Token'], columns = 'count')
df21 = df21.sort_values( by = 'count')							# Sorting dataframe in ascending order based on the count of each word
print("\nDataFrame df21 for book - 2 after removing stopwords")
df21.to_csv('B2_Stopwords_Tokens.csv')							# Storing the dataframe df21 in a CSV file called B1_Stopwords_Tokens.csv
print(df21)

# Creating word cloud for second book B2 after removing stopwords
print("\nGenerating WordCloud for T21...")
t21 = ' '.join(T21)				# Converting the list of words of book B1 not containing stopwords to string for generating WordCloud without stopwords
wordcloud=WordCloud(width=1000,height=1000,background_color="white").generate(t21)		# Generating WordCloud for T21
plt.figure(figsize=(40,40))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()

# Plotting a histogram between word length and frequency, for book B1 before removing stopwords
frqlist1 = [0] * 50 											# Creating a list where index shows the length of different words in book B1 and initialisation with '0' shows that initially occurrence of words of each length is zero 
for row in df1.index:											# Iterating the rows of dataFrame df1
	ind = len(row)												# Getting the length of word from dataFrame df1's first column containing all the different words occurring in book B1
	frqlist1[ind] = frqlist1[ind] + df1.at[ row,'count'] 		# Updating the values in frqlist1 according to occurrence of the word(present in second column of df1) with respect to it's length

print("\nPlotting histogram for Book1...")
plt.hist(frqlist1, bins = 50)									# Plotting the histogram of frqlist1
plt.xlabel("Number of occurrences in Book1") 
plt.ylabel("Length of word")
plt.show()
print(frqlist1)

# Plotting a histogram between word length and frequency, for book B2 before removing stopwords
frqlist2 = [0] * 50 											# Creating a list where index shows the length of different words in book B2 and initialisation with '0' shows that initially occurrence of word of each length is zero
for row in df2.index:											# Iterating the rows of dataFrame df2
	ind = len(row)												# Getting the length of word from dataFrame df2's first column containing all the different words occurring in book B2
	frqlist2[ind] = frqlist2[ind] + df2.at[ row,'count'] 		# Updating the values in frqlist2 according to occurrence of the word(present in second column of df2) with respect to it's length

print("\nPlotting histogram for Book2...")
plt.hist(frqlist2, bins = 50)									# Plotting the histogram of frqlist2
plt.xlabel("Number of occurrences in Book2") 
plt.ylabel("Length of word")
plt.show()
print(frqlist2)

# Plotting a histogram between word length and frequency, for book B1 after removing stopwords
frqlist11 = [0] * 50 											# Creating a list where index shows the length of different words in book B1 and initialisation with '0' shows that initially occurrence of words of each length is zero 
for row in df11.index:											# Iterating the rows of dataFrame df11
	ind = len(row)												# Getting the length of word from dataFrame df11's first column containing all the different words occurring in book B1
	frqlist11[ind] = frqlist11[ind] + df11.at[ row,'count'] 	# Updating the values in frqlist11 according to occurrence of the word(present in second column of df11) with respect to it's length

print("\nPlotting histogram for Book1 after removing stopwords...")
plt.hist(frqlist11, bins = 50)									# Plotting the histogram of frqlist11
plt.xlabel("Number of occurrences in Book1 after removing stopwords") 
plt.ylabel("Length of word")
plt.show()
print(frqlist11)

# Plotting a histogram between word length and frequency, for book B2 after removing stopwords
frqlist21 = [0] * 50 											# Creating a list where index shows the length of different words in book B2 and initialisation with '0' shows that initially occurrence of word of each length is zero
for row in df21.index:											# Iterating the rows of dataFrame df21
	ind = len(row)												# Getting the length of word from dataFrame df21's first column containing all the different words occurring in book B2
	frqlist21[ind] = frqlist21[ind] + df21.at[ row,'count'] 	# Updating the values in frqlist21 according to occurrence of the word(present in second column of df21) with respect to it's length

print("\nPlotting histogram for Book2 after removing stopwords...")
plt.hist(frqlist21, bins = 50)									# Plotting the histogram of frqlist21
plt.xlabel("Number of occurrences in Book2 after removing stopwords") 
plt.ylabel("Length of word")
plt.show()
print(frqlist21)

# PoS Tagging for book B1
T_temp1 = TextBlob(t1)
T_tags1 = T_temp1.tags 											# Giving tag to every word in Book B1 and storing it in a list named T_tags1
df3 = pd.DataFrame(T_tags1, columns = ['Token', 'Tag'])			# Creating a DataFrame df3 from list T_tags1 with columns as 'Token' and 'Tag'
df3 = df3.groupby(df3.columns.tolist(),as_index=False).size()	# Grouping all the rows having same token and tag to get their respective count
print("\nDataFrame df3 containing tags for book1\n", df3)
df3.to_csv('B1_Tags.csv', header = False, index = False)		# Storing the dataframe df3 in a CSV file called B1_Tags.csv

# PoS Tagging for book B2
T_temp2 = TextBlob(t2)
T_tags2 = T_temp2.tags 											# Giving tag to each word in Book B2 and storing it in a list named T_tags2
df4 = pd.DataFrame(T_tags2, columns = ['Token', 'Tag'])			# Creating a DataFrame df4 from list T_tags2 with columns as 'Token' and 'Tag'
df4 = df4.groupby(df4.columns.tolist(),as_index=False).size()	# Grouping all the rows having same token and tag to get their respective count
print("\nDataFrame df4 containing tags for book2\n", df4)
df4.to_csv('B2_Tags.csv', header = False, index = False)		# Storing the dataframe df4 in a CSV file called B2_Tags.csv

# Bi-gram matrix for tokens in book B1
my_list = list(nltk.bigrams(T1))

frequency_list = Counter( tuple( sorted( i)) for i in my_list)
words=sorted( list( set( [ item for t in my_list for item in t])))
df5 = pd.DataFrame( 0, columns=words, index=words)
for k,v in frequency_list.items():
  df5.at[ k[0], k[1]] = v
  
print(df5)
# df5.to_csv('B1_Bigram_Matrix.csv')     			Stores the dataframe df5 in a CSV file called B1_Bigram_Matrix.csv of size 600MB

# Bi-gram matrix for tokens in book B2
my_list = list(nltk.bigrams(T2))

frequency_list = Counter( tuple( sorted( i)) for i in my_list)
words=sorted( list( set( [ item for t in my_list for item in t])))
df6 = pd.DataFrame( 0, columns=words, index=words)
for k,v in frequency_list.items():
  df6.at[ k[0], k[1]] = v

print(df6)  
# df6.to_csv('B2_Bigram_Matrix.csv')     			Stores the dataframe df6 in a CSV file called B2_Bigram_Matrix.csv of size 433MB

# The above code generates a bi-gram matrix df5 and df6 for both books B1 and B2 having dimension as following:	df5 -> 17527x17527
# df6 -> 14888x14888. Such large matrices generate a very large CSV file of sizes 600MB and 433MB, which cannot be shared
# with the report. But, screenshots of the same are attached with the report to get a bit of sense of the output.
