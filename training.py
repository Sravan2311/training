text = "Hello, World!"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.find("World"))
print(text.replace("World", "Python"))
padded = "  hello  "
print(padded.strip())
words = text.split(", ")
result = "-".join(words)
print(result)
print(text.startswith("H"))
print(text.endswith("!"))
print("World" in text)
name = "Alice"
age = 30
print(f"{name} is {age} years old")