#Sql da tabela imoveis
SQL_CRIA_IMOVEL = 'INSERT into imoveis (ID_CORR, ID_PROP, ID_TIPO, FINALIDADE, ID_CIDADE, ID_BAIRRO, ENDERECO, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS, BANHEIRO, QUARTOS, GARAGEM)' \
                  ' values (%s, %s, %s, %s, %s, %s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)'

SQL_DELETA_IMOVEL = 'delete from imoveis where ID_IMOB = %s'

SQL_ATUALIZA_IMOVEIS = 'UPDATE imoveis SET ID_CORR=%s,ID_PROP=%s,ID_TIPO=%s,FINALIDADE=%s,ID_CIDADE=%s,ID_BAIRRO=%s,ENDERECO=%s, AREA=%s, DETALHES=%s,'\
                       'VALOR_IMOVEL=%s,VALOR_VENDA=%s,STATUS=%s, PORCENTAGEM=%s, HONORARIOS=%s,BANHEIRO=%s,QUARTOS=%s, GARAGEM=%s where ID_IMOB=%s'

'''SQL_BUSCA_LISTA_IMOB = 'SELECT ID_IMOB, ID_CORR, ID_PROP, SINGLA, TIPO, FINALIDADE, BAIRRO, QUADRA, LOTE, AREA, DETALHES,' \
                  ' VALOR_IMOVEL,VALOR_VENDA, STATUS, PORCENTAGEM, HONORARIOS from imoveis'
'''

SQL_BUSCA_LISTA_IMOB = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP  inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                       'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO'

SQL_BUSCA_IMOB_ID = 'select * from imoveis inner join proprietarios on imoveis.ID_PROP = proprietarios.ID_PROP inner join tipos on imoveis.ID_TIPO = tipos.ID_TIPO ' \
                    'join cidade on cidade.ID_CID = imoveis.ID_CIDADE join bairro on bairro.ID_BAIRRO = imoveis.ID_BAIRRO where imoveis.ID_IMOB = %s'

#Sql da tabela propeitarios
SQL_DELETA_PROPRIETARIO = 'delete from proprietarios where ID_PROP = %s'

SQL_CRIA_PROPRIETARIO = 'INSERT into proprietarios (NOME, CPF, RG, ENDERECO, TELEFONE, EMAIL) values (%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_PROPRIETARIO = 'UPDATE proprietarios SET NOME=%s, CPF=%s, RG=%s, ENDERECO=%s, TELEFONE=%s, EMAIL=%s  where ID_PROP=%s'

SQL_BUSCAR_LISTA_PROP = 'SELECT ID_PROP, NOME, CPF, RG, ENDERECO,TELEFONE,EMAIL from proprietarios'

#Sql da tabela corretores
SQL_CRIA_CORRETORES = 'INSERT into corretores (USUARIO,EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

SQL_ATUALIZA_CORRETORES = 'UPDATE corretores SET USUARIO=%s,EMAIL=%s,NOME=%s,IMOBIL=%s,CRECI=%s,CELULAR=%s,CPF=%s,ENDERECO=%s,SENHA=%s  where ID_CORR=%s'

SQL_BUSCA_LISTA_CORRETORES = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA from corretores'

SQL_BUSCA_CORR_ID = 'SELECT ID_CORR, USUARIO, EMAIL,NOME,IMOBIL,CRECI,CELULAR,CPF,ENDERECO,SENHA from corretores where USUARIO=%s'

#TIPOS
SQL_CRIA_TIPOS = 'INSERT into tipos (ID_TIPO,TIPO) values(%s,%s)'
SQL_LISTA_TIPOS = 'SELECT * FROM tipos'

#CIDADE E BAIRRO
SQL_CRIA_CIDADE = 'INSERT into cidade (ID_CID,CIDADE) values(%s,%s)'
SQL_LISTA_CIDADE = 'SELECT * FROM cidade'
SQL_CRIA_BAIRRO = 'INSERT into bairro (ID_BAIRRO,BAIRRO,CIDADE_ID_CID) values(%s,%s, %s)'
SQL_LISTA_BAIRRO = 'SELECT * FROM bairro inner join cidade on bairro.CIDADE_ID_CID = cidade.ID_CID'