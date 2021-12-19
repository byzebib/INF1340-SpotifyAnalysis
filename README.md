# INF1340-SpotifyAnalysis
Final group project for INF1340

Project Name 

INF1340H Final Project - Ariana Grande Spotify Music Analysis, Data Visualization, and K-Means Clustering of Music

Introduction 

This project works to first pull data of Ariana Grande’s music from our Spotify account to create a CSV file of her complete music information. Then, the program analyzes the data by different moods, properties, and contexts ranked by Spotify such as popularity, release date, length, danceability, liveliness, etc demonstrated by different data visualizations such as histograms, bar charts, graphs and more. To analyze the data, the project makes charts to determine the correlation between popularity, release date, danceability, album/song title, and more. 

Description 

This project works by accessing Spotify data to retrieve Ariana Grande’s music data and sorting through properties such as album, release date, popularity, danceability, acousticness, energy and more. The program cleans the data to remove any duplicates, increase the usability of the data, and sort the variables by their properties. The program then analyzes the data using NumPy, pandas, stats, and seaborn to create bar graphs based on correlations in the data such as Ariana Grande’s most popular albums, most danceable albums, and most popular, danceable, acoustic, and energetic songs. To analyze the data, the program sorts the data by properties such as popularity, danceability, release date, length, accouticness, and more. 

Additionally, the project pulled one of the member’s(Bethlehem Zebib) personal Spotify data to analyze and create cluster predictions of her music tastes.  To do this, Bethlehem sent a request to receive her data from Spotify.  This request usually takes up to a week, however, she received her data within 3 days. The request comes with a ZIP folder of multiple files, the only data we needed was the three JSON files with Bethlehem’s streaming history.  

The final portion of the project involves

Requirements 

This program has no special requirements besides a python environment and ensuring the environment has access to the arianagrande_spotify.csv file and the CSV file with Bethlehem’s Spotify data.

Configuration

The Ariana Grande CSV file may not be configured on google colab (because google colab does not support the spotipy package), but it will run on Jupyter Notebook and Replit. If the CSV file is still not showing up, we have attached the Ariana Grande CSV file that the user can upload to the python environment when running the program. 

Troubleshooting & FAQ

If the user receives errors when attempting to run the program please ensure that arianagrande_spotify.csv is uploaded to the environment. If the graphs are not loaded, please ensure the packages have been run. 
