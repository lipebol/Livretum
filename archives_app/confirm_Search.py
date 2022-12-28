from archives_app.search_API import data, n

def receiverSearch():
    selector = data['items'][n]['volumeInfo']
    if 'subtitle' not in selector:
        print("\n   Título: ", data['items'][n]['volumeInfo']['title'])
    else:
        print("\n   Título: ", data['items'][n]['volumeInfo']['title'],"-", data['items'][n]['volumeInfo']['subtitle'])
    if 'authors' not in selector:
        authors = None
        print("   Autor(es): ", authors, "\n")
    else:
        authors = ", ".join(data['items'][n]['volumeInfo']['authors'])
        print("   Autor(es): ", authors, "\n")
    confirmSearch()

def confirmSearch():
    global n, URL_book
    confirm_book = input(" É esse o livro? (s/n): ")
    if confirm_book == "s":
        URL_book = data['items'][n]['selfLink'] + "?fields=volumeInfo"
    elif confirm_book == "n":
        n += 1
        receiverSearch()
    else:
        print("\n Opção Inválida. \n")
        confirmSearch()

receiverSearch()