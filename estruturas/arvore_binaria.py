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
        self.nodes.append(node)
    
    def cria_no_esq(self, node, node_pai):
        node_pai.esq = node
        self.nodes.append(node)

    def cria_no_dir(self, node, node_pai):
        node_pai.dir = node
        self.nodes.append(node)

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

    # retorna o maior caminho de um no até a folha
    def altura(self, node):
        h1 = 0
        h2 = 0
        if node.esq is not None:
            h1 = self.altura(node.esq) 
        else:
            h1 = -1
        if node.dir is not None:
            h2 = self.altura(node.dir) 
        else:
            h2 = -1
        return 1 + (h1 if h1 > h2 else h2)

    def visita_pre_ordem(self, node):
        result = str(node)
        if node.esq is not None:
            result += " >> " + self.visita_pre_ordem(node.esq)
        if node.dir is not None:
            result += " >> " + self.visita_pre_ordem(node.dir)
        return result
    
    def mostra_profundidade_recursiva(self):
        if (self.raiz is not None):
            caminho = self.visita_pre_ordem(self.raiz)
            print(caminho)
        else:
            print ("Árvore vazia")
    
    def mostra_largura(self):
        node = self.raiz
        fila = [node]
        while fila:
            node = fila.pop()
            print(str(node))
            if node.esq:
                fila.insert(0, node.esq)
            if node.dir:
                fila.insert(0, node.dir)
        
    
    def gera_arvore(self, arquivo):
        result = '{ "elements":{ '
        node = self.raiz
        fila = [node]
        visitados = []
        while fila:
            node = fila.pop()
            coordX, coordY = self.calc_coord(node, visitados)
            visitados.insert(0,[node, coordX, coordY])
            if node.esq:
                fila.insert(0,node.esq)
            if node.dir:
                fila.insert(0, node.dir)
        vertices = ""
        arestas = ""
        while visitados:
            componente_node = visitados.pop()
            vertices += '\n{"data": {"id": ' + str(componente_node[0].conteudo) + '},'
            vertices += '\n    "position": {"x":'+ str(componente_node[1]) + ',\n        "y":'+ str(componente_node[2])+'} },'
            if componente_node[0].esq:
                arestas += '{"data": { "source": ' + str(componente_node[0].conteudo) + ', "target":' + str(componente_node[0].esq.conteudo) +'}},'
            if componente_node[0].dir:
                arestas += '{"data": { "source": ' + str(componente_node[0].conteudo) + ', "target":' + str(componente_node[0].dir.conteudo)+ '}},'
            
        vertices = vertices.rstrip(',')
        arestas = arestas.rstrip(',')
        
        result += '"nodes":[' + vertices + '], "edges":[' + arestas + ']}, '
        
        result += '"data":{"title": "Nova Árvore", "tags": [], "description":""}}'
        
        #path = arquivo
        #file = open(path, "a")
        #file.write(result)
        return result
        
    def calc_percurso(self, source, target):
        tam_path = 0
        no_visitado = source
        while no_visitado:
            if no_visitado == target:
                return tam_path
            if no_visitado.conteudo > target.conteudo:
                if no_visitado.esq:
                    no_visitado = no_visitado.esq
                    tam_path += 1
                else: # nao achou
                    return -1
            else: 
                if no_visitado.dir:
                    no_visitado = no_visitado.dir
                    tam_path += 1
                else: # nao acho
                    return -1
        return tam_path
        
    def calc_coord(self, node, lista):
        for item in lista:
            nivel = self.calc_percurso(self.raiz, node)
            if item[0].esq == node:
                coordX = (nivel+2)/(nivel+1) * (item[1] - 40)
                coordY = item[2] + 30
                return coordX, coordY 
            if item[0].dir == node:
                coordX = (nivel+2)/(nivel+1) * (item[1] + 40)
                coordY = item[2] + 30
                return coordX, coordY 
        return 50, 200
    
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
        self.nodes.append(No(val))
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
        
    def busca_pai(self, val):
        pai = self.raiz
        node = self.busca(val)
        if node:
            while (pai is not None):
                if pai.esq is not None and pai.esq.conteudo == val:
                    return pai
                if pai.dir is not None and pai.dir.conteudo == val:
                    return pai
                if pai.conteudo > val:
                    pai = pai.esq
                else:
                    pai = pai.dir
        return pai
    
    def maior_val_esq(self, node):
        node = node.esq
        maior_node = node
        while node is not None:
            if node.conteudo > maior_node.conteudo:
                maior_node = node
            node = node.dir
        return maior_node
    
    # retorna o maior caminho de um no até a folha
    def altura(self, val):
        node = self.busca(val)
        if node is None:
            return -1
        return self.altura_recursiva(node)
        
    def altura_recursiva(self, node):
        h1 = 0
        h2 = 0
        if node.esq is not None:
            h1 = self.altura_recursiva(node.esq) 
        else:
            h1 = -1
        if node.dir is not None:
            h2 = self.altura_recursiva(node.dir) 
        else:
            h2 = -1
        return 1 + (h1 if h1 > h2 else h2)

    # 1o caso nó folha
    def exclui_folha(self, node):
        # se a folha tb é a raiz
        if self.raiz == node:
            del self.raiz
        else:
            no_pai = self.busca_pai(node.conteudo)
            if no_pai.esq == node:
                no_pai.esq = None
            else:
                no_pai.dir = None
    
    # 2o caso nó interno com apenas uma subárvore
    def exclui_caso_2(self, node):
        no_pai = self.busca_pai(node.conteudo)
        # caso a subárvore existente esteja à esquerda
        # apontar o pai para a subárvore à esquerda
        if node.esq:
            # verificado qual ponteiro do pai apontava para o nó
            # se o pai tem valor maior, usar o ponteiro pai.esq
            # caso contrário, usar o ponteiro pai.dir
            if no_pai.conteudo > node.conteudo:
                no_pai.esq = node.esq
            else:
                no_pai.dir = node.esq
            # caso a subárvore existente esteja à direira
            # apontar o pai para a subárvore à direita
        else:
            # verificado qual ponteiro do pai apontava para o nó
            # se o pai tem valor maior, usar o ponteiro pai.esq
            # caso contrário, usar o ponteiro pai.dir
            if no_pai.conteudo > node.conteudo:
                no_pai.esq = node.dir
            else:
                no_pai.dir = node.dir
        
    def exclui(self, val):
        node = self.busca(val)
        if node is None:
            return -1

        # nó é folha
        if node.is_leaf():
            self.exclui_folha(node)
        # nó interno
        else:
            # 2o caso nó interno com apenas uma subárvore
            if node.esq is None or node.dir is None:
                self.exclui_caso_2(node)
            # 3o caso - nó interno com duas subárvores
            else:
                # pega o maior nó na subárvore da esquerda
                pivot = self.maior_val_esq(node)
#                print(str(pivot.conteudo))
                altura_pivot = self.altura(pivot.conteudo)
                
                no_pai = self.busca_pai(node.conteudo)
                
                # criando o nó substituto
                novo_node = No(pivot.conteudo)

                # se maior_node for folha                
                if altura_pivot == 0:
                    # exclui a pivot folha
                    self.exclui_folha(pivot)
                    
                    novo_node.esq = node.esq
                    novo_node.dir = node.dir
                    
                    if no_pai.conteudo > novo_node.conteudo:
                        no_pai.esq = novo_node
                    else:
                        no_pai.dir = novo_node
                    
                # pivot não é folha   
                else:
                # se maior_node for no interno com uma sub_arvore apenas
                    if pivot.esq is None or pivot.dir is None:
                        
                        pai_pivot = self.busca_pai(pivot.conteudo)
                        pai_pivot.dir = pivot.esq
                        
                        novo_node.esq = node.esq
                        novo_node.dir = node.dir
                        
                        self.exclui_caso_2(pivot)
                        
                        if no_pai.conteudo > novo_node.conteudo:
                            no_pai.esq = novo_node
                        else:
                            no_pai.dir = novo_node

        del node
                

class No:
    def __init__(self, val):
        self.conteudo = val
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.conteudo)
    
    def is_leaf(self):
        return (self.esq is None and self.dir is None)