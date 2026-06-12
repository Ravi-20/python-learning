# This program takes a name as a command-line argument and prints a greeting.
import sys

if len(sys.argv) < 2:
    sys.exit("too less arguments provided.")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)