#!/usr/bin/env python

"""
dot_find_cycles.py - uses Pydot and NetworkX to find cycles in a dot file directed graph.

Very helpful for 

By Jason Antman <jason@jasonantman.com> 2012.

Free for all use, provided that you send any changes you make back to me, update the changelog, and keep this comment intact.

REQUIREMENTS:
Python
python-networkx - <http://networkx.lanl.gov/>
graphviz-python - <http://www.graphviz.org/>
pydot - <http://code.google.com/p/pydot/>
(all of these are available as native packages at least on CentOS)

USAGE:
dot_find_cycles.py /path/to/file.dot

The canonical source of this script is:
$HeadURL$
$LastChangedRevision$

CHANGELOG:
    Wednesday 2012-03-28 Jason Antman <jason@jasonantman.com>:
        - initial script creation
"""

import sys
from os import path, access, R_OK
import networkx as nx

def main():

    path = ""
    if (len(sys.argv) > 1):
        path = sys.argv[1]
    else:
        sys.stderr.write("USAGE: dot_find_cycles.py /path/to/file.dot\n")
        sys.exit(1)

    try:
        fh = open(path)
    except IOError as e:
        sys.stderr.write("ERROR: could not read file " + path + "\n")
        sys.exit(1)


    # read in the specified file, create a networkx DiGraph
    G = nx.DiGraph(nx.read_dot(path))

    C = nx.simple_cycles(G)
    if(len(C) < 1):
        sys.exit(0)
    for i in C:
        print i
    
        
# Run

if __name__ == "__main__":
    main()