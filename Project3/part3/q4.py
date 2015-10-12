import re
import collections
from sets import Set

f = open('trace.txt','r')
aaa=set()
res=set()
c = collections.Counter()
d = collections.Counter()
for line in f:
    if line[0]==' ' and 'Flags' in line:#tcp packet
        newline=re.sub(r'[^0-9.\s]', '', line)
        cur=newline.split()
        ip1=cur[0].split('.')
        ip2=cur[1].split('.')
        a=ip1[0]+ip1[1]+ip1[2]+ip1[3]
        b=ip2[0]+ip2[1]+ip2[2]+ip2[3]
        if a=='103022101' or b=='103022101':
            if ('Flags 'in line):
                if 'seq 'in line:
                    x=line.split('seq')[1]
                    x=x.split(',')[0]
                    x=x.split()[0]
                    if not ':' in x:
                        seqno=int(x)
                    else:
                        seqno=int(x.split(':')[1])-1
                    c[seqno]+=1
                    s=a+' '+b+' '+str(seqno)
                    aaa.add(s)
                    if s in res and a=='103022101':#already acknowledged and send by phone
                        print s
                if 'ack 'in line:
                    x=line.split('ack')[1]
                    x=x.split(',')[0]
                    x=x.split()[0]
                    ackno=int(x)-1
                    d[ackno]+=1
                    s=b+' '+a+' '+str(ackno)
                    if s in aaa:
                        res.add(s)

