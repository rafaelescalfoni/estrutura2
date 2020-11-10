class ArvoreBinaria:
    def __init__(self):
        self.nodes = []
        self.raiz = None

    def lista_str(self, lista):
        result = '['
        for item in lista:
            result += str(item) + ', '
        result = result.rstrip(', ')
        result += ']'
        print(result)
        return None

    def cria_no(self, node):
        self.raiz = node
    
    def cria_no_esq(self, node, node_pai):
        node_pai.esq = node

    def cria_no_dir(self, node, node_pai):
        node_pai.dir = node

    def mostra_profundidade(self):
        visitados = set()
        visitados.add(self.raiz)
        falta_visitar = [self.raiz]
        result = ""
        while falta_visitar:
            vertice = falta_visitar.pop()
            result += str(vertice) + " >> "
            
            filho = vertice.dir
            if (filho is not None):
                if filho not in visitados:
                    visitados.add(filho)
                    falta_visitar.append(filho)

            filho = vertice.esq
            if (filho is not None):
                if filho not in visitados:
                    visitados.add(filho)
                    falta_visitar.append(filho)
                    
        print( result.rstrip(' >> '))    

    def mostra_largura(self):
        # implemente aqui seu codigo
        return None
    
class ArvoreBinariaBusca(ArvoreBinaria):
    
    def add_no (self, val, pai):
        val_pai = pai.conteudo
        if (val < val_pai):
            if (pai.esq is None):
                pai.esq = No(val)
                return self.raiz
            self.add_no(val, pai.esq)
        else:
            if (pai.dir is None):
                pai.dir = No(val)
                return self.raiz
            self.add_no(val, pai.dir)
        return None
    
    def adiciona(self, val):
        if(self.raiz is None):
            self.raiz = No(val)
            return self.raiz
        self.add_no(val, self.raiz)
    
    def busca(self, val):
        no = self.raiz
        while (no is not None):
            if (no.conteudo == val):
                return no; 
            else:
                if (no.conteudo > val):
                    no = no.esq;
                else:
                    no = no.dir;
        return None;
    
class No:
    def __init__(self, val):
        self.conteudo = val
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.conteudo)