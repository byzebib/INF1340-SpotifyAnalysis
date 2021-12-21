# APIs
### Ariana Grande API

def TrackIDs(user, playlist_id):

This function works to retrieve Spotify Track ID data using spotipy packages (a Python library for Spotify API) to determine variables such as the id associated with each track and audio features such as name, album, artist, release date, length, and popularity. These ids are later used to associate themselves with each track feature when analyzing and determining the data. The audio features are used to organize the audio information by name, album, artist, release date, length and popularity. 

def TrackFeatures(id): 

This function works to retrieve Spotify data using spotipy packages (a Python library for Spotify API)  and determine properties for music data such as acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, and length that the program later uses to analyze and compare the data. These ids are later used to associate themselves with each track feature when analyzing and determining the data. The properties are used to analyze the audio information by acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, and length of the song. 

pd.DataFrame: 

pd.Data frame is the cleaned version of the Ariana Grande CSV file in a data frame that is used to organize, display and analyze the data.


### Personal Streaming Data API

User Authentication to Access Spotify’s API
* Client ID (your client id when you sign up for Spotify Developers Account)
* Client Secret (your secret key on your Spotify Developers Account)
* Authentication URL (https://accounts.spotify.com/api/token)
* Store personal Access Token when you make a call
* Header - this authenticates when you make a call to the API
* Base URL is the link to access Spotify’s API (https://api.spotify.com/v1/) 

Access Personal Data Files
* pd.read_json() transforms a json file into a pandas dataframe.
* pd.concat() will combine all three streaming JSON files by stacking the data frames. 
* json.load() helps with reading json files in ipynb frame
* pd.DataFrame.from_dict() and pd.json_normalize() will split the JSON data into the appropriate data frame columns. 
* pd.merge() with merge data frames by columns.

Getting Audio Features for Each Song
* Feature_dict creates an empty list to store the pulled audio feature data from spotify’s API. 
* to_csv() converts the data frame into a csv file. 

Personal Stream Data Analysis
* pd.read_csv() reading the newly made streaming data library in the previous step to conduct the analysis.
* pd.DataFrame(“YOUR DATA”).drop() remove any unnecessary columns for the analysis.
* your_df.groupby() instead of having multiple rows for the same track, we take the sum of the total streamed seconds of each song, thus, reducing unnecessary duplicates. 
* your_df.describe() provides statistical summaries of the audio features for all tracks
* your_df.hist() histogram of each of the audio features
* your_df.corr() correlation matrix

#### Radar Chart
To normalise the tempo and loudness values since it does not have a 0-1 range like the other features. 

Using matplotlib, plot a circle to illustrate the means of each audio feature.

#### KMeans Analysis
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D
Create a KMeans model called the Elbow to determine the most ideal number of clusters for the prediction analysis. 
Must create a copy of the data to prevent changing the original data frame.  
From here, select only the numerical columns, i.e. audio features for the prediction analysis.
Scale the data for the columns to have similar ranges (0-1). 
Create the KMeans 3D plot graph with the clusters 
Lastly, print out the songs placed into the 4 clusters (0,1,2,3). 

