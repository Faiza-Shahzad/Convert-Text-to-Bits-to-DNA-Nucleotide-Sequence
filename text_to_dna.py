text=str(input("Enter the Text: "))
print("The text enetered by user is: ",text)
print("----------------------------")
def text_to_ASCII(text):
    ASCIIvalues=[]
    for ch in text:
        ASCIIvalues.append(ord(ch))
    return ASCIIvalues
def ASCII_to_bits(ASCII_LIST):
    str=""
    for number in ASCII_LIST:
        str+=format(number,"08b")
    return str
print("ASCI:")
def bits_to_DNA(bits):
    map={"00":"A","01":"T","10":"G","11":"C"}
    dna=""
    for i in range(0,len(bits),2):
        pair=bits[i:i+2]
        dna+=map[pair]
    return dna
def DNA_to_bits(dna):
    rev_map={"A":"00","T":"01","G":"10","C":"11"}
    bits=""
    for base in dna:
        bits += rev_map[base]
    return bits
def bits_to_text(bits):
    txt=""
    for i in range(0,len(bits),8):
        chunk=bits[i:i+8]    
        number=int(chunk,2)     
        txt+=chr(number)     
    return txt
values=text_to_ASCII(text)
print(values)
print("")
print("Bits:")
bits=ASCII_to_bits(values)
print(bits)
print("")
print("DNA: ")
dna=bits_to_DNA(bits)
print(dna)
recovered_bits=DNA_to_bits(dna)
recovered_text=bits_to_text(recovered_bits)
print("-------------------------------")
print("Recovered text:",recovered_text)
print("Round trip OK:",recovered_text==text)
print("-------------------------------")