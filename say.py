# This program uses the cowsay library to print a message in a cow speech bubble.
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])