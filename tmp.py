# Basic Ceaser Cracker

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ -',.;"

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
#asnwer = input("Is your message encrypted? y/n")
  
#msg = get_msg()
msg = '''NRXQMQRHBMVJHVRJ-HC'QFNTGARHVCAQ P CUVRQ N'BJVUAVAUN BIB NUQVAJNKQMHVRG QMN.BQAV
AU-NVHNKMCIV'BJNKMCIVAUNQA'N'BHQ VJQHVCANCTNVA'BYNTCMNJFJHB.N BIB NQA'NBJHQS VJX
BJNHBRXAVRQ N'B.QA'JNTCMNRCAJHMGRHVAUNQA'NHBRXAC CUFN'BJVUAN BIB -NQJNHC'QFWJNKM
QRHVRBNJXCDJ;NRCMMBRHNBAUVABBMVAUNRCAJHMGRHVIBNQA'NHBRXAC CUVRQ N'BRVJVCAJNQMBNG
AQS BNHCNRC.KBAJQHBNXC BJ;NDXVRXNDBMBN.Q'BNCANJFJHB.NQA'NTGARHVCAQ P CUVRQ N'BJV
HXMBBN BIB JNCTNKHJNRC.KGHBMPQV'B'N'BJVUANRCG 'NSBNKCVAHB'NCGH;NDXVRXNQMBN'VTTBM
BAHVQHB'NSFN VJHNQA'NRXQMQRHBMNCTNJC IVAUNHQJZJ-NVANCGMNCKVAVCANJFJHB.NQA'NKQMHV
RG QM FNTGARHVCAQ P CUVRQ N'BJVUAN BIB JNQMBNHXBNZBFNTCMN.QVANKHJNKQMQ.BHBMJNQA'''

key = get_key()

def encrypt(msg, key, function, translated):

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
    return translated

while asnwer != 'y':
    decr = encrypt(msg, key, 'd', translated)
    asnwer = input("Is your message encrypted? y/n: ")