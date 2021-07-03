import argparse

parser = argparse.ArgumentParser(description='Calculator program')

parser.add_argument("filename", type=str, help="Filename to process.  List of operations in the format 'calc / 69 78'")

args = parser.parse_args()

def perform_single_calc(op, int1, int2):
    if op == "x":
        return float(int1) * float(int2)
    if op == "/":
        return float(int1) / float(int2)
    if op == "+":
        return float(int1) + float(int2)
    if op == "-":
        return float(int1) - float(int2)


with open (args.filename, 'r') as f:
    lines = f.read().splitlines()

result = 0
for line in lines:
    command = line.split()
    result = result + perform_single_calc (command[1], command[2], command[3])
   
print(result)    

    






