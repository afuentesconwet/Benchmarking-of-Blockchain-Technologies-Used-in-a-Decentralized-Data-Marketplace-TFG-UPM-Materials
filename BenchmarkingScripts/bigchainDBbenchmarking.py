import time
import threading

from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb_root_url = 'localhost:9984'  # Use YOUR BigchainDB Root URL here
bdb = BigchainDB(bdb_root_url)	#Without auth tokens, second param for the tokens.

alice, bob = generate_keypair(), generate_keypair()

numTh = 8
numTx = 10

class BigchainTh(threading.Thread):
	def run(self):
		global numTx
		assetList = []
		txList = []
		fulfilled_token_txList = []

		for i in range(numTx):
			assetList.append(
				{
					'data': {
						'Temperature': 'aajd'+self.getName(),
						'Humidity': i,
						'Location': 'UPM-CoNWetLab'
					}
				}
			)

		for i in range(numTx):
			txList.append(
				bdb.transactions.prepare(
			    		operation='CREATE',
			    		signers=alice.public_key,
			    		recipients=[([bob.public_key], 10)],
			    		asset=assetList[i]
				)
			)

		for i in range(numTx):
			fulfilled_token_txList.append(
				bdb.transactions.fulfill(
		    			txList[i],
		    			private_keys=alice.private_key
				)
			)

		start = time.time()

		for i in range(numTx):
			startTx = time.time()
			bdb.transactions.send_async(fulfilled_token_txList[i])
			endTx = time.time()
			#print("Sent a transaction in {} .".format(endTx-startTx))

		end = time.time()

		print("Thread {} sent {} TXs in {} .".format(self.getName(), numTx, end - start))

def main():
	for i in range(numTh):
		myTh = BigchainTh(name = i)
		myTh.start()

if __name__ == '__main__':
	main()
