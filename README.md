# INF1340-SpotifyAnalysis
Final group project for INF1340

# Project Name 

INF1340H Final Project - Ariana Grande Spotify Music Analysis, Data Visualization, and K-Means Clustering of Music

# Introduction 

This project works to first pull data of Ariana Grande’s music from our Spotify account to create a CSV file of her complete music information. Then, the program analyzes the data by different moods, properties, and contexts ranked by Spotify such as popularity, release date, length, danceability, liveliness, etc demonstrated by different data visualizations such as histograms, bar charts, graphs and more. To analyze the data, the project makes charts to determine the correlation between popularity, release date, danceability, album/song title, and more. 

# Description 

This project works by accessing Spotify data to retrieve Ariana Grande’s music data and sorting through properties such as album, release date, popularity, danceability, acousticness, energy and more. The program cleans the data to remove any duplicates, increase the usability of the data, and sort the variables by their properties. The program then analyzes the data using NumPy, pandas, stats, and seaborn to create bar graphs based on correlations in the data such as Ariana Grande’s most popular albums, most danceable albums, and most popular, danceable, acoustic, and energetic songs. To analyze the data, the program sorts the data by properties such as popularity, danceability, release date, length, accouticness, and more. 

Additionally, the project pulled one of the member’s(Bethlehem Zebib) personal Spotify data to analyze and create cluster predictions of her music tastes.  To do this, Bethlehem sent a request to receive her data from Spotify.  This request usually takes up to a week, however, she received her data within 3 days. The request comes with a ZIP folder of multiple files, the only data we needed was the three JSON files with Bethlehem’s streaming history.  

The final portion of the project involves creating suitable k-means clusters of the songs in the Ariana Grande CSV file and Bethlehem's Spotify Data CSV file. Using the Elbow method with the within cluster sum of errors (wcss), the optimal number of clusters was found for both datasets. An analysis was conducted of each cluster that was found based on the features of the songs, this includes features such as dancability, tempo, and energy. The analysis of the clusters can be found in the corresponding files. The purpose of creating the clusters is to use as a base for a recommendation system. If a particular song was chosen by a user a list of similar songs can be displayed based on which cluster the users song choice is placed in.

## Description of Files

**Ariana Grande Spotify** - includes the code used to pull Ariana Grande's discography from a playlist that was created on Spotify

**arianagrande_spotify.csv** - CSV file that was created using the code from the *Ariana Grande Spotify* file. This CSV files includes information on each song that was in the original Spotify playlist 

**Ariana Grande K-Means Recommendation** - includes the data analysis of Ariana Grande's discography using the k-means method

**Betye Stream** - includes the code used to pull Bethlehem's spotify streaming history and the corresponding information for each song that was pulled

**MySpotifyData.csv** - CSV file that contains information regarding each song from Bethlehem's streaming history

**Betye Spotify** - includes the analysis of the songs that Bethlehem has streamed along with the analysis of the songs from her streaming history using the k-means method

# Requirements 

This program has no special requirements besides a python environment and ensuring the environment has access to the arianagrande_spotify.csv file and the CSV file with Bethlehem’s Spotify data.

# Configuration

The Ariana Grande CSV file may not be configured on google colab (because google colab does not support the spotipy package), but it will run on Jupyter Notebook and Replit. If the CSV file is still not showing up, we have attached the Ariana Grande CSV file that the user can upload to the python environment when running the program. 

# Troubleshooting & FAQ

If the user receives errors when attempting to run the program please ensure that arianagrande_spotify.csv or MySpotifyData.csv is uploaded to the environment based on which file is being run. If the graphs are not loaded, please ensure the packages have been run. 

# Expected Outcomes 
<img width="818" alt="Screen Shot 2021-12-19 at 2 42 18 PM" src="https://user-images.githubusercontent.com/63612469/146693648-326e58de-9cb2-4625-826c-98ddda139797.png">

<img width="742" alt="Screen Shot 2021-12-19 at 5 48 56 PM" src="https://user-images.githubusercontent.com/63612469/146693693-39feaad1-bd79-4c74-b07a-47de17ab9d30.png">




## Citations 

Dae Bardhoshi, September 30th, "Music System", Source Code,  https://github.com/DeaBardhoshi/Data-Science-Projects/blob/main/Music%20System.ipynb

Rafael Duarte, March 19th, “Spotify_K_Means_Clustering”, Source Code, 
https://github.com/rafaelnduarte/Spotify_K-Means_Clustering/blob/master/Spotify_Clulstering.ipynb

Rohit Kumar Thakur, August 30th, "Spotify Data Visualization and Analysis using Python" Source code, https://medium.com/geekculture/spotify-data-visualization-and-analysis-using-python-4af81c5531a7

