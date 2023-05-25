

def upItem(ack_item, categories, rating, price, collection):
    
    locate = {
        '_id': ack_item['_id']
        }
    up_categories = ack_item['categoria(s)'] == categories
    if up_categories == False:
        up = {
            "$set": {'categoria(s)': categories}
        }
        upCategories = collection.update_one(locate, up)
        if upCategories.modified_count == 1:
            up_categories = "categories"
    up_rating = ack_item['avaliação'] == rating
    if up_rating == False:
        up = {
            "$set": {'avaliação': rating}
        }
        upRating = collection.update_one(locate, up)
        if upRating.modified_count == 1:
            up_rating = "rating"
    up_price = ack_item['preço'] == price
    if up_price == False:
        up = {
            "$set": {'preço': price}
        }
        upPrice = collection.update_one(locate, up)
        if upPrice.modified_count == 1:
            up_price = "price"
    
    if up_categories == up_rating == up_price:
        return "No Update"
    else:
        return "Update"


