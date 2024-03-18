import sys

def check_eq(val, expected):
    errors = []
    if val != expected:
        errors.append("Expected: "+str(expected))
        errors.append("Got:" + str(val))
    return errors

def check_output(f, expected):
    old_stdout = sys.stdout
    with open('output.txt', 'w') as sys.stdout:
        f()
    sys.stdout = old_stdout
    errors = []
    with open('output.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) != len(expected):
            if len(lines) >= len(expected):
                errors.append("Too many lines")
            else:
                errors.append("Too few lines")
        for i,(x,l) in enumerate(zip(expected,lines)):
            l = l.strip()
            if l != x:
                errors.append("Discrepancy on line" + str(i))
                errors.append("Expected: "+str(x))
                errors.append("Got:" + str(l))
    return errors

def report(msg,errs):
    if len(errs) == 0:
        print(msg, "OK")
    else:
        print(msg,"Errors:")
        for e in errs: print (e)

    
