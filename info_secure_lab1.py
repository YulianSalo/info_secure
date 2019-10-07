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

prep_letters = sorted_letters[1:11]


bigram_letters = ''.join(prep_letters)


#bigram = [x*x for x in bigram_letters]

t_bigram = list(itertools.permutations(bigram_letters, 2))
#bigram = list(itertools.chain(*t_bigram))


new_bigram = []

for i in range(len(t_bigram)):
	new_bigram.append(''.join(t_bigram[i]))

print(new_bigram)

bigram_final = []
bigram_final_count = []


for i in range(len(new_bigram)):
	if new_bigram[i] in content:
		bigram_final.append(new_bigram[i])
		bigram_final_count.append(content.count(new_bigram[i]))

print(len(new_bigram), len(bigram_final), '\n',bigram_final_count)

bigram_dict = dict(zip(bigram_final, bigram_final_count))
print(bigram_dict)

bigram_sorted_dict = sorted(((value, key) for (key,value) in bigram_dict.items()), reverse = True)
print(bigram_sorted_dict)


plt.bar(sorted_letters, sorted_keys, align='center')
plt.xticks(range(len(count)), sorted_letters)

#plt.show()

plt.bar(range(len(count)), list(count.values()), align='center')
plt.xticks(range(len(count)), list(sorted(count.keys())))
#plt.show()
