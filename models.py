class imovel:
    def __init__(self, sigla, tipo, finalidade, bairro, quadra, lote,area, descricao, valor_imovel, status, porcentagem, proprietario_id=None, corretor_id=None, imob_id=None, valor_venda=None,honorarios=None):
        self._id = imob_id
        self._sigla = sigla
        self._tipo= tipo
        self._finalidade = finalidade
        self._bairro = bairro
        self._quadra = quadra
        self._lote = lote
        self._area = area
        self._descricao = descricao
        self._valor_imovel = valor_imovel
        self._valor_venda = valor_venda
        self._status = status
        self._porcentagem = porcentagem
        self._honorarios = honorarios
        self._proprietario_id = proprietario_id
        self._corretor_id = corretor_id

    def get_area(self):
        self._area = self._area.replace('m','')
        return float(self._area)

    def get_percentagem(self):
        self._porcentagem = self._porcentagem.replace('%','')
        return float(self._porcentagem)

    def get_valor_imovel(self):
        self._valor_imovel = self._valor_imovel.replace('.','')
        return float(self._valor_imovel)

    def get_honorarios(self):
        self._honorarios = (self.get_percentagem() * self.get_valor_imovel())/100
        return float(self._honorarios)

    def get_valor_venda(self):
        self._valor_venda = (self.get_valor_imovel() + ((self.get_percentagem() * self.get_valor_imovel())/100))
        return float(self._valor_venda)
    def imprimir(self):
        print('{} - {}'.format(self._bairro,self._tipo))

class Proprietario:
    def __init__(self, nome, cpf, rg, endereco, telefone, email, id = None ):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._telefone = telefone
        self._email = email

    def imprimir(self):
        print('{} - {}'.format(self._nome,self._telefone))

class Corretores:
    def __init__(self, usuario, email, nome, imobil, creci, celular, cpf, endereco, senha, id_corr=None):
        self._id_corr = id_corr
        self._usuario = usuario
        self._email = email
        self._nome = nome
        self._imobil = imobil
        self._creci = creci
        self._celular = celular
        self._cpf = cpf
        self._endereco =endereco
        self._senha = senha

#classe para receber inner join da tabela imovel e proprietario do banco de dados
class Imob_Prop(imovel,Proprietario):
    def __init__(self, sigla, tipo, finalidade, bairro, quadra, lote,area, descricao,
                 valor_imovel, status,porcentagem,proprietario_id, corretor_id, imob_id,
                 valor_venda,honorarios,nome, cpf, rg, endereco, telefone, email, id):
        imovel.__init__(self, sigla, tipo, finalidade, bairro, quadra, lote,area, descricao, valor_imovel, status,
                        porcentagem, proprietario_id, corretor_id, imob_id, valor_venda,honorarios)
        Proprietario.__init__(self,nome, cpf, rg, endereco, telefone, email,id)