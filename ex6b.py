from collections import deque

s = input("Enter a string: ")

# Remove special characters and convert to lowercase
clean = ""
for ch in s:
    if ch.isalnum():
        clean += ch.lower()

q = deque(clean)

palindrome = True

while len(q) > 1:
    if q.popleft() != q.pop():
        palindrome = False
        break

print("Processed String:", clean)

if palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
