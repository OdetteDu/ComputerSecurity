import re
import collections
from sets import Set

f = open('trace.txt','r')
res={}
c = collections.Counter()   
for line in f:
    if line[0]==' ':
        newline=re.sub(r'[^0-9.\s]', '', line)
        cur=newline.split()
        ip1=cur[0].split('.')
        ip2=cur[1].split('.')
        if len(ip2)==5:
            pair=''
            for i in range(4):
                pair=pair+ip1[i]
            pair+='###'
            for i in range(4):
                pair=pair+ip2[i]
            if pair in res:
                res[pair].add(int(ip2[4]))
            else:
                res[pair]=set([int(ip2[4])])

for pair in res:
    c[pair]=len(res[pair])
print c.most_common(20)
print sorted(res['1030165###10305234'])
f.close()
