# Basic Ceaser Cracker

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ;-.,'"

# Try every possible key

translated = ''

def get_func():
    print('Do you want to (e)ncrypt or (d)ecrypt a Message?')
    func = input()
    function = func[0]
    return function

def get_msg():
    print('Enter the Secret Message you want to crack')
    msg = open("SZ_71", "r")
    return msg
    
def get_key():
    print('Select a key shift')
    key = int(input())
    return key
asnwer = ' '
msg = '''XEF.BANBYNG XNXA.Z'TNFLFGX'ONULNJBE-WNJTEN..PN'XV TA.VT-NTAWNX-XVGEB'XV TA.VT-N
V.C XEN'TV .AXFNJXEXN.ANJ.WXNHFXPNT-G BHZ RJ XEXNFHV N'TV .AXFNJXEXN.'CETVG.VT-R
'TAHT-NFLFGX'FNVBAG.AHXWN.ANHFXONZEXTGNTWITAVXFNJXEXN'TWXN.ANUBG NV.C XENWXF.ZAN
TAWNVELCGTAT-LF.FPNT--N.ANFXVEXVLON.AYBE'TG.BANTUBHGNG .FNCXE.BWN TFNUXZHANGBNUX
NWXV-TFF.Y.XWNTFNG XNBYY.V.T-NUE.G.F NFXVEXVLNCXE.BWN TFNVB'XNGBNTANXAWPNTFNHFNT
'TG X'TG.VT-N'XG BWFNCEB-.YXETGXWN.ANG XNCXE.BWNCE.BENGBNJBE-WNJTENABGTU-LN.ANJ.
--.T'NYONYE.XW'TASFNTCC-.VTG.BANBYNFGTG.FG.VT-NGXV A.DHXFNGBNVELCGTAT-LF.FNTAWNV
.C XENWXIX-BC'XAGNTAWN.AN'TE.TANEX,XJF;.SFN.A.G.T-NUEXT;N.AGBNG XNZXE'TANTE'LSFN'''
count = {}

for character in msg:
    count.setdefault(character, 0)
    count[character] = count[character] +1

#count key-values
list_count = 0

for x in count: 
    list_count += 1

print(list_count, len(LETTERS))



alphabet = [""]

sorted_count = sorted(((value, key) for (key,value) in count.items()), reverse = True)
print(sorted_count)

sorted_letters = list([values[1] for values in sorted_count])
bigram_letters = ''.join(sorted(sorted_letters))
print(bigram_letters, "\n", LETTERS)

#asnwer = input("Is your message encrypted? y/n")
for i in range(len(LETTERS)+1):    
    function = 'd'
    #msg = get_msg()
   
    key = i

    # Start the translation
    for chr in msg:
        if chr in LETTERS:
            num = LETTERS.find(chr)

            if function == 'e':
                num = num + key
            elif function == 'd':
                num = num - key

    # Sort the wrap around problem, so that it acts like a ceaser wheel
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

    # Start to build the translated string
            translated = translated + LETTERS[num]

        else:
            translated = translated + chr

    # Print the result
    print("Iteration: ", i)
    print(translated)
    translated = ''
    #asnwer = input("Is your message encrypted? y/n: ")

'''for i in range(len(bigram_letters)):    
    function = 'd'
    #msg = get_msg()
   
    key = i

    # Start the translation
    for chr in msg:
        if chr in bigram_letters:
            num = bigram_letters.find(chr)

            if function == 'e':
                num = num + key
            elif function == 'd':
                num = num - key

    # Sort the wrap around problem, so that it acts like a ceaser wheel
            if num >= len(bigram_letters):
                num = num - len(bigram_letters)
            elif num < 0:
                num = num + len(bigram_letters)

    # Start to build the translated string
            translated = translated + bigram_letters[num]

        else:
            translated = translated + chr

    # Print the result
    print("Iteration: ", i)
    print(translated, "\n")
    translated = ''
    '''