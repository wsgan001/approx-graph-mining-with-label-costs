import sys
from plot import *
from collections import deque

def process(inpfile, outfile):
    f = open(inpfile)
    lines = deque([i.strip() for i in f.readlines()])
    xvalues = [10*i for i in range(1, 51)]
    def read_two(qu):
        l1 = qu.popleft()
        l2 = qu.popleft()
        return xvalues, [float(x) for x in l2.split(",")], "minsup = $%s$"%(str(l1))
    values = []
    while lines:
        values.append(read_two(lines))
    myplot(values, [r'Number of random walks', r'Time in seconds',\
                    r'Time for random walks in CMDB dataset'], outfile)

if __name__ == '__main__':
    print 'Usage: python cmdb_diffminsup_time.py cmdb_diffminsup_time/l1ge.stats2 cmdb_diffminsup_time/cmdbtiming.png'
    process(sys.argv[1], sys.argv[2])


