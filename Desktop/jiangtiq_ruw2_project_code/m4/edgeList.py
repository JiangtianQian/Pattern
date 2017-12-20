import networkx as nx
import csv

G=nx.Graph()

with open('node.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        G.add_edge(row['Source'],row['Target'])

nx.write_edgelist(G,'karate.edgelist',data=False)
print "done"