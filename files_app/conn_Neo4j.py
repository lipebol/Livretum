from neo4j import GraphDatabase
import json
import os


def queryNeo4j(query):
    file = open('book.json')
    docjson = json.load(file)
    return query.run("""
    WITH $docjson as data
    UNWIND  data.título AS livro
    MERGE (p:Autor {nome: data.autor})
    MERGE (c: Coleção {nome: data.coleção})
    MERGE (b:Livro {título: livro})
    SET b.id_MongoDB = data._id, b.páginas = data.páginas, b.idioma = data.idioma, b.dt_pub = data.data_da_publicação
    MERGE (e:Editora {nome: data.editora})
    MERGE (p)-[:ESCREVEU]->(b)
    MERGE (e)-[:PUBLICOU]->(b)
    MERGE (b)-[:COLEÇÃO]->(c)
    """, docjson = docjson
    )


def toRecordGraphBook():
    print("\n[Neo4j] \n")
    userNeo4j = input("  Usuário: ")
    passNeo4j = input("  Senha: ")
    hostNeo4j = input("  Host: ")
    CONNECTION_STRING = "neo4j://{}:7687".format(hostNeo4j)
    connection = GraphDatabase.driver(CONNECTION_STRING, auth=(userNeo4j, passNeo4j))
    with connection.session() as session:
        session.execute_write(queryNeo4j)
        session.close()
    with open('book.json','w') as cnt:
        pass
    os.remove('book.json')

    return print("\n Criado com Sucesso!\n")