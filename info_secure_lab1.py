import matplotlib.pyplot as plt
import itertools 
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

	#count key-values
	list_count = 0

	for x in count: 
		list_count += 1

	print(list_count)



	alphabet = [""]

sorted_count = sorted(((value, key) for (key,value) in count.items()), reverse = True)
print(sorted_count)

sorted_letters = list([values[1] for values in sorted_count])

sorted_keys = list([keys[0] for keys in sorted_count])

bigram_letters = ''.join(sorted_letters[:10])


#bigram = [x*x for x in bigram_letters]

t_bigram = list(itertools.permutations(bigram_letters, 2))
#bigram = list(itertools.chain(*t_bigram))

print(t_bigram)

#for i in range(pow(len(bigram_letters)),2):
	#bigram.append()


bigram_keys = sorted_keys[:10]

print(bigram_letters)


#sorted_keys = list()

plt.bar(sorted_letters, sorted_keys, align='center')
plt.xticks(range(len(count)), sorted_letters)

plt.show()

plt.bar(range(len(count)), list(count.values()), align='center')
plt.xticks(range(len(count)), list(sorted(count.keys())))
plt.show()