def stateProb(N,nf,maxN):
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
    print(f'Probability of state N={N},nf={nf} is {100*(b1+b2+b3):.2f}%')
    print(p1)
    print(f'{100*b1:.2f} from picking 2 full pills')
    print(p2)
    print(f'{100*b2:.2f} from picking 3 half pills')
    print(p3)
    print(f'{100*b3:.2f} from picking 1 of each')
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

print(f'Result = {100 * stateProb(3, 0, 15):.2f}%')