from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()
db = client['sessions']

def user_signup(user_info):
	#Here we have to save the user_info dict inside mongo
	
	results = db['users'].insert_one(user_info)
	return True

def search_user_by_username(username):
	filter_query = {'username' : username}
	results = db["users"].find(filter_query)
	
	if(results.count() > 0):
		return results.next()
	
	else:
		return None

def search_user_by_user_id(user_id):
	filter_query = {'_id' : ObjectId(user_id)}
	results = db["users"].find(filter_query)
	
	if(results.count() > 0):
		return results.next()
	
	else:
		return None

def seller_products(user_id):
	ans =[]
	filter_query = {'seller_id' : user_id}
	results = db["products"].find(filter_query)
	for post in results:
		ans.append(post)
	return ans

def buyer_products():
	ans =[]
	#filter_query = {'buyer_id' : user_id}
	results = db['products'].find({})
	for post in results:
		ans.append(post)
	return ans

def Product_addition(product_info):
	#saves the products inside mongo
	results = db['products'].insert_one(product_info)
	return True

def search_products_in_page(search):

	result=[]
	filter_query = {"product name" : search}
	result = db['products'].find(filter_query)
	return result

def check_user(username):
	filter_query = {'username' :username}
	results = db['users'].find(filter_query)

	if(results.count()>0):
		return results.next()
	else:
		return None

def cart_details(user_id):
	results =[]
	
	filter_query1 = {"_id":ObjectId(user_id)}
	result = db["users"].find_one(filter_query1)
	cart_list=result["cart_details"]

	for item in cart_list:
		filter_query2 = {"_id":ObjectId(item)}
		results.append(db["products"].find_one(filter_query2))
	return results

def update_cart_details(user_id,product_id):
	
	result = db["users"].update({"_id":ObjectId(user_id)},{"$addToSet":{"cart_details":{"$each":[product_id]}}})
	return True 	
