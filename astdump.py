#!/usr/bin/python
import sys
import os

import ast
import codegen

sys.path.insert(0, os.path.dirname(__file__))


sys.stdout.write(codegen.to_source(ast.parse(open(sys.argv[1]).read())))
