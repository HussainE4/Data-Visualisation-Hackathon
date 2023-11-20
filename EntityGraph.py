import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def unpack(entity):
    df = pd.read_excel("/Users/jackfan/Downloads/CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx")

    #Filling na values, cleaning data
    df['Facebook Follower #'] = df['Facebook Follower #'].fillna(0)
    df['X (Twitter) Follower #'] = df['X (Twitter) Follower #'].fillna(0)
    df['Instagram Follower #'] = df['Instagram Follower #'].fillna(0)
    df['Threads Follower #'] = df['Threads Follower #'].fillna(0)
    df['YouTube Subscriber #'] = df['YouTube Subscriber #'].fillna(0)
    df['TikTok Subscriber #'] = df['TikTok Subscriber #'].fillna(0)

    df['Total Followers'] = df['X (Twitter) Follower #'] + df['Facebook Follower #'] 
    + df['Instagram Follower #'] + df["Threads Follower #"] + df['YouTube Subscriber #'] +df['TikTok Subscriber #']

    # seperating on;ly ministry of affairs
    df = df[df['Parent entity (English)']==entity]
    
    #aggregating values
    aggregate_function = {'Region of Focus': 'first','Total Followers': 'sum'}
    df = df.groupby('Region of Focus', as_index = False).aggregate(aggregate_function) 
    
    #Sorting and getting the last 10
    df = df.sort_values(by='Total Followers')
    
    return df

def plot(data, x_obj, y_obj, x_title, y_title, title):
    my_range = range(1, len(data.index)+1)  

    data['Color'] = data[y_obj].apply(lambda x: 'red' if is_chinese(x) else 'skyblue')

    
    plt.rcParams.update({'font.size': 20})

    #Plotting 
    plt.hlines(y=my_range, xmin=0, xmax=data[x_obj], color=data['Color'])
    plt.plot(data[x_obj], my_range, 'D')

    #Adding labels and fonts
    plt.yticks(my_range, data[y_obj] )
    plt.xlabel(x_title, size = 20).set_fontweight('bold')
    plt.ylabel(y_title, size = 20).set_fontweight('bold')
    plt.xscale('log')
    plt.title(title,size=20).set_fontweight('bold')

    #Suffix for the numbers
    def suffix(v):
        #K suffix
        if 1000<=v<1000000:
            return str(round(v/1000,1)) + " K"
        elif v>=1000000:
            return str(round(v/1000000,1))  + " Million"
        else:
            return str(v)
            
    #Adding the population textg
    for i, v in enumerate(data['Total Followers']):
        plt.text(v*1.1, i+0.9, suffix(v))
    
    plt.show()  

#Method for determining if the entity is chinese or not
def is_chinese(entity):
        return entity in ['Ministry of Foreign Affairs', 'Central Publicity Department', 'State Council', 'Committee of CCP']

#Method for getting the followers from dataframe
def get_total_followers(data, ):
    return data['Total Followers'].sum()

#Anglosphere followers were researched
df = { 'Parent Entity' : ['CNN', 'Fox News', 'CBC', 'ABC', 'BBC', 'Ministry of Foreign Affairs', 'Central Publicity Department', 'State Council', 'Committee of CCP'],
        'Total Followers': [143700000, 67900000, 5400000, 4260000, 93620000, 
                            get_total_followers(unpack('Ministry of Foreign Affairs')),
                            get_total_followers(unpack('Central Publicity Department')),
                            get_total_followers(unpack("State Council")),
                            get_total_followers(unpack('Central Committee of the Chinese Communist Party'))
                            ]
    }

#Sorting the dataframe by followers for plotting
new_df = pd.DataFrame(df).sort_values(by='Total Followers')

#Plotting
plot(new_df, 'Total Followers', 'Parent Entity', 'Total Social Media Followers', 'Parent Entity', 'Total Social Media Followers Across Parent Entities')