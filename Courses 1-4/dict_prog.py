name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicto=dict()

for line in handle:
    if not line.startswith('From '): continue
    line=line.rstrip()
    words=line.split()
    for word in words[1:2]:
        dicto[word]=dicto.get(word,0)+1

bign = None
bigw = None
for word,c in dicto.items():
    if bign<c:
        bigw=word
        bign=c

print(bigw,bign)
