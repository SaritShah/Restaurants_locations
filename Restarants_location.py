#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


os.chdir(r"C:\Users\sarit\Documents\Careerera\Own Practise")


# In[3]:


import chardet

with open("Restaurants.csv", 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']

df = pd.read_csv("Restaurants.csv", encoding=encoding)


# In[4]:


df


# In[5]:


df.shape


# In[6]:


pd.set_option('display.max_columns', None)


# In[7]:


print(df)


# In[23]:


df


# In[14]:


import pandas as pd

# Create a DataFrame from the provided dataset
df1=df

# Define category filters

import pandas as pd

# Create a DataFrame from the provided dataset
df1 = pd.DataFrame({'Restaurant': ['GO AGAIN!!', 'Hutong', 'Gaucho', 'Mint leaf', 'Chai Ki', 'Darbaar', 'Dishoom', 'Roti Chai', 'Quaglino',
    'Hakkasan', 'Tarshish', 'China tang', 'The iskelé', 'Stk', 'HSandCO', 'Mahiki (Cocktail)', 'Madison',
    'Coppa Club', 'Thai Square', 'Hiadilao Hot Pot', 'Jw steakhouse', 'Casa do Frango', 'The meat co',
    'Masala Canteen', 'Dinerama (shut down :( )', 'Sticks’n’sushi', 'Scarlet Rasoi', 'Bocconcino',
    'Bright courtyard', 'Cat tre', 'Kricket', 'Dim t', 'Booma', 'circolo popolare', 'AOK', 'Kinkao (Thai)',
    'Cicchetti', 'Bindi Green (bottomless Brunch)', 'Aqua Kyoto', 'Oka restaurant (sushi)', 'Nabrasa Express',
    'Cardamom Black', 'Izgara restaurunt', 'The Banc - NEED TO GO AGAIN', 'Chutney Mary', 'Ayllu', 'Farzi Cafe',
    'Vu Lounge', 'Apothecary', 'MezeMiso', 'Nine', 'Kibele', 'Lake Kane', 'Figo Restaurant',
     'Hutong', 'Gaucho', 'Mint leaf', 'Chai Ki', 'Darbaar', 'Dishoom', 'Roti Chai', 'Quaglino',
    'Hakkasan', 'Tarshish', 'China tang', 'The iskelé', 'Stk', 'HSandCO', 'Mahiki (Cocktail)',
    'Madison', 'Coppa Club', 'Thai Square', 'Hiadilao Hot Pot', 'Jw steakhouse', 'Casa do Frango',
    'The meat co', 'Masala Canteen', 'Dinerama (shut down :( )', 'Sticks’n’sushi', 'Scarlet Rasoi',
    'Bocconcino', 'Bright courtyard', 'Cat tre', 'Kricket', 'Dim t', 'Booma', 'circolo popolare',
    'AOK', 'Kinkao (Thai)', 'Cicchetti', 'Bindi Green (bottomless Brunch)', 'Aqua Kyoto',
    'Oka restaurant (sushi)', 'Nabrasa Express', 'Cardamom Black', 'Izgara restaurunt',
    'The Banc - NEED TO GO AGAIN', 'Chutney Mary', 'Ayllu', 'Farzi Cafe', 'Vu Lounge', 'Apothecary',
    'MezeMiso', 'Nine', 'Kibele', 'Lake Kane', 'Figo Restaurant',
    'The Colony Club', 'Hawksmoor', 'Eggbreak - breakfast & Lunch', 'The Ivy Asia',
    'Amazonico London', 'Sheesh Restaurant', 'Aubaine (Breakie,Lunch,Dinner)', 'Shoryu (Japanese)',
    'Chotto Matte (Japanese )', 'Taka', 'Kutir', 'Coco (halal +views)', 'Sixbynico', 'Charco Charco',
    'Yan hi barbecue', 'Mestizo', 'Gloria', 'East West (indian+Italian fusion)', '1947', 'Binda’s Eatery',
    'Kricket', 'Rudy’s Neopolitan', 'Crustbro’s', 'Azura', 'L’Antica Pizzeria Da Michele (one of the oldest pizzeria’s)',
    'Mnky hse', 'Lokkum', 'LPM restaurant & bar', 'Novikov', 'sushisamba', 'ROKA', 'Restaurant Ours', 'Madera',
    'Christopher’s', 'Benihana International', 'Sumosan Twiga', 'Market Hall Victoria (Ox st coming soon)',
    'Gunpowder', 'Kanishka (Indian)', 'Pizza union', 'Kintan', 'Rawshà', 'Jinjuu (Korean)', 'Viet Food',
    'Kahani', 'Bob Bob Ricard', 'Harry’s dolce vita', 'Cantina Laredo (Mex)', 'The blues kitchen',
    'Scarlet Rasoi (indian)', 'Sexy Fish', 'Mildred’s (Good veggie food)', 
    'bird restaurant', 'Pivaz', 'Meat and shake (Watford)', 'The Athenias', 'Japanese canteen',
    'Amigos burger and shake', 'Garfunkel’s', 'Wing Wing', 'Mesa kitchen and lounge', 'Bone daddies (Japanese)',
    'The diner', 'Hoppers', 'The Sauce', 'Flame Flame', 'Big easy', 'Three uncles', 'Absurd Bird', 'Wahaca',
    'Franco Manca', 'Burgeri', 'Zefi', 'Fuwa Fuwa', 'Cereal killer cafe', 'Passo', 'Siirgista Bros (Halal)',
    'Dintaifung', 'Kinkao', 'One love kitchen (Caribbean)', 'Chin Chin (Dessert)', 'Afrikana', 'Fatt Pundit',
    '@Pizza (Grand Central Birmingham)', 'Cocochan (pan Asian)', 'East Street (little bit tasteless but good vibes lol)',
    'DF Tacos', 'Coqfighter', 'Scarpetta', 'Marugame Udon', 'Lina Stores', 'Issho-Ni (bottomless sushi brunch)',
    'Lumi', 'Baozilnn', 'Bar Elba (rooftop bar)', 'Netil 360', 'Skylark roof garden (plus food)', 'Bar douro', 'Coq d’argent',
    'Big chill (normal bar)', '12th Knot', 'Wagtail', 'Syon Lounge', 'Wish lounge', 'The hart lounge', 'Tigerbay shisha lounge', 'VU Lounge',
    'Aura lounge', 'Mesa Kitchen & Lounge', 'Al hadra lounge', 'Atlantis Lounge', 'Envi Lounge',
    'Sumki London', 'Shisha Gardens', 'Noir', 'Ak']})

# Define category filters
Go_again =  ['Hutong', 'Gaucho', 'Mint leaf', 'Chai Ki', 'Darbaar', 'Dishoom', 'Roti Chai', 'Quaglino',
            'Hakkasan', 'Tarshish', 'China tang', 'The iskelé', 'Stk', 'HSandCO', 'Mahiki (Cocktail)',
            'Madison', 'Coppa Club', 'Thai Square', 'Hiadilao Hot Pot', 'Jw steakhouse', 'Casa do Frango',
            'The meat co', 'Masala Canteen', 'Dinerama (shut down :( )', 'Sticks’n’sushi', 'Scarlet Rasoi',
            'Bocconcino', 'Bright courtyard', 'Cat tre', 'Kricket', 'Dim t', 'Booma', 'circolo popolare',
            'AOK', 'Kinkao (Thai)', 'Cicchetti', 'Bindi Green (bottomless Brunch)', 'Aqua Kyoto',
            'Oka restaurant (sushi)', 'Nabrasa Express', 'Cardamom Black', 'Izgara restaurunt',
            'The Banc - NEED TO GO AGAIN', 'Chutney Mary', 'Ayllu', 'Farzi Cafe', 'Vu Lounge', 'Apothecary',
            'MezeMiso', 'Nine', 'Kibele', 'Lake Kane', 'Figo Restaurant']

Want_to_go= ['The Colony Club', 'Hawksmoor', 'Eggbreak - breakfast & Lunch', 'The Ivy Asia',
              'Amazonico London', 'Sheesh Restaurant', 'Aubaine (Breakie,Lunch,Dinner)', 'Shoryu (Japanese)',
              'Chotto Matte (Japanese )', 'Taka', 'Kutir', 'Coco (halal +views)', 'Sixbynico', 'Charco Charco',
              'Yan hi barbecue', 'Mestizo', 'Gloria', 'East West (indian+Italian fusion)', '1947', 'Binda’s Eatery',
              'Kricket', 'Rudy’s Neopolitan', 'Crustbro’s', 'Azura', 'L’Antica Pizzeria Da Michele (one of the oldest pizzeria’s)',
              'Mnky hse']

Recommended= ['Lokkum', 'LPM restaurant & bar', 'Novikov', 'sushisamba', 'ROKA', 'Restaurant Ours', 'Madera',
               'Christopher’s', 'Benihana International', 'Sumosan Twiga', 'Market Hall Victoria (Ox st coming soon)',
               'Gunpowder', 'Kanishka (Indian)', 'Pizza union', 'Kintan', 'Rawshà', 'Jinjuu (Korean)', 'Viet Food',
               'Kahani', 'Bob Bob Ricard', 'Harry’s dolce vita', 'Cantina Laredo (Mex)', 'The blues kitchen',
               'Scarlet Rasoi (indian)', 'Sexy Fish', 'Mildred’s (Good veggie food)']

Casual =   ['bird restaurant', 'Pivaz', 'Meat and shake (Watford)', 'The Athenias', 'Japanese canteen',
          'Amigos burger and shake', 'Garfunkel’s', 'Wing Wing', 'Mesa kitchen and lounge', 'Bone daddies (Japanese)',
          'The diner', 'Hoppers', 'The Sauce', 'Flame Flame', 'Big easy', 'Three uncles', 'Absurd Bird', 'Wahaca',
          'Franco Manca', 'Burgeri', 'Zefi', 'Fuwa Fuwa', 'Cereal killer cafe', 'Passo', 'Siirgista Bros (Halal)',
          'Dintaifung', 'Kinkao', 'One love kitchen (Caribbean)', 'Chin Chin (Dessert)', 'Afrikana', 'Fatt Pundit',
          '@Pizza (Grand Central Birmingham)', 'Cocochan (pan Asian)', 'East Street (little bit tasteless but good vibes lol)',
          'DF Tacos', 'Coqfighter', 'Scarpetta', 'Marugame Udon', 'Lina Stores', 'Issho-Ni (bottomless sushi brunch)',
          'Lumi', 'Baozilnn']

Rooftop = ['Bar Elba (rooftop bar)', 'Netil 360', 'Skylark roof garden (plus food)', 'Bar douro', 'Coq d’argent',
           'Big chill (normal bar)', '12th Knot', 'Wagtail']

Restaurant_shisha = ['Syon Lounge', 'Wish lounge', 'The hart lounge', 'Tigerbay shisha lounge', 'VU Lounge',
                     'Aura lounge', 'Mesa Kitchen & Lounge', 'Al hadra lounge', 'Atlantis Lounge', 'Envi Lounge',
                     'Sumki London', 'Shisha Gardens', 'Noir', 'Ak']


# Apply category filters
Go_again_df1 = df1.isin(Go_again)
Want_to_go_df1 = df1.isin(Want_to_go)
Recommended_df1 = df1.isin(Recommended)
Casual_df1 = df1.isin(Casual)
Rooftop_df1 = df1.isin(Rooftop)
Restaurant_shisha_df1=df1.isin(Restaurant_shisha)



# Display the separate categories
# Display the separate categories
print("Go Again:")
print(df1[df1['Restaurant'].isin(Go_again)])
print("\nWant to Go:")
print(df1[df1['Restaurant'].isin(Want_to_go)])
print("\nRecommended:")
print(df1[df1['Restaurant'].isin(Recommended)])
print("\nCasual:")
print(df1[df1['Restaurant'].isin(Casual)])
print("\nRooftop:")
print(df1[df1['Restaurant'].isin(Rooftop)])
print("\nRestaurant/Shisha:")
print(df1[df1['Restaurant'].isin(Restaurant_shisha)])


# In[15]:


df1


# In[11]:


#pip install folium


# In[10]:


#pip install googlemaps


# In[16]:


# Initialize the Google Maps client with your API key
import googlemaps
api_key = 'AIzaSyBTfRZvBb4vNrBsb7o80RKH5Ve4vJvFxg4'
gmaps = googlemaps.Client(api_key)

# Function to get the location coordinates from the restaurant name
def get_location(restaurant_name):
    # Perform geocoding request
    geocode_result = gmaps.geocode(restaurant_name)
    
    # Extract the latitude and longitude from the geocoding result
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None

# Apply the get_location function to the restaurant names in your DataFrame
df1['Location'] = df1['Restaurant'].apply(get_location)

# Display the DataFrame with the location information
print(df1)


# In[17]:


import folium

# Create a map centered on a specific location
map_restaurants = folium.Map(location=[51.5074, -0.1278], zoom_start=12)  # London coordinates

# Add markers for each restaurant location
for index, row in df1.iterrows():
    restaurant_name = row['Restaurant']
    location = row['Location']

    if location is not None:
        latitude, longitude = location
        folium.Marker([latitude, longitude], popup=restaurant_name).add_to(map_restaurants)

# Display the map
map_restaurants


# In[18]:


import folium

# Create a map centered on London
map_london = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# Filter the DataFrame to include only restaurants in London
df_london = df1[df1['Location'].notnull()]  # Assuming 'Location' column contains the coordinates

# Add markers for each restaurant location in London
for index, row in df_london.iterrows():
    restaurant_name = row['Restaurant']
    location = row['Location']
    latitude, longitude = location

    # Add a marker for each restaurant within London coordinates
    folium.Marker([latitude, longitude], popup=restaurant_name).add_to(map_london)

# Display the map with London restaurants
map_london


# In[ ]:




