import os
os.system('clear')
import socket
banner = print("""
\033[1;31m
████████╗░░░██╗░░░██╗░░░░██████╗░  ████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝░░░╚██╗░██╔╝░░░██╔════╝░  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░░░░░╚████╔╝░░░░██║░░██╗░  ░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░░░░░░╚██╔╝░░░░░██║░░╚██╗  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░██╗░░░██║░░░██╗╚██████╔╝  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░╚═════╝░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
                     𝑪𝒐𝒅𝒆 𝑩𝒚 𝑴𝒓 𝑺𝒂𝒎𝒊 |𝒊𝒏𝒂𝒔𝒕𝒂| @𝒄𝒚𝒃𝒆𝒓_77𝒌
	""")
spider = input('\033[1;31mEnter URL Site :\033[1;32m ')
port = input('\033[1;31mEnter Name Port :\033[1;32m ')
sami = socket.gethostbyname(spider)
po_ye = socket.getservbyname(port)
print('-------------------')
print('\033[1;31murl website : \033[1;32m', spider)
print('\033[1;31mip website : \033[1;32m', sami)
print('\033[1;31mThis is Port: \033[1;32m', po_ye)
print('\033[1;31mName Port : \033[1;32m', port)
print('-------------------')
print('\033[1;31mChannel tele :\033[1;32m @TYG_TEAM')
try_ye = input('\033[1;31mTo close the tool, choose the number (0) Return to the previous list, choose the number (1) ? ')
if try_ye == 1:
	os.system('clear')
	os.system('python ip.py')
elif try_ye == 0:
	os.system('exit')
else:
	os.system('python ip.py')
