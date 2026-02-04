import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install colorama")
    os.system("pip install randomstring")
    os.system("pip install colorama")
elif c == "1":
    os.system("pip3 install colorama")
    os.system("pip3 install randomstring")
    os.system("pip3 install colorama")
print("Done.")
