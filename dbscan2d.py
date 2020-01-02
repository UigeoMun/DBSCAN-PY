#python dbscan1d.py [filepath] [eps] [minpts]

import sys
import csv
from sklearn.cluster import DBSCAN

filepath = sys.argv[1]

eps = float(sys.argv[2])
minpts = int(sys.argv[3])

file = open(filepath, 'r', encoding='utf-8')
csvParsed = csv.reader(file)

chAmpList = []
for idx, amp in enumerate(csvParsed):
    if idx != 0:
        listEl = [ float(amp[0]), float(amp[1]) ]
        chAmpList.append( listEl )

dbsacn = DBSCAN(eps, minpts, 'euclidean')
clusterMask = dbsacn.fit_predict(chAmpList)

values = set(map( lambda x:x, clusterMask ))
clusetrs = [[idx for idx,value in enumerate(clusterMask) if value==x] for x in values]

file.close()
print(clusetrs)
