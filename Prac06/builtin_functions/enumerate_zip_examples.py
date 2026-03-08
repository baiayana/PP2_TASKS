# Use enumerate() and zip() for paired iteration
# Demonstrate type checking and conversions

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print("Using enumerate:")
for index, name in enumerate(names, start=1):
    print(index, name)

print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

value = "123"

print("\nType checking:")
print(type(value))
print(isinstance(value, str))

converted_value = int(value)
print("Converted value:", converted_value)
print("New type:", type(converted_value))