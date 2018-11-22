import sys
from genfun import *

genout = sys.argv[1]
goutput = open(genout, "r")
transmittedMessage = goutput.readline().rstrip()
transmittedMessage = int(transmittedMessage,base=2)
transmittedMessage = bin(transmittedMessage)[2:]

