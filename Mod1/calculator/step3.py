import argparse

parser = argparse.ArgumentParser(description='Calculator program')

parser.add_argument("steps_file", type=str, help="Step file to process.  List of operations in the format 'goto <lineno>' or 'goto calc / 69 78'")

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

line = 0
list_of_seen_lines = []
#open the step file and process
with open(args.steps_file, 'r') as step_file:
    step_lines = step_file.read().splitlines()
    #find the first step
    

    
    
    

    #for step_line in step_lines:
    #    step = step_line.split()
    #    if(step[1]) == 'calc':
    #        result = perform_single_calc(step[2],step[3],step[4])
    #        line = .index(step[1] + " " + step[2] + " " + step[3] + " " + step[4]) + 1  
    #    else:
    #        continue
    #        #line = step[1]
    #        #op_line = op_lines[int(step[1])-1].split()
    #        #result = result + perform_single_calc(op_line[1],op_line[2],op_line[3])#

print(f"{line}")        

    
    

    






