import argparse

parser = argparse.ArgumentParser(description='Calculator program')

parser.add_argument("operation", type=str, help="Operation - either x / + - ^ %")
parser.add_argument("integer1", type=int, help="First Integer")
parser.add_argument("integer2", type=int, help="Second Integer")

args = parser.parse_args()

if args.operation == "x":
    print (args.integer1 * args.integer2)

if args.operation == "/":
    print (args.integer1 / args.integer2)

if args.operation == "+":
    print (args.integer1 + args.integer2)

if args.operation == "-":
    print (args.integer1 - args.integer2)

if args.operation == "^":
    print (args.integer1 ** args.integer2)

if args.operation == "%":
    print (args.integer1 % args.integer2)