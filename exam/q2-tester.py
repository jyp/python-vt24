from outcheck import *
from q2 import *

report("genome1",
       check_output(lambda: gene_match("ACA","genome1.txt"),
                    ["2","4"]))
report("genome2",
       check_output(lambda: gene_match("AAAAA","genome2.txt"),
                    [str (i) for i in range(7)]))
