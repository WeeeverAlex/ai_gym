
from aigyminsper.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aigyminsper.search.Graph import State

class ProblemSpecification(State):

    def __init__(self, op, robo, s_esq, s_dir): 
        self.operator = op
        self.posicao = ''
        self.robo = robo
        self.situacao_esq = s_esq
        self.situacao_dir = s_dir
    
    def sucessors(self):
        sucessors = []
        #esq 
        sucessors.append(ProblemSpecification("esq","ESQ",self.situacao_esq,self.situacao_dir))
        #dir
        sucessors.append(ProblemSpecification("dir","DIR",self.situacao_dir,self.situacao_dir))
        #limpar
        if self.posicao == "ESQ":
            sucessors.append(ProblemSpecification("limpar",self.posicao,"LIMPO",self.situacao_dir))
        else:
            sucessors.append(ProblemSpecification("limpar",self.posicao,self.situacao_esq,"LIMPO"))

        return sucessors
                                              

    def is_goal(self):
        if (self.situacao_dir == "LIMPO") and (self.situacao_esq == "LIMPO") and (self.robo == "ESQ"):
            return True
        return False

    
    def description(self):
        return 'Problema da aspirador de pó'
    
    def cost(self):
        return 1
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main():
    print('Busca em profundidade iterativa')
    state = ProblemSpecification('','ESQ','SUJO','SUJO')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()