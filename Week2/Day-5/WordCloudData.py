import re

class WordCloudData(object):

	def __init__(self, in):

		# Count the frequency of each word
		lis = re.split('\.| |\?|\!|:|\- |, |\(|\)',in)
		dic = {}
		for i in lis:
			if i!='':
				j = i.title()
				if i in dic:
					dic[i] += 1
				elif j in dic:
					dic[i] = 1+dic[j]
					dic.pop(j, None)
				else:
					dic[i] = 1
		self.words_to_counts = dic

# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

input = 'I like cake'
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {'I': 1, 'like': 1, 'cake': 1}
print(actual == expected)

input = 'Chocolate cake for dinner and pound cake for dessert'
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {'and': 1,'pound': 1,'for': 2,'dessert': 1,'Chocolate': 1,'dinner': 1,'cake': 2,}
print(actual == expected)

input = 'Strawberry short cake? Yum!'
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
print(actual == expected)

input = 'Dessert - mille-feuille cake'
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
print(actual == expected)

input = 'Mmm...mmm...decisions...decisions'
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {'mmm': 2, 'decisions': 2}
print(actual == expected)

input = "Allie's Bakery: Sasha's Cakes"
word_cloud = WordCloudData(input)
actual = word_cloud.words_to_counts
expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
print(actual == expected)
