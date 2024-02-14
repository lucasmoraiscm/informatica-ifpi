from dao import *

class ProdutoController():
    @classmethod
    def salvar(cls, nome, preco, quant, id):
        if len(nome) > 1 and preco > 0 and quant >= 0 and len(id) == 10:
            produto1 = Produtos(nome, preco, quant, id)
            ProdutoDao.salvar(produto1)
            return True
        else:
            return False

class ClienteController():
    @classmethod
    def salvar(cls, nome, cpf, num):
        if len(nome) > 2 and len(cpf) ==11 and (len(num)==10 or len(num)==11):
            cliente1 = Cliente(nome, cpf, num)
            ClienteDao.salvar(cliente1)
            return True
        else:
            return False
