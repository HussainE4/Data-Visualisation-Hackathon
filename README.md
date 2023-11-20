# Data-Visualisation-Hackathon
This repository contain's our team's submission to the CANIS Data Visualization and Foreign Interference Hackathon.

# Data
This project uses the CANIS_PRC_state_media_on_social_media_platforms dataset.

# Overview
Our goal was to showcase the scale of China's social media prescence. We did this by analysing the 4 largest parent entities in the dataset(Ministry of Foreign Affairs, Central Publicity Department, State Council, Central Committee of the Chinese Communist Party) and creating a regional breakdown.

In our project, we added together the social media followers of various actors assocaiated with each of these entities and plotted them using the "pandas" and "matplotlib" libraries.
You can view our results at https://rickshaltzv2.github.io/

# Usage
Note: For both the python files, you must first install the dependencies in requirements.txt

The plot_entity_regions.py file is used for plotting the regional breakdown for a given parent entity from the dataset. Run the file and input an entity to see the results

The EntityGraph.py file is used for creating plotting the number of followers of actors associated with the main Chinese parent entities and major English news organisations. Run the file to see the results

The CANIS_data_viz_code.Rmd file is used for showcasing the distribution of the major Chinese parent entities with regards to follower counts in the Anglosphere. Run the file to see the visualisation.

