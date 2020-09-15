import re

lst2=list()
fhand=open('regex_sum_663886.txt')
for line in fhand:
    line=line.rstrip()
    lst=re.findall('([0-9]+)',line)
    if len(lst)<1 : continue
    for num in lst:
        lst2.append(int(num))
print(sum(lst2))
