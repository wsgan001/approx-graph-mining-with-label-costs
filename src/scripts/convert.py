# read the sim file, db file and replace string labels of the vertices in the
# graph with integer labels starting with 0
# also convert the file to a cost file with space between the values

import sys
import pdb
import networkx as nx
import pdb

def read_db(db):
# read the input graph and get a mapping for its vertices
    count = 0
    vmap = {} # key is the vertex id and the value is the new vid
    f = open(db)
    for line in f.readlines():
        line = line.strip()
        print line
        sp = line.split()
        try:
            if sp[0].startswith("v"):
                old = int(sp[1])
                if old not in vmap:
                    vmap[old] = count
                    count += 1
        except Exception:
            pass

    return vmap



def convert(db, sim, dbout, simout):
    s = open(sim)
    w = open(simout, 'w')
    header = s.readline()
    labs = header.split()
    labmap = dict(zip(labs, range(len(labs))))
    hout = ' '.join(str(labmap[i]) for i in labs)
    w.write(hout+"\n")
    lines = []
    for line in s.readlines():
        line = line.strip()
        sp = line.split()
        l1  = [str(labmap[sp[0]])]
        l2 = map(lambda x:str(1-float(x)), sp[1:])
        #valline = ' '.join([str(labmap[sp[0]])] + map(lambda x: 1.0 - float(x), sp[1:]))
        valline = ' '.join(l1+l2)
        lines.append(valline)
    w.write('\n'.join(lines))
    w.close()
    # convert the graph
    vmap = read_db(db)
    d = open(dbout, 'w')
    for line in open(db).readlines():
        line = line.strip()
        if not line:
            continue
        sp = line.split(" ")
        if sp[0] == 'v':
            sp[2] = str(labmap[sp[2]])
            sp[1] = str(vmap[int(sp[1])])
        if sp[0] == 'e':
# get the modified vid
            sp[1] = str( vmap[int(sp[1])])
            sp[2] = str( vmap[int(sp[2])])
        d.write(' '.join(sp) + "\n")
    d.close()


if __name__ == '__main__':
    convert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
