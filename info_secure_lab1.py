import matplotlib.pyplot as plt
#71 option
f = open("VT00", "r")

if f.mode == "r":
	content = f.read()
	print (content)
	print ("text length: ", len(content))

	#count alphabet

	count = {}

	for character in content:
		count.setdefault(character, 0)
		count[character] = count[character] +1
	print(count)

	#count key-values
	list_count = 0

	for x in count: 
		list_count += 1

	print(list_count)

	alphabet = [""]




plt.bar(range(len(count)), sorted(list(count.values()), reverse = True), align='center')
plt.xticks(range(len(count)), list(count.keys()))

plt.show()


