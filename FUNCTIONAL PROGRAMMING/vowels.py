lst=["apple","banana","cherry"]

vowels='aeiou'


lst=[''.join ([i for i in word if i not in vowels]) for word in lst]
print(lst)

