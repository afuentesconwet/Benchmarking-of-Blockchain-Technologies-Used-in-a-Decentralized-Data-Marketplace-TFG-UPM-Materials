from datetime import datetime
import sys
import statistics

f = open("sublog", "r")

dataTimes = []

dataLines = []

for l in f.readlines():
	if "DATA RECEIVED" in l:
		dataLines.append(l.split()[-1])

for v, w in zip(dataLines[:-1], dataLines[1:]):
	t1 = datetime.strptime(v, '%H:%M:%S.%f')
	t2 = datetime.strptime(w, '%H:%M:%S.%f')
	print("ESTO: {}".format(t2-t1))
	dataTimes.append(t2.timestamp() - t1.timestamp())

avgData = sum(dataTimes)/len(dataTimes)
print(avgData)

print("Received {} Data Updates in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(dataTimes)+1, sum(dataTimes), statistics.stdev(dataTimes), sum(dataTimes)/len(dataTimes), len(dataTimes)/sum(dataTimes)))
