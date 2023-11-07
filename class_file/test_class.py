
a = [1,2,3,4,5,6,7,8,9,10]

b = []

[b.append(url) for url in a if url%2 == 0]
print(b)