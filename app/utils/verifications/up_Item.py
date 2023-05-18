

def upItem(ack_item, categories, rating, price, collection):

    up_categories = ack_item["categoria(s)"] == categories
    if up_categories == False:
        ack_categories = ack_item["categoria(s)"]
        down = {
            "categoria(s)": ack_categories
        }
        up = {
            "$set": {"categoria(s)": categories}
        }
        upCategories = collection.update_one(down, up)
        if upCategories.modified_count == 1:
            up_categories = "categories"
    up_rating = ack_item["avaliação"] == rating
    if up_rating == False:
        ack_rating = ack_item["avaliação"]
        down = {
            "avaliação": ack_rating
        }
        up = {
            "$set": {"avaliação": rating}
        }
        upRating = collection.update_one(down, up)
        if upRating.modified_count == 1:
            up_rating = "rating"
    up_price = ack_item["preço"] == price
    if up_price == False:
        ack_price = ack_item["preço"]
        down = {
            "preço": ack_price
        }
        up = {
            "$set": {"preço": price}
        }
        upPrice = collection.update_one(down, up)
        if upPrice.modified_count == 1:
            up_price = "price"
    
    if up_categories == up_rating == up_price:
        return "No Update"
    else:
        return "Update"


