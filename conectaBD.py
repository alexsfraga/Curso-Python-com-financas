import cx_Oracle as cx
cx.init_oracle_client(lib_dir=r"C:\DEV_WorkSpace\Rep_Python\env_python\cli_oracle\instantclient_19_8")

def connectBd():
    host_name = "192.168.56.3"
    port_number = "1521"
    service_name = "orcl"
    pass_1 = "useraction"
    user = "useraction"
    dbschema = "BD_ACOES"
    host = host_name + ":" + port_number + "/" + service_name

    conn = cx.connect(user, pass_1, host , encoding="UTF-8")
    #print(conn)
    #cursor = conn.cursor()
    return conn

def select(psql):
    #psql = "select * from ticket"
    conn = connectBd()
    cursor = conn.cursor()
    print(cursor)

    for row in cursor.execute(psql):
        print(row)

    conn.close()


def insertToBd(sigla, tipo, bolsa):
    conn = connectBd()
    cursor = conn.cursor()
    #sql = ("insert into ticket(id_ticket, nome, tipo, pais) VALUES(SEQ_IDTICKET.nextval,'EGIE3.SA','ON','BRASIL')")
    p1 = "','"
    psql = "insert into acoes(id_acao, sigla, tipo, bolsa) VALUES(SEQ_IDACAO.nextval,'"+sigla+p1+tipo+p1+bolsa+"')"
    print(psql)
    cursor.execute(psql)
    cursor.execute("commit")

def getCursor(psql):
    conn = connectBd()
    cursor = conn.cursor()
    return cursor

#insertToBd("PG","ON","NYSE")
#select()

def geraSqlInsert(nome_tabela, dados):
    sql_insert = 'insert into ' + nome_tabela + '('
    sql_str_campo = ''
    sql_str_valor = ''

    for p_campo, p_valor in dados.items():
        sql_str_campo = sql_str_campo + p_campo + ','
        sql_str_valor = sql_str_valor + "'" + str(p_valor) + "',"
    sql = sql_insert + sql_str_campo[:-1] + ') values(' + sql_str_valor[:-1] + ')'
    return sql

def insertCotacoes(id_sigla, pcotacao):
    conn = connectBd()
    cursor = conn.cursor()
    dados = {}
    print('print pcotacao = »»»» ',pcotacao)
    for t in pcotacao:
        dic1 = dict(list(pcotacao)[list(pcotacao).index(t)])
        print(dic1)
        for p_data, p_open, p_high, p_low, p_close, p_adj_close, p_volume, p_dividend_amount, p_split in dic1:
        #for x in lst1:
            print('print teste »»' ,p_data,p_close)
            #print(list(dic1)[list(dic1).index(x)], ' = ',dic1[x])
            """dados = {'ID_TICKET': id_ticket,
                      'DATA_COTACAO': p_data,
                      'HIGH': p_high,
                      'LOW': p_low,
                      'OPEN': p_open,
                      'CLOSE': p_close,
                      'VOLUME': p_volume,
                      'ADJ_CLOSE': p_adj_close
            }"""

    print('print dados = »»»» ',dados)
    sql = geraSqlInsert('cotacao_diaria', dados)
    try:
        print(sql)
        #cursor.execute(sql)
    except Exception as err:
        print(err)
    #conn.commit()

    """
    {
     'data': '2020-10-23',
     'open': '82.2500',
     'high': '83.2600', 
     'low': '80.6400',
     'close': '81.6700',
     'adjusted close': '81.6700',
     'volume': '8068300',
     'dividend amount': '0.0000',
     'split coefficient': '1.0'
     }
    """