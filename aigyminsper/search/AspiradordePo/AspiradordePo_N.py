from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State
import copy

class AspiradorPoN(State):

    def _init_(self, op, posicao, situacao, direcao):
        
        # ANDA, DIR, ESQ, LMP
        self.operator = op

        # (linha, coluna)
        self.posicao_robo = posicao
        
        # 0 - LIMPO; 1- SUJO
        self.situacao = situacao

        # N, S, L, O
        self.direcao = direcao

    def sucessors(self):
        sucessors = []
        
        if self.direcao == 'N':
            sucessors.append(AspiradorPoN("dir", self.posicao_robo, self.situacao, "L"))
            sucessors.append(AspiradorPoN("esq", self.posicao_robo, self.situacao, "O"))
            # cim
            if self.posicao_robo[0] - 1 >= 0:
                pos = (self.posicao_robo[0]-1, self.posicao_robo[1])
                sucessors.append(AspiradorPoN("anda N",pos,self.situacao, "N"))

        if self.direcao == 'L':
            sucessors.append(AspiradorPoN("dir", self.posicao_robo, self.situacao, "S"))
            sucessors.append(AspiradorPoN("esq", self.posicao_robo, self.situacao, "N"))
            # dir
            if self.posicao_robo[1] + 1 < len(self.situacao[0]):
                pos = (self.posicao_robo[0], self.posicao_robo[1]+1)
                sucessors.append(AspiradorPoN("anda L",pos,self.situacao, self.direcao))
        
        if self.direcao == 'S':
            sucessors.append(AspiradorPoN("dir", self.posicao_robo, self.situacao, "O"))
            sucessors.append(AspiradorPoN("esq", self.posicao_robo, self.situacao, "L"))
            # bxo
            if self.posicao_robo[0] + 1 < len(self.situacao):
                pos = (self.posicao_robo[0]+1, self.posicao_robo[1])
                sucessors.append(AspiradorPoN("anda S",pos,self.situacao, self.direcao))
        
        if self.direcao == 'O':
            sucessors.append(AspiradorPoN("dir", self.posicao_robo, self.situacao, "N"))
            sucessors.append(AspiradorPoN("esq", self.posicao_robo, self.situacao, "S"))
            # esq
            if self.posicao_robo[1] - 1 >= 0:
                pos = (self.posicao_robo[0], self.posicao_robo[1]-1)
                sucessors.append(AspiradorPoN("anda O",pos,self.situacao, self.direcao))
        
        # lmp
        if self.situacao[self.posicao_robo[0]][self.posicao_robo[1]] == 1:
            sit = copy.deepcopy(self.situacao)
            sit[self.posicao_robo[0]][self.posicao_robo[1]] = 0

            sucessors.append(AspiradorPoN("lmp", self.posicao_robo, sit, self.direcao))
        

        return sucessors

    def is_goal(self):
        soma = 0
        for i in self.situacao:
            soma += sum(i)
        if(soma==0) and (self.posicao_robo == (0,0)):
            return True
        return False 

    def cost(self):
        return 1

    def description(self):
        return "Implementa um aspirador de po para 2 quartos"

    def env(self):
        return self.operator


def main():
    state = AspiradorPoN('',(0,0),[[1,1],[1,1]], 'N')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if _name_ == '_main_':
    main()