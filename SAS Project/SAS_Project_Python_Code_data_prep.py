import pandas as pd

data = pd.read_csv('/Users/tapas/Downloads/Oil/SRG_Group_Survey_Data.csv',header=0)

data['Q30rav_time_spend_grocery'] = data['Q30rav'].map(
    {'Agree somewhat': 1,
     'Strongly agree': 2,
     'Disagree somewhat':0,
     'Strongly disagree':-1})

data['Q30rav_time_spend_grocery'].value_counts(normalize=True)

def code_ethnicity(data):
    if (data['D7r1'] == 'White /Anglo/Caucasian') & (data['D7r2'] == 'Hispanic'):
        return 'Hispanic_White'
    if data['D7r1'] == 'White /Anglo/Caucasian':
        return 'White'
    if data['D7r2'] == 'Hispanic':
        return 'Hispanic'
    if data['D7r3'] == 'Black/African American':
        return 'African_American'
    if data['D7r4'] == 'Asian/Oriental':
        return 'Asian/Oriental'
    if data['D7r5'] == 'American Indian':
        return 'American_Indian'
    if data['D7r6'] == 'Other ( please specify)':
        return 'other'
    if data['D7r7'] == 'Decline to answer':
        return 'Decline_to_answer'

data['ethnicity'] = data.apply(lambda x: code_ethnicity(x), axis=1)

data['Price_Sense'] = data['Q30rbb']


data['Q30rbb_food_price_shopper'] = data['Q30rbb'].map(
    {'Agree somewhat': 1,
     'Strongly agree': 1,
     'Disagree somewhat':0,
     'Strongly disagree':0})


def map_dinner_loc(x):
    if x == 'Ate at home':
        return 'home'
    elif x == 'Ate at a restaurant':
        return 'restaurant'
    elif x == 'Ate at someone else\'s house':
        return 'others house'
    else: return 'No info'

data['Q10r1_dinner_where_lnight'] = data['Q10r1'].map(lambda x: map_dinner_loc(x))
data['Q10r2_dinner_where_before_lnight'] = data['Q10r2'].map(lambda x: map_dinner_loc(x))   
data['Q10r3_dinner_two_nights_ago'] = data['Q10r3'].map(lambda x: map_dinner_loc(x)) 
data['Q10r4_dinner_three_nights_ago'] = data['Q10r4'].map(lambda x: map_dinner_loc(x))  


data['hS3_age_group'] = data['hS3']

def isStressed(x):
    if x['Q1ra'] in ['Agree Some what','Strongly Agree']:
        return 1
    else:
        return 0

def isStressed2(x):
    if x['Q1rb'] in ['Agree Some what','Strongly Agree']:
        return 1
    else:
        return 0

data['Q1ra_is_stressed'] = data.apply(lambda x: isStressed(x),axis=1)
data['Q1rb_work_too_much'] = data.apply(lambda x: isStressed2(x),axis=1)


#1. Which age groups are more stressed
data.groupby(['hS3_age_group'])['Q1ra_is_stressed'].mean().plot()

data['total_time_spent_cooking'] = data['Q13'] + data['Q14']

data['Q13_time'] = data['Q13'].map({
'Less than five minutes':5,
'6-15 minutes':10.5,    
'16-30 minutes':23,
'31-45 minutes':38,
'46-60 minutes':53,
'Over one hour':75})

data['Q14_time'] = data['Q14'].map({
'Put something in the crock pot in the morning':0,
'Less than five minutes':5,
'6-15 minutes':10.5,    
'16-30 minutes':23,
'31-45 minutes':38,
'46-60 minutes':53,
'Over one hour':75})

data['total_time_spent_cooking'] = data.apply(lambda x: str(x['Q13_time'] + x['Q14_time']) + ' minutes', axis=1)

data['total_time_spent_cooking_int'] = data.apply(lambda x: x['Q13_time'] + x['Q14_time'], axis=1)

data['total_time_spent_cooking_int'].mean()


def last_dinner(x):
    if x['Q12ra'] == 'Plated entrée - a meal that could include a protein, a side dish (like a vegetable) and a starch (like potatoes or rice':
        return 'Plated_entrée'
    elif x['Q12rb'] == 'Pasta (does not include macaroni & cheese)':
        return 'Pasta'
    elif x['Q12rc'] == 'Pizza (not delivered)':
        return 'Pizza'
    elif x['Q12rd'] == 'Salad':
        return 'Salad'
    elif x['Q12re'] == 'Sandwich - lunchmeat, grilled cheese, BLTs, etc.':
        return 'Sandwich'
    elif x['Q12rf'] == 'From the grill - burgers, hot dogs, brats or smoked sausage in a bun':
        return 'Grilled_Products'
    elif x['Q12rg'] == 'Traditional favorites - meatloaf, roasts, etc.':
        return 'Meatloafs_Roasts'
    elif x['Q12rh'] == 'Kids favorites - corn dogs, macaroni & cheese, chicken nuggets':
        return 'CornDogs_Mac&Cheese_chickenNuggets'
    elif x['Q12ri'] == 'Casseroles':
        return 'Casseroles'
    elif x['Q12rj'] == 'Soups, stews, chili or gumbo':
        return 'Soups_stews_chili_gumbo'
    elif x['Q12rk'] == 'Crockpot meal':
        return 'Crockpot_meal'
    elif x['Q12rl'] == 'Meatless Meal - baked potatoes, vegetable sauté':
        return 'Meatless_Meal_baked_potatoes_or_vegetable_sauté'
    elif x['Q12rm'] == 'Breakfast foods - eggs, cereal, waffles, etc.':
        return 'Breakfast_foods-eggs_cereal_waffles_etc'
    elif x['Q12rn'] == 'Frozen complete meal kit - frozen or refrigerated bagged meals (e.g. Bertolli, P.F. Changs)':
        return 'Frozen_Meal'
    elif x['Q12ro'] == 'Shelf stable meal starter kit (e.g. Hamburger Helper)':
        return 'Shelf_stable_meal_starter_kit'
    elif x['Q12rp'] == 'Refrigerated meal starter kit (e.g. sliced pre-cooked chicken, other pre-cooked meats':
        return 'Refrigerated_meal_starter_kit'
    elif x['Q12rq'] == 'Heat and eat meal - frozen entrees (e.g. Lean Cuisine, Stouffer\'s':
        return 'Heat_and_eat_meal-frozen_entrees'
    elif x['Q12rr'] == 'Snack Food or Dessert Food as Dinner - ate snacks or desserts instead of making dinner':
        return 'Snack_or_Dessert_instead_of_dinner'
    elif x['Q12rs'] == 'Sushi':
        return 'Sushi'
    elif x['Q12rt'] == 'Italian foods - chicken parmesan, pesto':
        return 'Italian_foods-chicken_parmesan_pesto'
    elif x['Q12ru'] == 'Asian foods - Chinese, Thai etc.':
        return 'Asian_foods'
    elif x['Q12rv'] == 'Mexican food - tacos, burritos, quesadilla, etc.':
        return 'Mexican_food'
    elif x['Q12rx'] == 'Latin food (non-Mexican) - Cuban, South American etc.':
        return 'Latin_Food'
    elif x['Q12ry'] == 'Indian food - Chicken Tikka, Chana Masala, Saag Paneer etc.':
        return 'Indian_food'
    elif x['Q12raa'] == 'Fast Food - food from any fast food restaurant':
        return 'Fast_Food_Restaurant'
    elif x['Q12rbb'] == 'Carry Out or Delivery Pizza':
        return 'Carry_Out_or_Delivery_Pizza'
    elif x['Q12rcc'] == 'Ate Food from a Fast Casual Restaurant - order food at a counter, no wait staff, no tips left such as Chipotle, Panera,':
        return 'Fast_Casual'
    elif x['Q12rdd'] == 'Ate at a Casual Dining Restaurant - order from the waiter or waitress such as Chili\'s or Applebee\'s':
        return 'Casual Dining'
    elif x['Q12ree'] == 'Ate at a local restaurant':
        return 'local_restaurant'
    elif x['Q12rff'] == 'Ate at a fine dining restaurant':
        return 'fine_dining_restaurant'
    elif x['Q12rgg'] == 'Ate prepared food from the grocery store - either at the grocery store or take away':
        return 'grocery_store_or_take_away'
    elif x['Q12rhh'] == 'Other (please specify):':
        return 'Others'
    


data['last_remmbered_dinner'] = data.apply(lambda x: last_dinner(x),axis=1)


def restaurant_type(x):
    if x['Q12raa'] == 'Fast Food - food from any fast food restaurant':
        return 'Fast_Food_Restaurant'
    elif x['Q12rbb'] == 'Carry Out or Delivery Pizza':
        return 'Carry_Out_or_Delivery_Pizza'
    elif x['Q12rcc'] == 'Ate Food from a Fast Casual Restaurant - order food at a counter, no wait staff, no tips left such as Chipotle, Panera,':
        return 'Fast_Casual'
    elif x['Q12rdd'] == 'Ate at a Casual Dining Restaurant - order from the waiter or waitress such as Chili\'s or Applebee\'s':
        return 'Casual Dining'
    elif x['Q12ree'] == 'Ate at a local restaurant':
        return 'local_restaurant'
    elif x['Q12rff'] == 'Ate at a fine dining restaurant':
        return 'fine_dining_restaurant'
    elif x['Q12rgg'] == 'Ate prepared food from the grocery store - either at the grocery store or take away':
        return 'grocery_store_or_take_away'
    elif x['Q12rhh'] == 'Other (please specify):':
        return 'Others'
    else:
        return 'At-home?'


data['type_of_restaurant'] = data.apply(lambda x: restaurant_type(x),axis=1)



def dinner_with(x):
    if (x['Q16ra'] > 0) :
        if (x['Q16rb'] >0) | (x['Q16rc'] >0) | (x['Q16rd'] >0):
            return 'Significant_other_and_children'
        else:
            return 'Significant_other'
    elif x['Q16rb'] > 0:
        return 'Children_aged_13_18'
    elif x['Q16rc'] > 0:
        return 'Children_aged_5_12'
    elif x['Q16rd'] > 0:
        return 'Children_under_5'
    elif x['Q16re'] > 0:
        return 'extended_family'
    elif x['Q16rf'] > 0:
        return 'male_friends'
    elif x['Q16rg'] > 0:
        return 'female_friends'
    elif x['Q16rh'] > 0:
        return 'co-workers'
    elif x['Q16ri'] > 0:
        return 'other_children'
    elif x['Q16rj'] > 0:
        return 'other_people'
    elif x['Q16rk'] > 0:
        return 'ate_alone'


data['dinner_with'] = data.apply(lambda x: dinner_with(x),axis=1)


g_map = {
    'Female': 1,
    'Male': 0
}
data['Gender'] = data['S2'].map(g_map).astype(int)

m_map = {
    'Yes, married or living with partner': 1,
    'No, not married and not living with partner': 0
}
data['D3'].replace(' ', 'Yes, married or living with partner', inplace = True)

data['Married'] = data['D3'].map(m_map).astype(int)


e_map = {
    'Some high school or less' : 0,
    'Graduated high school':1, 
    'Trade or technical school':2, 
    'Some college or Associate degree':3,
    "Graduated college/Bachelor's degree":4,
    "Attended graduate school or received Advanced degree (Master's, Ph.D.)" : 5,
}
data['D5'] = data['D5'].replace('Decline to answer', data['D5'].value_counts().idxmax())
data['Education'] = data['D5'].map(e_map).astype(int)

data['D6'] = data['D6'].replace('Decline to answer', data['D6'].value_counts().idxmax())

from collections import defaultdict
in_dd = defaultdict()
for i, key in enumerate(data['D6'].unique()):
    in_dd[key] = i
    
data['Income'] = data['D6'].map(in_dd).astype(int)


### Decline to answer': 6 to the most frequent value
data['D8'] = data['D8'].replace('Decline to answer', data['D8'].value_counts().idxmax())

from collections import defaultdict
in_dd = defaultdict()
for i, key in enumerate(data['D8'].unique()):
    in_dd[key] = i
    
data['Work'] = data['D8'].map(in_dd).astype(int)



p_map = {'Agree somewhat': 1,
         'Strongly agree': 2,
         'Disagree somewhat':0,
         'Strongly disagree':-1}

data['Q30rae_prefer_natural_product'] = data['Q30rae'].map(p_map)
data['Q30ram_prefer_store_brand'] = data['Q30ram'].map(p_map)
data['Q30rbm_prefer_taste_to_health'] = data['Q30rbm'].map(p_map)
data['Q30rbc_prefer_quality'] = data['Q30rbc'].map(p_map)
data['Q30rao_calorie_conscious'] = data['Q30rao'].map(p_map)

def create_y_label(x):
    profile_1 = x['Q30rbb_food_price_shopper'] + x['Q30ram_prefer_store_brand'] + x['Q30rbm_prefer_taste_to_health']
    profile_2 = x['Q30rbc_prefer_quality']+x['Q30rae_prefer_natural_product']+x['Q30rao_calorie_conscious']
    
    if profile_1 > profile_2:
        return "Tasty_Pizza"
    elif profile_1 < profile_2:
        return "Healthy_sandwich"
    else: 
        return "Unsure"

data['choice'] = data.apply(lambda x: create_y_label(x),axis=1)


data.to_csv('/Users/tapas/Downloads/Oil/SRG_Group_data_2.csv')


