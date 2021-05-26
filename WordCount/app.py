# Approach 1
#test_string = input("Enter what you are thinking:")
#word_cnt = test_string.split()
#print("Number of words", len(word_cnt))

# Approach 2
import re
test_string = "Today is a sunny day compared to last day"
print(re.findall(r'\w+',test_string))
print(len(re.findall(r'\w+',test_string)))

