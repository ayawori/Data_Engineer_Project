
# Sparkify Postgres ETL

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


## Schema for Song Play Analysis
Using the song and log datasets, we create following tables.

Fact Table
1. songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

Dimension Tables
2. users - users in the app
  user_id, first_name, last_name, gender, level
3. songs - songs in music database
  song_id, title, artist_id, year, duration
4. artists - artists in music database
artist_id, name, location, latitude, longitude

5. time - timestamps of records in songplays broken down into specific units
   start_time, hour, day, week, month, year, weekday
   
##  Project files


In addition to the data files, the project workspace includes six files:

1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.
7. README.md provides discussion on your project.
#  Project Steps

Below are steps you can follow to complete the project:

## Create Tables
1. Write CREATE statements in sql_queries.py to create each table.
2. Write DROP statements in sql_queries.py to drop each table if it exists.
3. Run create_tables.py to create your database and tables.


4. Run in terminal
 ```
python create_tables.py
```

5. Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.


6. Followed the instructions and completed etl.ipynb Notebook to create the blueprint of the pipeline to process and insert all data into the tables.

7. Once verified that base steps were correct by checking with test.ipynb, filled in etl.py program.

8. Run etl in terminal, and verify results:
 ```
python etl.py
```



Notice:


We notice that, if the  dataset that we  have is a subset of a much larger dataset, so it's possible that the artist_id which you are looking for is not even available.
In that case, we can remove the foreign key constrain.



## Build ETL Processes
We follow the instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table.


Notice: Rememebr to rerun create_tables.py to reset your tables before each time you run this notebook.

## Build ETL Pipeline
Prerequisites: 
- Database and tables created

Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables.
Run test.ipynb to confirm your records were successfully inserted into each table.


1. On the etl.py we start our program by connecting to the sparkify database, and begin by processing all songs related data.

2. We walk through the tree files under /data/song_data, and for each json file encountered we send the file to a function called process_song_file.

3. Here we load the file as a dataframe using a pandas function called read_json().

4. For each row in the dataframe we select the fields we are interested in:
    
    ```
    song_data = [song_id, title, artist_id, year, duration]
    ```
    ```
     artist_data = [artist_id, artist_name, artist_location, artist_longitude, artist_latitude]
    ```
5. Finally, we insert this data into their respective databases.

6. Once all files from song_data are read and processed, we move on processing log_data.


7. We load our data as a dataframe same way as with songs data. 

