from sys import stdin

def moverCaixas(monte, fonte, alvo):
    crate_pilhas[alvo] += crate_pilhas[fonte][-monte:]
    crate_pilhas[fonte] = crate_pilhas[fonte][:-monte]

def pilhasCriadas(dados):
    pilhas = []
    for i, char in enumerate(pilhasString):
        if char == ' ': continue
        pilhas.append([])

        for lvl in dados[::-1]:
            if len(lvl) <= i or lvl[i] == ' ': continue
            pilhas[-1].append(lvl[i])

    return pilhas

pib = []
for line in stdin:
    pib.append(line.rstrip())
    if not '[' in line: break
stdin.readline()

pilhasString = pib.pop()
crate_pilhas = pilhasCriadas(pib)

for line in stdin:
    X, Y, Z = map(int, line.split()[1::2])
    moverCaixas(X, Y-1, Z-1)

print(''.join([pilha[-1] for pilha in crate_pilhas]))