# This will make it so somthing is timed out if it takes too long.

def timedout():
    i = 30
    while i > 0:
        i = i - 1
        time.sleep(1)
        if i == 0:
            print("Timed Out")
