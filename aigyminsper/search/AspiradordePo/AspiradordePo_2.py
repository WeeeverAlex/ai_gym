from aigyminsper.search.SearchAlgorithms import BuscaLargura
from aigyminsper.search.Graph import State
import copy

class AspiradorPo2(State):

    def _init_(self, op, posicao, situacao):
        
        # DIR; ESQ; CIM; BXO; LMP
        self.operator = op

        # (linha, coluna)
        self.posicao_robo = posicao
        
        # 0 - LIMPO; 1- SUJO
        self.situacao = situacao

    def sucessors(self):
        sucessors = []
        
        # esq
        if self.posicao_robo[1] - 1 >= 0:
            pos = (self.posicao_robo[0], self.posicao_robo[1]-1)
            sucessors.append(AspiradorPo2("esq",pos,self.situacao))
        
        # dir
        if self.posicao_robo[1] + 1 < len(self.situacao[0]):
            pos = (self.posicao_robo[0], self.posicao_robo[1]+1)
            sucessors.append(AspiradorPo2("dir",pos,self.situacao))

        # cim
        if self.posicao_robo[0] - 1 >= 0:
            pos = (self.posicao_robo[0]-1, self.posicao_robo[1])
            sucessors.append(AspiradorPo2("cim",pos,self.situacao))
        # bxo
        if self.posicao_robo[0] + 1 < len(self.situacao):
            pos = (self.posicao_robo[0]+1, self.posicao_robo[1])
            sucessors.append(AspiradorPo2("bxo",pos,self.situacao))
        
        # lmp
        if self.situacao[self.posicao_robo[0]][self.posicao_robo[1]] == 1:
            sit = []
            # for i in range(len(self.situacao)):
            #     l = self.situacao[i]
            #     if i == self.posicao_robo[0]:
            #         l = []
            #         for j in range(len(self.situacao[i])):
            #             if j == self.posicao_robo[1]:
            #                 l.append(0)
            #             else:
            #                 l.append(self.situacao[i][j])
            #     sit.append(l)
            sit = copy.deepcopy(self.situacao)
            sit[self.posicao_robo[0]][self.posicao_robo[1]] = 0

            sucessors.append(AspiradorPo2("lmp", self.posicao_robo, sit))
        

        return sucessors

    def is_goal(self):
        soma = 0
        for i in self.situacao:
            soma += sum(i)
        # print(soma)
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
    state = AspiradorPo2('',(0,0),[[1,1],[1,1]])
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if _name_ == '_main_':
    main()