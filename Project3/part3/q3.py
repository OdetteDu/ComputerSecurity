import re
import collections
f = open('trace.txt','r')
res=[]
c = collections.Counter()

for line in f:
    if line[0]==' ' and 'Flags [S]' in line:#syn packet
        newline=re.sub(r'[^0-9.\s]', '', line)
        cur=newline.split()
        ip1=cur[0].split('.')
        ip2=cur[1].split('.')
        a=ip1[0]+ip1[1]+ip1[2]+ip1[3]
        b=ip2[0]+ip2[1]+ip2[2]+ip2[3]
        pair=a+b
        c[pair]+=1

print c.most_common(20)
f.close()
