import queue
class rr:                                 #Using Class as a C-like structure
    def __init__(self,pid,at,bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.av = bt
        self.ct, self.wt, self.tat,self.st = int(), int(), int(), False
    def __str__(self):
        res = str(self.pid)+"\t"+str(self.at)+"\t"+str(self.bt)+"\t"+str(self.av)+"\t"+str(self.ct)+"\t"+str(self.tat)+"\t"+str(self.wt)
        return res
    def __lt__(self,fcfs):
        return self.at < fcfs.at
    

time,tq,l = 0,3,[]
l = [rr(1,5,5),rr(2,4,6),rr(3,3,7),rr(4,1,9),rr(5,2,2),rr(6,6,3)]
l.sort()                                    #OR if __lt__ is not overloaded, l.sort(key=lambda x:x.at)
z = []
k = []
if time >= l[0].at:
    k.append(l[0])
    l[0].st = True
else:
    while(time != l[0].at):
        time = time + 1
    k.append(l[0])
    l[0].st = True
    
c = 0
while c < len(k):
    x = k[c]
    if x.av != 0:
        time += min(tq, x.av)
        x.av -= min(tq, x.av)
        z.append(x.pid)
    for i in l:
        if i.at <= time and i.st == False:
            k.append(i)
            i.st = True
    if x.av > 0:
        k.append(x)
    else:
        x.ct = time
        x.tat = x.ct - x.at
        x.wt = x.tat - x.bt
    del x
    c = c + 1

print("PID\tAT\tBT\tAV\tCT\tTAT\tWT")
for x in l:
    print(x)
print(z)
