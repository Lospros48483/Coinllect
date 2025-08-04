from os import system
ask = input("Windows (W), Mac OS (M), Linux (L): ")

with open('os.txt', 'w') as openfile:
    openfile.write(ask)
    
with open('num.txt', 'w') as openfile:
    openfile.write("0")

if ask == "w" or ask == "W":
    system("powershell pip install opencv-python")
else:
    system("pip3 install opencv-python")
    
if ask == "w" or ask == "W":
    system("powershell pip install pillow")
else:
    system("pip3 install pillow")
