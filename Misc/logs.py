
import re
import operator
import csv

error = dict()
per_user = {}
info = {}

with open('testing.py', 'r') as f:
     line = f.readlines()
     for l1 in line:
         result_info = re.search(r"INFO .* \((.*)\)", l1.strip())
         if result_info == None : continue
         elif result_info :
             res = re.search(r"\(.*\)", result_info.group())
             rest = res.group()[1:len(res.group())-1]
             if rest not in per_user:
                 per_user[rest] = {}
             per_user[rest]["INFO"] = per_user[rest].get("INFO", 0) + 1
     for l2 in line:
         result_error = re.search(r"ERROR .*", l2.strip())
         if result_error == None : continue
         elif result_info :
             res = re.search(r"\(.*\)", result_error.group())
             rest = res.group()[1:len(res.group())-1]
             if rest not in per_user:
                 per_user[rest] = {}
             per_user[rest]["ERROR"] = per_user[rest].get("ERROR", 0) + 1

with open('testing.py', 'r') as f2:
    line = f2.readlines()
    for l in line:
        result_e = re.search(r"ERROR .*", l.strip())
        if result_e == None : continue
        elif result_e :
            hes = re.search(r"ERROR (.*)", result_e.group())
            hest = hes.group(1)
            hest2 = ""
            for ch in hest:
                if ch == '(' : break
                else: hest2 += ch
            error[hest2.rstrip()] = error.get(hest2.rstrip(),0) + 1

error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)
per_user = sorted(per_user.items())

error.insert(0,("Error","Count"))
per_user.insert(0,("Username","INFO","ERROR"))

with open('error_message.csv', 'w') as em:
    writer = csv.writer(em)
    writer.writerows(error)

with open('user_statistics.csv', 'w') as us:
    writer = csv.writer(us)
    writer.writerows(per_user)

#print(error)
#print(type(error))
#print(per_user)
#print(type(per_user))
