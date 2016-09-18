import operator;
import functools;
import sys;

# Recursive Brute Force implementation
def notSoRandRecursive(N, X, K, A, B, C, ratioList):
    tempList = [];
    tempList2 = ratioList;
    if N == 1:
        ratioMul = functools.reduce(operator.mul, tempList2, 1);
        calc1 = (X&K);
        calc2 = (X|K);
        calc3 = (X^K);
        output = ratioMul * (((A/100)*calc1) + ((B/100)*calc2) + ((C/100)*calc3));
        return output;
    else:
        calc1 = (X&K);
        tempList = tempList2 + [(A/100)];
        recurs1 = notSoRandRecursive(N-1, calc1, K, A, B, C, tempList);
        calc2 = (X|K);
        tempList = tempList2 + [(B/100)];
        recurs2 = notSoRandRecursive(N-1, calc2, K, A, B, C, tempList);
        calc3 = (X^K);
        tempList = tempList2 + [(C/100)];
        recurs3 = notSoRandRecursive(N-1, calc3, K, A, B, C, tempList);

        output = recurs1+recurs2+recurs3;
        return output;


# Non-recursive smoother solution, done with reference to correct solutions posted codejam website
def notSoRandBitwise(N, X, K, A, B, C):
    place = 0;
    output = 0;

    while K!=0 or X!=0:
        # determines rightmost X bit
        xBit = X&1;
        # determines rightmost k bit
        kBit = K&1;

        output += simulFunc(N, xBit, kBit, A, B, C) * pow(2, place);
        place+=1;
        X = X>>1;
        K = K>>1;
    return output;

def simulFunc(N, xBit, kBit, A, B, C):
    bitProb = [0, 0];
    bitProb[xBit] = 1;
    for i in range(0, N):
        bitProbNext = [0, 0];
        # AND Logic probability calc
        bitProbNext[0] += bitProb[0] * (A/100);
        bitProbNext[1&kBit] += bitProb[1] * (A/100); # adjusts bit prob of 0 or 1 depending on if k is 0 or 1
        # OR Logic probability calc
        bitProbNext[0|kBit] += bitProb[0] * (B/100);
        bitProbNext[1] += bitProb[1] * (B/100);
        # XOR Logic probability calc
        bitProbNext[0^kBit] += bitProb[0] * (C/100);
        bitProbNext[1^kBit] += bitProb[1] * (C/100);
        # Set start of next machine as end of previous machine
        bitProb = bitProbNext;
    return bitProb[1]; # Note, probability of 0 is irrelevant to final calculation.

t = int(input());

for i in range(1, t+1):
    N, X, K, A, B, C = map(int, input().split(" "));
    #output = notSoRandRecursive(N, X, K, A, B, C, []);
    output = notSoRandBitwise(N, X, K, A, B, C);
    print("Case #{}: {:.10f}".format(i, output));
