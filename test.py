from play import ver_env

env = ver_env()
sA, sB = env.reset()
for i in range(5):
    aA = (1,1,1,1)
    aB = (1,1,1,1)
    sA, rA, sB, rB, done = env.step(aA, aB)
    print('sa:',sA)
    print('sb:',sB)