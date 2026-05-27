from models.livro import Livro
import json
class LivroRepository:

    def __init__(self,caminho_arquivo='data/livros.json'):

        self.caminho_arquivo=caminho_arquivo


    def salvar(self,livros:list):
        dados=[]
        for livro in livros:
            dados.append({
                'autor':livro.autor,
                'titulo':livro.titulo,
                'status':livro.status
            }

            )

        with open(self.caminho_arquivo,'w',encoding='utf-8') as arquivo:
            json.dump(dados,arquivo,ensure_ascii=False,indent=4)


    def carregar(self):
        dados=[]
        livros=[]
        try:
            with open(self.caminho_arquivo,'r', encoding='utf-8') as arquivo:
                dados=json.load(arquivo)
            
            for dado in dados:
                livro=Livro(autor=dado['autor'],titulo=dado['titulo'],status=dado['status'])
                livros.append(livro)
        except FileNotFoundError:
            return []
        return livros