import Table
# Closer function

def Closer(table , attrSet):
    closer = {}.union(attrSet)

    for i in range(len(closer)):
            for index in range(table.getNoOfFds()):
                fd = table.getFdById(index)
                fdLeft = fd[0]
                fdRight = fd[1]
                if(fdLeft.issubset(closer)):
                    closer.union(fdRight)

def MinimalCover(table):
    pass;

def CandidateKey(table):
    pass;




