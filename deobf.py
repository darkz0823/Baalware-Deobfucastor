import os
import logging
from pystyle import *
import colorama
from pystyle import Box
from pystyle import Colors, Colorate

baalware = """

██████╗  █████╗  █████╗ ██╗     ██╗    ██╗ █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔══██╗██║     ██║    ██║██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║███████║██║     ██║ █╗ ██║███████║██████╔╝█████╗  
██╔══██╗██╔══██║██╔══██║██║     ██║███╗██║██╔══██║██╔══██╗██╔══╝  
██████╔╝██║  ██║██║  ██║███████╗╚███╔███╔╝██║  ██║██║  ██║███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

                     [+] created by baalware   \n                 
"""
os.system("cls")
print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(baalware)))

def decryption(encrypted_file):
    with open(encrypted_file, encoding='utf-8') as f:
        s = f.read()
    # Extract the 'pea' list from the encoded string in the file
    pea_list = eval(s.split('d=')[1].split(';exec')[0])
    decrypted_text = ''
    for encoded_char in pea_list:
        # Determine the original character by calculating the length of each string in 'pea_list'
        decrypted_text += chr(len(encoded_char))
    
    # Save the decrypted file
    decrypted_file = os.path.join("baalware obfs", os.path.splitext(os.path.basename(encrypted_file))[0] + "_decrypted.py")
    with open(decrypted_file, "w", encoding='utf-8') as f:
        f.write(decrypted_text)
        os.system("cls")
    print(Colorate.Horizontal(Colors.red_to_yellow, Center.XCenter(baalware)))
    logging.info("Arquivo descriptografado com sucesso como '{}'".format(decrypted_file))
    print(Center.XCenter("Arquivo descriptografado com sucesso como '{}'".format(decrypted_file)))

while True:
    arquivo = input("\nnome do arquivo que será descriptografado: ")
    if arquivo.lower() == 'sair':
        break
    decryption(os.path.join("baalware obfs", arquivo))
