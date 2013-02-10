import pdb
import os
import sys
import os.path
import commands

def ensure(directory):
    if not os.path.exists(directory):
            os.makedirs(directory)

DS = "../results/test/"
DB  = "../data/test2.txt"
SIM  = "../data/testSim.txt"
HOPS  = "../data/test.khops"
WALKS = [1, 2]
ALPHA  = [0.2]
MINSUP  = [3]
SEED  = [1729]
ALGO = [1, 0] # 1 is compressed label and 0 is complete enumeration


for walk in WALKS:
    for alpha in ALPHA:
        for minsup in MINSUP:
            for seed in SEED:
                for algo in ALGO:
                    ensure(DS)
                    filesuffix = "W%sE%sM%sS%sA%s.txt"%(str(walk), str(alpha),\
                                    str(minsup), str(seed), str(algo))
                    confile = os.path.join(DS, "Config_"+filesuffix)
                    statfile = os.path.join(DS, "Stat_"+filesuffix)
                    logfile = os.path.join(DS, "Log_"+filesuffix)
                    f1 = open(confile, 'w')
                    attrs = ["DB", "SIM", "HOPS", "WALKS", "ALPHA", "SEED",\
                            "MINSUP", "ALGO"]
                    values = [DB, SIM, HOPS, walk, alpha, seed, minsup, algo]
                    f1.write('\n'.join([i+" "+str(j) for i,j in zip(attrs,\
                        values)]))
                    f1.close()
                    cmd = './mine %s %s %s'%(confile, logfile, statfile)
                    print cmd
                    commands.getstatusoutput(cmd)

if __name__ == '__main__':
    pass
