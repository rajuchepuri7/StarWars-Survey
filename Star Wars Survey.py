#!/usr/bin/env python
# coding: utf-8

# # Star Wars Survey

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas
import numpy
from matplotlib import pyplot

# Read the data set into a DataFrame
star_wars = pandas.read_csv("star_wars.csv", encoding="ISO-8859-1")
star_wars


# In[2]:


star_wars = star_wars[pandas.notnull(star_wars["RespondentID"])]


# In[3]:


star_wars.head()


# In[4]:


star_wars.columns


# ### Cleaning and Mapping Yes / No Columns

# In[5]:


yes_no = {'Yes': True, 'No': False}

star_wars["Have you seen any of the 6 films in the Star Wars franchise?"] = star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].map(yes_no)
star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] = star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].map(yes_no)
star_wars["Do you consider yourself to be a fan of the Star Trek franchise?"] = star_wars["Do you consider yourself to be a fan of the Star Trek franchise?"].map(yes_no)

star_wars


# ### Cleaning and Mapping Checkbox Columns

# In[6]:


movie_seen_unseen = {
    'Star Wars: Episode I  The Phantom Menace': True,
    'Star Wars: Episode II  Attack of the Clones': True,
    'Star Wars: Episode III  Revenge of the Sith': True,
    'Star Wars: Episode IV  A New Hope': True,
    'Star Wars: Episode V The Empire Strikes Back': True,
    'Star Wars: Episode VI Return of the Jedi': True,
    numpy.nan:  False
}

for column in star_wars.columns[3:9]:
    star_wars[column] = star_wars[column].map(movie_seen_unseen)

star_wars


# In[7]:


star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    'Unnamed: 4': 'seen_2',
    'Unnamed: 5': 'seen_3',
    'Unnamed: 6': 'seen_4',
    'Unnamed: 7': 'seen_5',
    'Unnamed: 8': 'seen_6',
})
star_wars


# ### Cleaning the Ranking Columns

# In[8]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars.head()


# In[9]:


star_wars = star_wars.rename(columns={
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.': "ranking_1",
    'Unnamed: 10': 'ranking_2',
    'Unnamed: 11': 'ranking_3',
    'Unnamed: 12': 'ranking_4',
    'Unnamed: 13': 'ranking_5',
    'Unnamed: 14': 'ranking_6'
})
star_wars


# ### Finding the Highest-Ranked Movie

# In[10]:


star_wars[star_wars.columns[9:15]].mean()


# In[11]:


from numpy import arange
fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = star_wars[star_wars.columns[9:15]].mean()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(star_wars.columns[9:15], rotation = 90.0)

pyplot.show()


# ## Rankings

# So far, we've cleaned up the data, renamed several columns, and computed the average ranking of each movie. As I suspected, it looks like the "original" movies are rated much more highly than the newer ones.
# 
# The "Star Wars: Episode V The Empire Strikes Back" movie is highly rated (ranking_5) and the "Star Wars: Episode III Revenge of the Sith" is rated very low (ranking_3). a lower ranking is better! here.

# ### Finding the Most Viewed Movie

# In[12]:


star_wars[star_wars.columns[3:9]].sum()


# In[13]:


fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = star_wars[star_wars.columns[3:9]].sum()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(star_wars[star_wars.columns[3:9]], rotation = 90.0)

pyplot.show()


# ## View Counts

# It appears that the original movies were seen by more respondents than the newer movies. This reinforces what we saw in the rankings, where the earlier movies seem to be more popular.

# In[14]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]


# In[15]:


print(males[males.columns[9:15]].mean())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = males[males.columns[9:15]].mean()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(males[males.columns[9:15]], rotation = 90.0)

pyplot.show()


# In[16]:


print(females[females.columns[9:15]].mean())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = females[females.columns[9:15]].mean()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(females[females.columns[9:15]], rotation = 90.0)

pyplot.show()


# In[17]:


print(males[males.columns[3:9]].sum())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = males[males.columns[3:9]].sum()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(males[males.columns[3:9]], rotation = 90.0)

pyplot.show()


# In[18]:


print(females[females.columns[3:9]].sum())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = females[females.columns[3:9]].sum()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(females[females.columns[9:15]], rotation = 90.0)

pyplot.show()


# # Male/Female differences in favorite Star Wars movie and most seen movie

# Interestingly, more males watches episodes 1-3, but males liked them far less than females did.

# In[19]:


fans = star_wars[star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] == True]
Others = star_wars[star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] == False]


# In[20]:


print(fans[fans.columns[9:15]].mean())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = fans[fans.columns[9:15]].mean()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(fans[fans.columns[9:15]], rotation = 90.0)
ax.set_title("Highest-Ranked movie by Starwars Fans")

pyplot.show()


# In[21]:


print(Others[Others.columns[9:15]].mean())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = Others[Others.columns[9:15]].mean()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(Others[Others.columns[9:15]], rotation = 90.0)
ax.set_title("Highest-Ranked movie by Others")

pyplot.show()


# In[22]:


print(fans[fans.columns[3:9]].sum())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = fans[fans.columns[3:9]].sum()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(fans[fans.columns[3:9]], rotation = 90.0)
ax.set_title('Most Viewed Movie by Starwars Fans')

pyplot.show()


# In[23]:


print(Others[Others.columns[3:9]].sum())

fig, ax = pyplot.subplots()

bar_positions = arange(6) + 0.75
bar_heights = Others[Others.columns[3:9]].sum()
pyplot.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(range(1,7))
ax.set_xticklabels(Others[Others.columns[3:9]], rotation = 90.0)
ax.set_title('Most Viewed Movie by Others')

pyplot.show()


# ### Difference in favorite Star Wars movie and most seen movie between Starwars Fans/Other

# While Starwars fans liked the episode 4, 5 and 6, Others liked episode 1, 5 and 6.
# 
# it's very clear that Starwars fans viewd the movies more than others. But the most viewed movies are similar betweer Starwar fans and Others. Both of them viewd episode 1, 5 and 6 the most!
