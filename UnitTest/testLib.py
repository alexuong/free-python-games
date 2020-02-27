"""
Collection of utilities for testing.
"""

from contextlib import contextmanager


@contextmanager
def captured_output():
    import sys
    from StringIO import StringIO
    
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def winOrLin():
    import os
    #Windows or Linux?
    if os.name == 'nt':
        slash = '\\'
        isWin = True
    elif os.name == 'posix':
        slash = '/'
        isWin = False
    return slash, isWin


def writeInput(path,inp):
    import os
    slash, isWin = winOrLin()
    cwd = os.getcwd()
    # delete the input file
    if os.path.isfile(cwd + slash + path):
        command = 'rm ' + cwd + slash + path
        os.system(command)
    # write an input file to be read in
    f = open(path, 'w')
    for lineNum in xrange(0, len(inp)):
        f.write(inp[lineNum] + '\n')
    f.close()


def readFile(path):
    import sys
    error_to_catch = getattr(__builtins__, 'FileNotFoundError', IOError)
    try:
        f = open(path,'r')
    except error_to_catch:
        print('File not found!')
        sys.exit(1)
    x = f.readlines()
    f.close()
    y = []
    # Cycle through file lines
    for z in x:
        if (len(z) > 1):
            y.append(z)
    return y


def round_sig(x, sig=2):
    from math import log10, floor
    if x > 0:
        return round(x, sig-int(floor(log10(x)))-1)


def md5(fname):
    import hashlib
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
