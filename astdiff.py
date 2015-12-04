#!/usr/bin/python
import os
import subprocess
import sys
import ast
import tempfile

import codegen

from optparse import OptionParser

sys.path.insert(0, os.path.dirname(__file__))

parser = OptionParser()
parser.add_option("-u", action="store_true", default=True,
                  help="ignored. ALWAYS -u!")
parser.add_option("-L", dest="L", action="append")

options, args = parser.parse_args()

fn1, fn2 = args

tempdir = tempfile.mkdtemp()

d1 = open(fn1).read()
d2 = open(fn2).read()

b1 = os.path.basename(fn1)
b2 = os.path.basename(fn2)

if b1 == b2:
    b2 = b2 + ".other"

ast1 = ast.parse(d1)
ast2 = ast.parse(d2)

pretty1 = codegen.to_source(ast1)
pretty2 = codegen.to_source(ast2)

outfn1 = os.path.join(tempdir, b1)
out1 = open(outfn1, "w")
out1.write(pretty1)
out1.close()

outfn2 = os.path.join(tempdir, b2)
out2 = open(outfn2, "w")
out2.write(pretty2)
out2.close()

cmdline = ["diff", "-u"]
if options.L:
    for L in options.L:
        cmdline.append("-L")
        cmdline.append(L)
cmdline.extend([outfn1, outfn2])

# print "CALLED WITH:", sys.argv
# print "PRODUCING  :", cmdline


subprocess.call(cmdline)

subprocess.call(["rm", "-rf", tempdir])
