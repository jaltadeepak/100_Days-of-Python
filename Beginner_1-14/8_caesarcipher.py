# def func_a(para_b, para_c):
#     function code 
# func_a(arg_b, arg_c) // positional arguments
# func_a(b=arg_b, c=arg_c) is the same as func_a(c=arg_c, b=arg_b) // keyword arguments

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
to_cont = True

while to_cont == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        shift = shift%26
        text_list = list(text)
        new_text = ""
        for i in range(0, len(text)):
            if text_list[i] in alphabet:
                pos = alphabet.index(text_list[i])
                if direction=="encode":
                    if pos+shift<=26:    
                        new_text += alphabet[pos+shift]
                    else:
                        new_text += alphabet[pos+shift-26]
                elif direction=="decode":
                    pos = alphabet.index(text_list[i])   
                    new_text += alphabet[pos-shift]       
            else:
                new_text += text_list[i] 
        print(f"The {direction}d text is {new_text}")

    caesar(text, shift, direction)

    cont = input("type yes to continue, and no to end... ")

    if cont == "yes":
        continue
    if cont == "no":
        to_cont = False
        print("GOODBYE!")