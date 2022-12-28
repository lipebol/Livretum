from py2neo import Graph
import json


def toRecordGraphBook():
    print("\n[Neo4j] \n")
    userNeo4j = input("  Usuário: ")
    passNeo4j = input("  Senha: ")
    hostNeo4j = input("  Host: ")
    URL = "bolt://{}:7687".format(hostNeo4j)
    graph = Graph(URL, auth=(userNeo4j, passNeo4j))
    file = open('book.json')
    docjson = json.load(file)
    query = graph.run("""
    WITH $docjson as data
    UNWIND  data.autor AS autor
    MERGE (p:Autor {nome: autor})
    MERGE (c: Coleção {nome: data.coleção})
    MERGE (b:Livro {título: data.título})
    SET b.id_MongoDB = data._id, b.páginas = data.páginas, b.idioma = data.idioma, b.dt_pub = data.data_da_publicação
    MERGE (e:Editora {nome: data.editora})
    MERGE (p)-[:ESCREVEU]->(b)
    MERGE (e)-[:PUBLICOU]->(b)
    MERGE (b)-[:COLEÇÃO]->(c)
    """, docjson = docjson
    )

    return print("\nCriado com Sucesso!\n")