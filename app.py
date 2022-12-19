from archives_app.conn_MongoDB import toRecordBook
from archives_app.conn_Neo4j import toRecordGraphBook

def app():
    toRecordBook()
    toRecordGraphBook()
app()