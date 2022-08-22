import numpy as np
from matplotlib import pyplot as plt

def stateProb(N,nf,maxN,loud=False):
    if N==maxN and nf==maxN:
        return 1.0
    if N>maxN or nf>N:
        return 0.0

    p1 = pf(N+1, nf+2)
    p2 = phh(N+3, nf)
    p3 = ps(N+2, nf+1)
    s1 = stateProb(N+1, nf+2, maxN)
    s2 = stateProb(N+3, nf, maxN)
    s3 = stateProb(N+2, nf+1, maxN)
    b1 = p1 * s1
    b2 = p2 * s2
    b3 = p3 * s3
    if(loud):
        print(f'Probability of state N={N},nf={nf} is {100*(b1+b2+b3):.2f}%')
        print(f'{100*b1:.2f}% from picking 2 full pills')
        print(f'{100*b2:.2f}% from picking 3 half pills')
        print(f'{100*b3:.2f}% from picking 1 of each')
    return b1 + b2 + b3

def pf(N,nf):
    if nf<2 or nf>N:
        return 0.0
    elif N==nf:
        return 1.0
    else:
        return (nf/N)*((nf-1)/(N-1))

def phh(N,nf):
    nh = N-nf
    if nh < 3:
        return 0.0
    else:
        return (nh/N)*((nh-1)/(N-1))*((nh-2)/(N-2))

def ps(N,nf):
    return 1.0 - (pf(N,nf) + phh(N,nf)) 

numPills = np.arange(3,33,3,dtype=np.int32)
rightFinalDose = 1.0 - np.array([stateProb(3,0,n) for n in numPills])

plt.plot(numPills/1.5, 100 * rightFinalDose)
plt.xlabel("Number of Days")
plt.ylabel("\\% Chance of correct final dose")
plt.show()
