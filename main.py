#!/usr/bin/env python

# https://docs.python.org/3.6/library/argparse.html#required
import argparse
parser = argparse.ArgumentParser(description='Give me a white russian')
parser.add_argument('-u', metavar='username', type=str, help='Name of the user passed as Arg.', required=True)
args = parser.parse_args()
print (f"Hello World! {args.u}")
