f = open("SZ_71", "r")

if f.mode == "r":
	content = f.read()
	print (content)
	print ("text length: ", len(content))

	count = {}

	for character in content:
		count.setdefault(character, 0)
		count[character] = count[character] +1
	print(count)