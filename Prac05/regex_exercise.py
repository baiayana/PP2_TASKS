#1
import re

pattern = r'^ab*$'

text = input("Enter a string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#2
import re

pattern = r'^ab{2,3}$'

text = input("Enter a string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#3
import re

pattern = r'\b[a-z]+_[a-z]+\b'

text = input("Enter a string: ")

matches = re.findall(pattern, text)

print("Matches:", matches)

#4
import re

pattern = r'\b[A-Z][a-z]+\b'

text = input("Enter a string: ")

matches = re.findall(pattern, text)

print("Matches:", matches)

#5
import re

pattern = r'^a.*b$'

text = input("Enter a string: ")

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")

#6
import re

text = input("Enter a string: ")

result = re.sub(r'[ ,.]', ':', text)

print(result)

#7
text = input("Enter snake_case string: ")

words = text.split('_')

camel = words[0] + ''.join(word.capitalize() for word in words[1:])

print(camel)

#8
import re

text = input("Enter a string: ")

result = re.split(r'(?=[A-Z])', text)

print(result)

#9
import re

text = input("Enter a string: ")

result = re.sub(r'([A-Z])', r' \1', text).strip()

print(result)

#10
import re

text = input("Enter camelCase string: ")

snake = re.sub(r'([A-Z])', r'_\1', text).lower()

print(snake)        