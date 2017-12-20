import networkx as nx
import csv

G=nx.Graph()

with open('edgelist.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        G.add_edge(row['source'],row['target'])

nx.write_edgelist(G,'test.edgelist',data=False)
print "done"