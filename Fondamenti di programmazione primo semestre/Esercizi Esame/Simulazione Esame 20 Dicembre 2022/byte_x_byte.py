fileA = "func3_1_exp.txt"
fileB = "func3_1_out.txt"

fileA = open(fileA, "rb")
fileB = open(fileB, "rb")

Acontent = fileA.read()
Bcontent = fileB.read()

fileA.close()
fileB.close()

try:
    for i in range(len(Acontent)):
        if Acontent[i] != Bcontent[i]:
            print(f"({i}) {Acontent[i]} != {Bcontent[i]}")
except Exception:
    pass
        
print(Acontent)
print(Bcontent)