print("Enter the values (P1, P2, A, B, F) :")
inp = [input() for i in range(5)]
print(inp)


B = {
    "true": 0.001,
    "false": 0.999
}

F = {
    "true": 0.002,
    "false": 0.998
}

P1 = {
    "true": {"true": 0.95, "false": 0.05},
    "false": {"true": 0.05, "false": 0.95}
}

P2 = {
    "true": {"true": 0.80, "false": 0.01},
    "false": {"true": 0.20, "false": 0.99}
}

A = {
    "true": { 
        "true" : {"true": 0.95, "false": 0.94},
        "false": {"true": 0.29, "false": 0.001} 
        },
    "false": {
        "true" : {"true": 0.05, "false": 0.06},
        "false": {"true": 0.71, "false": 0.999} 
        }
}

ans = P1[inp[0]][inp[2]] * P2[inp[0]][inp[2]] * A[inp[2]][inp[3]][inp[4]] * B[inp[3]] * F[inp[4]]

# print(P1[inp[0]][inp[2]])
# print(P2[inp[0]][inp[2]])
# print(A[inp[2]][inp[3]][inp[4]] )
# print(B[inp[3]])
# print(F[inp[4]])

print(ans)

