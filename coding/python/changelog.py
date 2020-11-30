# This makes it so when this happens, it will ask your premission to veiw the changelog. #

cg = input("see change log?(y/n)\n")
print("")
if cg == "y":
	cg = open('change.txt', "r")
	changed = cg.read()
	print(changed)
	cg.close()
	print("")
