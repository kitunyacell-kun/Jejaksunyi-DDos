import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install scapy")
    os.system("pip install datetime")
    os.system("pip install colorama")
    
    os.system("pip install aiohttp")
elif c == "1":
    os.system("pip3 install scapy")
    os.system("pip3 install datetime")
    os.system("pip3 install colorama")
print("Done.")
