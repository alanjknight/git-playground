import argparse
import sys

def search(list,value):
    for item in range(len(list)):
        if list[item] == value:
            return True
    return False


def create_fezz_output(output):
    new_list = []
    if len(output) == 0:
        return ['Fezz']
    else:
        for item in output:
            if item[0] != 'B':
                new_list.append(item)
            else:
                if search(new_list,'Fezz') == False:
                    new_list.append('Fezz')
                new_list.append(item)
    return new_list


parser = argparse.ArgumentParser(description='FizzBuzz program')

parser.add_argument("end_index", type=int, help="Maximum Integer to count up to")
parser.add_argument("--rules", action="append", help="Any rules to be processed (empty for all)")

args = parser.parse_args()
rules = args.rules

for i in range(1, int(args.end_index)+1):
    output = []
    if not rules or "3" in rules:
        if i % 3 == 0:
            output.append('Fizz')
    if not rules or "5" in rules:
        if i % 5 == 0:
            output.append('Buzz')
    if not rules or "7" in rules:
        if i % 7 == 0:
            output.append('Bang')
    if not rules or "11" in rules:
        if i % 11 == 0:
            output = ['Bong']
    if not rules or "13" in rules:
        if i % 13 == 0:
            output = create_fezz_output(output)
    if not rules or "17" in rules:
        if i % 17 == 0:
            output = output[::-1]
    if len(output) == 0:
        output = [i]
    print(output)



