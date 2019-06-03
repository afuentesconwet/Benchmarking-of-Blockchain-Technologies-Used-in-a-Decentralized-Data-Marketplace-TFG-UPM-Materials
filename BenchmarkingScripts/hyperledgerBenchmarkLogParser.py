import sys
import statistics

f = open("log", "r")

offerTimes = []
dataTimes = []
acquiTimes = []
payTimes = []
acceptTimes = []

avgOffer = 0
avgData = 0
avgAcqui = 0
avgAccept = 0
avgPay = 0

for l in f.readlines():
	if "Offering" in l:
		words = l.split()
		offerTimes.append(int(words[-1][:-2]))
		avg = 0
		for elem in offerTimes:
			avgOffer += elem

	if "Dataset" in l:
		words = l.split()
		dataTimes.append(int(words[-1][:-2]))
		for elem in dataTimes:
			avgData += elem

	if "Acquisition" in l:
		words = l.split()
		acquiTimes.append(int(words[-1][:-2]))
		for elem in acquiTimes:
			avgAcqui += elem

	if "Accepted" in l:
		words = l.split()
		acceptTimes.append(int(words[-1][:-2]))
		for elem in acceptTimes:
			avgAccept += elem

	if "Payment" in l:
		words = l.split()
		payTimes.append(int(words[-1][:-2]))
		for elem in payTimes:
			avgPay += elem

print("Offer: {}".format(offerTimes))
print("Data: {}".format(dataTimes))
print("Acqui: {}".format(acquiTimes))
print("Accept: {}".format(acceptTimes))
print("Pay: {}".format(payTimes))

print("Created {} Offerings in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(offerTimes), sum(offerTimes), statistics.stdev(offerTimes), sum(offerTimes)/len(offerTimes), len(offerTimes)/sum(offerTimes)))
print("Accepted {} Agreements in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(acceptTimes), sum(acceptTimes), statistics.stdev(acceptTimes), sum(acceptTimes)/len(acceptTimes), len(acceptTimes)/sum(acceptTimes)))
print("Confirmed {} Payments in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(payTimes), sum(payTimes), statistics.stdev(payTimes), sum(payTimes)/len(payTimes), len(payTimes)/sum(payTimes)))
print("Created {} Datasets in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(dataTimes), sum(dataTimes), statistics.stdev(dataTimes), sum(dataTimes)/len(dataTimes), len(dataTimes)/sum(dataTimes)))
print("Created {} Acquisitions in {} ms. Jitter: {}. AverageLatency: {}. Throughput: {}.".format(
	len(acquiTimes), sum(acquiTimes), statistics.stdev(acquiTimes), sum(acquiTimes)/len(acquiTimes), len(acquiTimes)/sum(acquiTimes)))
