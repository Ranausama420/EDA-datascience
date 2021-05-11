#!/usr/bin/env python
# coding: utf-8

# <center> <h2> Assignment # 2 </h2> </center>  
# <center> <h3> Perform the basic wrangling on the data <h3> </center> 

# ### Task 1: Importing Files and Libraries
# **i. Import Required libraries and Data File**

# In[1]:


#write code here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')


# **ii. Read Fifa.csv file**

# In[2]:


#write code here
data= pd.read_csv('fifa.csv')


# **iii. Copy dataframe in df**

# In[3]:


#write code here
df = data.copy()


# ### Task 2: Some Basic Operations on Data Frame </h3>

# **i. Display the first five rows of the dataframe**

# In[4]:


#Write Your Code Here
df.head()


# **ii. Display columns names of the dataframe**

# In[5]:


#Write Your Code Here
df.columns


# **iii. Remove extra space in column names**

# In[6]:


#Write Your Code Here
df.columns.str.strip()


# **iv. Check data type of columns**

# In[7]:


#Write Your Code Here
df.dtypes


# **v. Get the Last five rows of dataframe**

# In[8]:


#Write Your Code Here
df.tail()


# ### Question: What do you understand by having a look at the top five and last 5 rows of data? 

# *Hint: Some values are not filled for certain types of positions.* 

# ### Answer: 
#              The dataset consist of 19 columns and some values with empty string and last colmn contain some NaN values

# **vi. Get the statistical summary for the numerical columns**

# In[9]:


#Write Your Code Here
df.describe()


# **vii. Show the statistical summary of object type columns in dataframe**

# In[10]:


#Write Your Code Here
df.describe(include='O')


# **viii. Show the statistical summary of all the columns in dataframe**

# In[11]:


#Write Your Code Here
df.describe(include='all')


# ### Task 3: Dealing with Missing Value 

# **i. Count the number of missing values in each column**

# In[12]:


#Write Your Code Here
df.isnull().sum()


# **ii. Replace extra space with NaN**

# In[13]:


#write code here
df=df.replace(' ',np.NaN)
df.head()


# **iii. Fill all null values of dataframe with 0**

# In[14]:


#write code here
df=df.replace(np.NaN,0)
df.head()


# **iv. Count the number of players in each position**

# In[15]:


#Write Your Code
#there were spaces in column names
df.columns = df.columns.str.replace(' ', '')
df.groupby('position')['position'].count()


# **v. Check datatypes of all columns**

# In[16]:


#write code here
df.dtypes


# **vi. Cast ' pace', ' shooting', ' passing', ' dribbling', ' defending',' heading', ' diving', ' handling', ' kicking', ' reflexes', ' speed',' positioning' into Integer type**

# In[17]:


#write code here
cols=['pace', 'shooting', 'passing', 'dribbling', 'defending','heading', 'diving', 'handling', 'kicking', 'reflexes', 'speed','positioning']
for col in cols:
    df[col]=df[col].astype('int64')


# In[18]:


#write code here
df.dtypes


# ### Task 4

# **You have to split the dataframe into two dataframes, one containing all the features of Goal Keeper and other dataframe contains all other players** 
# 

# In[19]:


df_goalkeeper= df[df['position'] == 'GK']
df_goalkeeper.head()


# <span style="color:green">**As you can see that the dataframe is empty and no value has been assigned to it. Let's check out the issue.**</span>

# **i. Check unique value of position, there must be a space on each position**

# In[20]:


#Write code here
df['position'].unique()


# <span style="color:green">**From the above output, you can see that there is an extra space in the position reffered to as GK.**</span> 

# **ii. Remove extra space in position column and remove it like ' GK' to 'GK' and then again make dataframe of GK**<br>
# *Hint: Use str.replace*
# 

# In[21]:


#Write Code here
df['position']=df['position'].str.replace(' ','')
df['position'].unique()


# **iii. Now make a dataframe of df_goalkeeper.**

# In[22]:


#Write Your Code Here
df_goalkeeper= df[df['position'] == 'GK']
df_goalkeeper.head()


# **iv. Dataframe of goal keeper must and only contain the following columns 'id', 'name', 'rating', 'position', 'height', 'foot',' rare','diving', 'handling', 'kicking', 'reflexes', 'speed','positioning'** <br>
# **Drop all the other columns**

# In[23]:


#write code here
col_to_keep=['id', 'name', 'rating', 'position', 'height', 'foot','rare','diving', 'handling', 'kicking', 'reflexes', 'speed','positioning']
df_goalkeeper=df_goalkeeper[col_to_keep]


# In[24]:


#write code here
df_goalkeeper


# **v. Make the dataframe of df_players having data of the all the other players except the goal keeper.**
# 

# In[25]:


#write code here
df_players=df[df['position'] != 'GK']
df_players.head()


# **vi. Dataframe of other players must contain the following columns 'id', 'name', 'rating', 'position', 'height', 'foot', 'rare',  'pace', 'shooting', 'passing', 'dribbling', 'defending', 'heading'** <br>
# **Drop all the other columns**

# In[26]:


#write code here
col_to_keep=['id', 'name', 'rating', 'position', 'height', 'foot', 'rare', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'heading']
df_players=df_players[col_to_keep]


# In[27]:


#write code here
df_players.head()


# **vii. Find shape of both the datasets**

# In[28]:


#Write Your Code Here
df_goalkeeper.shape


# In[29]:


#write code here
df_players.shape


# **viii. Check head of both the splited dataframe**

# In[30]:


#Write Your Code Here
df_goalkeeper.head()


# In[31]:


#Write Your Code Here
df_players.head()


# **ix. Show the summary stats of both the datasets**

# In[32]:


#Write Your Code Here for summary stats of goal keeper
df_goalkeeper.describe()


# ### Question: What do you understand from the summary statistics of goal keeper?

# ### Answer:
#             From this statistical summary it is clear that we have a data of 930 rows because count of id is 930 and all id's are unique. we have average rating about 65 or 66 and maximum of rating is 89 and data is slightly spread out because standard deviation is bit high , we have max height of 208 and average is 188 and minimum is 173, there is no accurate data for pace, shooting, passing, dribbling, defending, heading becuase of empty strings

# In[ ]:





# In[33]:


#Write Your Code Here for summary stats of players
df_players.describe()


# ### Question: What do you understanf from the summary statistics of other players?

# ### Answer:
#              From this summary, we can see that we have 7917 rows. we have max rating of 94 which is greater than goal keeper dataset. we have more accurate summary because there is no empty string in df_players dataset, maximum of shooting, passing and dribbling are above or equal to 90, they all have high standard deviation which mean data is spread out, and average is range between 55 to 61

# ### Task 5: Group By and Pivoting 

# **i. Display averages of each columns according the players' positions**

# In[34]:


#Write Your Code Here
df.groupby('position').mean()


# **ii. Count number of players against each position and foot used by them.**    
# *Hint: Use Groupby*

# In[35]:


#Write Your Code Here
#Group By Here
df.groupby(['position','foot']).count()


# **iii. Perform grouping on position and foot to find mean, min and max values of rating. Store the result in a variable called 'a'** <br>
# 

# In[36]:


#Write Your Code H
a=df.groupby(['position','foot']).agg({'rating': ['mean', 'min', 'max']}) 
a


# **iv. Perform "PIVOTING" on the dataframe 'df'. The properties should be as following:**<br>
# *index = ' position'<br>
# columns = ' foot'<br>
# values=' rating'<br>
# aggfunc=['min','mean']*<br>

# In[37]:


#Write Code Here
pivt= pd.pivot_table(df,index='position',columns='foot', values='rating',aggfunc=['min','mean'])
pivt


# # Visualization

# ### Task 6: Display total players of each position.

# In[38]:


#write code here
sns.countplot(x='position', data=df);
plt.ylabel('No. Of Players')


# **Question: What insights do you get from the above plot?**
# ### Answer:
#              Maximum players are at M position and lowest number of players are goal keeper while more players are at D position as compared to A position

# ### Task 7:  Show the total number of players for each foot type.

# In[39]:


#Write code here
sns.countplot(x='foot', data=df);
plt.ylabel('No. Of Players')


# ### Task 8. Show 'foot' ditribution per 'rating' using boxplot

# In[40]:


#write code here
sns.boxplot(x = 'foot', y = 'rating', data = df) 


# **Question: What does the above box plot show?**
# ### Answer
#              Players with right foot have alot of outliers and this distribution is positivley skewed, players with left are normaly skewed and there are less outliers as compared tp right foot

# ### Task 9. Display total number of players for each foot type according to their positions. But the result of each position should be a separate graph yet shown collectively  <br>
# *Hint: You can use subplots and you can have a separate dataframe for each postion. Sample code fir subplots is given below:*<br>
# *Sample Code 
# <br>*
# ```
# fig, ax=plt.subplots(2,2,sharey=True, figsize=(15,8))
# sns.countplot(x='rating', data=df_goalkeeper, ax=ax[0,0])
# ax[0,0].set_title('Goal keeper')
# ```

# In[41]:


df['position'].unique()


# In[42]:


df_M=df[df['position']=='M']
df_A=df[df['position']=='A']
df_D=df[df['position']=='D']


# In[43]:


#Write code here
fig, ax=plt.subplots(2,2,sharey=True, figsize=(15,12))
sns.countplot(x='foot', data=df_goalkeeper, ax=ax[0,0])
sns.countplot(x='foot', data=df_M, ax=ax[0,1])
sns.countplot(x='foot', data=df_A, ax=ax[1,0])
sns.countplot(x='foot', data=df_D, ax=ax[1,1])
ax[0,0].set_title('Goal keeper')
ax[0,1].set_title('Midfielder')
ax[1,0].set_title('Attacking midfield')
ax[1,1].set_title('Defenders')


# ### Task 10: What can be the relationship/correlation  ratings and defending of other players.<br>
# *Hint: reg plot*

# In[44]:


#Write code here
plt.figure(figsize=(15,10));
sns.regplot(x="rating", y="defending", data=df)


# **Question: What does the above plot show?**
# ### Answer 
#             rating and defending shows positive correlation, while the strength of correlation is bit weak.

# ### Task 11: Plot a graph to show the relationship/correlation among rating and handling of goal keeper. Also the distributions of each should be displayed along with the graph showing the relationship.<br>
# *Hint: jointplot*

# In[45]:


#Write code here
sns.jointplot(x ='rating',y='handling',data = df_goalkeeper)


# ### Task 12-a.  Make a heatmap to show correlation among all the columns of the goal keeper dataframe and answer the questions

# In[46]:


#write code here to find the correlation
cor=df_goalkeeper.corr()


# In[47]:


#write code here for heatmap
plt.figure(figsize=(15,10))
sns.heatmap(cor, annot=True, fmt='.1g');


# **Question: Which columns/variables/factors are important to determine ratings of goal keepers and why?**
# ### Answer:
#             diving, handling, kicking and reflexes are important factors in determining ratings because they all have higher corelation values

# ### Task 12-b. Make a heatmap show correlation among all the columns of dataframe having data of all the other players and answer the questions

# In[48]:


# Write the code to find the correlation here
cor=df_players.corr()


# In[49]:


#write code here for heatmap
sns.heatmap(cor, annot=True, fmt='.1g');


# **Question: Which columns/variables/factors are important to dertmine ratings of other players and why?**
# ### Answer
#             Shooting, passing and dribbling are important factors in determining ratings of other player becuase they have higher correlation values

# ### Task 13. Show distribution of rating.
# *Hint: Use dist plot*

# In[50]:


#write code here
sns.distplot(df['rating'])


# **Question: What insights do you get from the distplot drawn above?**
# ### Answer
#             This distploat shows distribution of ratings of players and this distribution seems symmetric

# ### Task 14: Show the distribution of ratings of each types of players using distplot() and apply KDE

# In[51]:


#Write code here
fig, ax=plt.subplots(2,2,sharey=True, figsize=(15,12))
sns.distplot(df_goalkeeper['rating'], kde = True, ax=ax[0,0])
sns.distplot(df_M['rating'], kde = True, ax=ax[0,1])
sns.distplot(df_A['rating'], kde = True, ax=ax[1,0])
sns.distplot(df_D['rating'], kde = True, ax=ax[1,1])
ax[0,0].set_title('Goal keeper')
ax[0,1].set_title('Midfielder')
ax[1,0].set_title('Attacking midfield')
ax[1,1].set_title('Defenders')


# ### Task 15: What is the count of rare players in each type of postion?

# In[52]:


#write code here
df.groupby('position')['rare'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:




