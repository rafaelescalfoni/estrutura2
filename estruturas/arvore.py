class Arvore:
    def __init__(self, node):
        self.raiz = node
        
    def mostra_profundidade(self):
        visitados = set()
        visitados.add(self.raiz)
        falta_visitar = [self.raiz]
        result = ""
        while falta_visitar:
            vertice = falta_visitar.pop()
            result += str(vertice) + " >> "
            for filho in vertice.prox:
                if filho not in visitados:
                    visitados.add(filho)
                    falta_visitar.append(filho)
        print( result.rstrip(' >> '))    

    def mostra_largura(self):
        # implementar
        return None
 
        
class Node:
    def __init__(self, val):
        self.conteudo = val
        self.prox = []
        
    def adiciona(self, node):
        self.prox.insert(0,node)
    
    def __str__(self):
        return str(self.conteudo)