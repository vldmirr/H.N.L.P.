import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-c', '--count')
args = parser.parse_args()

if not args.count:
    print("Колличество не определено")
else:
    print(args.count)