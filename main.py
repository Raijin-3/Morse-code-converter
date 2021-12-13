MORSE_CODE ={ 
              'A':'.-', 
              'B':'-...',
              'C':'-.-.',
              'D':'-..',
              'E':'.',
              'F':'..-.',
              'G':'--.',
              'H':'....',
              'I':'..',
              'J':'.---',
              'K':'-.-',
              'L':'.-..',
              'M':'--',
              'N':'-.',
              'O':'---',
              'P':'.--.',
              'Q':'--.-',
              'R':'.-.',
              'S':'...',
              'T':'-',
              'U':'..-',
              'V':'...-',
              'W':'.--',
              'X':'-..-',
              'Y':'-.--',
              'Z':'--..',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              '0':'-----',
              ', ':'--..--',
              '.':'.-.-.-',
              '?':'..--..',
              '/':'-..-.',
              '-':'-....-',
              '(':'-.--.',
              ')':'-.--.-'
}


text = input("please enter your message: ").upper()


splited_text = []
morsed_splited_text = []


for letter in text:
    splited_text.append(letter)

    
for item in splited_text:
    item = MORSE_CODE[item]
    morsed_splited_text.append(item)


coded_text = ''.join(morsed_splited_text)
print(f"The coded message is: {coded_text}")