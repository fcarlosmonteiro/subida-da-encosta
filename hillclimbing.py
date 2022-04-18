import random
import string

#gerar a solucao
def gerar_solucao(length=9):
    sol = []
    for _ in range (length):
        sol.append(random.choice(string.printable))
    return sol

#expadir a vizinhanca
def expandir_vizinhanca(solucao):
    index = random.randint(0,len(solucao)-1)
    solucao[index]=random.choice(string.printable)
    return solucao

#funcao objetivo
def funcao_objetivo(solucao):
    objetivo=list("Ola mundo")
    valor_fit=0
    for i in range(len(objetivo)):
        s=solucao[i]
        t=objetivo[i]
        valor_fit+=abs(ord(s)-ord(t))
    return valor_fit

#fluxo
best = gerar_solucao()
best_score = funcao_objetivo(best)
iteracao=0

while True:
    iteracao+=1

    if best_score == 0:
        break
    nova_solucao=list(best)
    expandir_vizinhanca(nova_solucao)

    score = funcao_objetivo(nova_solucao)
    if score<best_score:
        best=nova_solucao
        best_score=score
        print("Iteração", iteracao,"-- Solução:","".join(best), "-- Valor de avaliação:", best_score)
