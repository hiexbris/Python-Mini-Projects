import pandas as pd
from Graph import Grapher

file = pd.read_excel(r'C:\Users\A-Team\Downloads\Final (8).xlsx', sheet_name=None, header=None) #LINK FOR EXCEL FILE

graph = Grapher(file)
no_of_brands = 7 # put 0 if market share is given
cap = 0

# # For market share:
# market_share = graph.branddata_percent(0, no_of_brands, 3)
# print(market_share)

# #For Ingredients
# ingredients = graph.ingredient(0, no_of_brands)
# print(ingredients)
#
# #For Benefits
# benefits = graph.benefits(0, no_of_brands)
# print(benefits)
#
# #For Claims
# claims = graph.claims(0, no_of_brands)
# print(claims)

#For Ingredients X Benefits
ingredientsxbc = graph.benefits_with_ingredients()
print(ingredientsxbc)

#For Ingredients X Claims
ingredientsxclaims = graph.claims_with_ingredients()
print(ingredientsxclaims)
#
# #Prices By Top Brands
# prices = graph.branddata(cap, no_of_brands, 4) #the cap or 0 signifies the market share the client wants
# print(prices)
#
# #MRP By Top Brands
# mrp = graph.branddata(cap, no_of_brands, 5)
# print(mrp)
#
# #Weight By Top Brands
# Weight = graph.branddata(cap, no_of_brands, 7)
# print(Weight)
#
# #Average Discount By Top Brands
# discount = graph.branddata_percent(cap, no_of_brands, 6)
# print(discount)
#
# #Prices Per Unit wieght By Top Brands--> oz
# unit_weight_oz = graph.branddata(cap, no_of_brands, 8)
# print(unit_weight_oz)
#
# #Prices Per Unit wieght By Top Brands--> ml
# unit_weight_ml = graph.branddata(cap, no_of_brands, 9)
# print(unit_weight_ml)
#
# #price band
# price_band = graph.band_new(0)
# print(price_band)
#
# #Wieght Band
# weight_band = graph.band_new(15)
# print(weight_band)
#
# #MRP Band
# MRP_band = graph.band_new(5)
# print(MRP_band)
#
# #Discount Band
# discount_band = graph.band_new(10)
# print(discount_band)
#
# #Price Per Weight Band-->oz
# price_weight_oz = graph.band_new(20)
# print(price_weight_oz)
#
# #Price Per Weight Band-->oz
# price_weight_ml = graph.band_new(25)
# print(price_weight_ml)