word=input("Input word you'd like to count: ")

vowel = 'A,a,E,e,I,i,O,o,U,u'
Count = 0
for vowel in word:
   Count += 1
print('There are {} vowels in the string: \'{}\''.format(Count,word))

inputString = input("Please enter a string: ")

count = 0
for char in inputString:
    if char in ("a", "e", "i", "o", "u"):
        count += 1
print(f"Number of vowels in {inputString} is {count}")