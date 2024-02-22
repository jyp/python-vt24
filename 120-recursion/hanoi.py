
def move1(source,destination):
    disc = source.pop()
    destination.append(disc)
    # print(pegs)

def hanoi(source,intermediate,destination,n):
    # move n discs from source to destination, with an intermediate.
    if n>0:
        hanoi(source,destination, intermediate,n-1)
        move1(source,destination)
        hanoi(intermediate,source,destination,n-1)

number_of_discs = 5
stack = list(reversed(range(1,number_of_discs+1)))
pegs = [stack,[],[]]

print(pegs)
hanoi(pegs[0],pegs[1],pegs[2],number_of_discs)        
