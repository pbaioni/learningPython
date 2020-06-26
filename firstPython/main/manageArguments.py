import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="first factor")
parser.add_argument("b", type=int, help="second factor")
args = parser.parse_args()
product = args.a*args.b

print 'The product is:', product




