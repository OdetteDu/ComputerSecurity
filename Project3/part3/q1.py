import re

f = open('trace.txt','r')
res=[]
count=0
for line in f:
    if line[0]==' ':
        newline=re.sub(r'[^0-9.\s]', '', line)
        cur=newline.split()
        ip1=cur[0].split('.')
        ip2=cur[1].split('.')
        if len(ip2)==5:
            if ip2[4]=='80':
                if not cur[1] in res:
                    flag=0
                    if not ip1[0]=='10':
                        flag=1
                    if not ip1[1]=='30':
                        flag=1
                    if not ip1[2]=='22':
                        flag=1
                    if not ip1[3]=='101':
                        flag=1
                    if flag==0:
                        res.append(cur[1])

print res
f.close()
