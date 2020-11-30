# This is a helpful snippit that can slow down your text in python #

import time

def sprint(text, wait=0.05):
	for i in text:
		print(i,end="",flush = True)
		time.sleep(wait)
	print("")
