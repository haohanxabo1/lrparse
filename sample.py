import lrparse

# lr() → first match between delimiters
print(lrparse.lr("pre[mid]post", "[", "]"))
# ['mid']

# lrr() → all matches between delimiters
print(lrparse.lrr("<a><b>c", "<", ">"))
# ['a', 'b']

# If delimiters don't exist, you get an empty list
print(lrparse.lr("hello world", "{", "}"))
# []

# If both delimiters are empty, the whole string is returned
print(lrparse.lr("abc", "", ""))
# ['abc']
