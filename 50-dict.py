

def load_dict(fname, source, target):
    d = {}
    file = open(fname)
    for l in file.readlines():
        l = l.strip()
        if len(l) > 0 and l[0] != '#':
            fields = l.split(";")
            for word0 in fields[target].split(","):
                for word1 in fields[source].split(","):
                    d.setdefault(word1.strip(),[]).append(word0.strip())
    return d
    

# d = load_dict("terms.csv", 1, 0)
# print(d['input'])
# d = load_dict("terms.csv", 0, 2)
# print(d['påskägg'])
d = load_dict("terms.csv", 2, 1)
print(d['N'])

