(Udacity: Data Engineering Nano Degree) | siddeghamid@gmail.com | 2020-08-16_
_This project is a part of [Udacity's Data Engineer Nano Degree](https://eu.udacity.com/course/data-engineer-nanodegree--nd027)._

# PROJECT-1: Data Modelling with Postgres

## Quick start

After installing python3 + postgresql libraries and dependencies, run from command line:

* `python3 create_tables.sql` (to create the DB to Postgresql)
* `python3 etl.py` (to process all the input data to the DB)

---

## Overview

This Project-1 handles data of a music streaming startup, Sparkify. Data set is a set of files in JSON format and contains two parts:

* **./data/song_data**: static data about artists and songs
* **./data/log_data**: event data of service usage e.g. who listened what song, when, where, and with which client

Below, some figures about the data set (results after running the etl.py):

* ./data/song_data: 71 files
* ./data/log_data: 30 files
* songplays: 6820
* (unique) user: 97
* songs: 71
* artists: 69
* songplays with an artist included in artist table: 1 (song_id = SOZCTXZ12AB0182364, artist_id = AR5KOSW1187FB35FF4)

Project builds an ETL pipeline (Extract, Transform, Load) to create the DB and tables, fetch data from JSON files, process the data, and insert the the data to DB. As technologies, Project-1 uses python, SQL, Postgresql DB.

---

## About Database

Sparkify analytics database (called here sparkifydb) schema has a star design. Start design means that it has one Dimension Table having business data, and supporting Fact Tables. Dimension Table answers one of the key questions: what songs users are listening to. DB schema is the following:

![SparkifyDB schema as ER Diagram](https://udacity-reviews-uploads.s3.us-west-2.amazonaws.com/_attachments/33760/1602143181/Song_ERD.png)

_*SparkifyDB schema as ER Diagram.*_

### Fact Table

* **songplays**: song play data together with user, artist, and song info (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

### Dimension Tables

* **users**: user info (columns: user_id, first_name, last_name, gender, level)
* **songs**: song info (columns: song_id, title, artist_id, year, duration)
* **artists**: artist info (columns: artist_id, name, location, latitude, longitude)
* **time**: detailed time info about song plays (columns: start_time, hour, day, week, month, year, weekday)

---

## HOWTO use

**Project has two scripts:**

* **create_tables.py**: This script drops existing tables and creates new ones.
* **etl.py**: This script uses data in ./data/song_data and ./data/log_data, processes it, and inserts the processed data into DB.

### Prerequisites

Python3 is recommended as the environment. The most convenient way to install python is to use Anaconda (https://www.anaconda.com/distribution/) either via GUI or command line.
Also, the following libraries are needed for the python environment to make Jupyter Notebook and Postgresql to work:

* _postgresql_ (+ dependencies) to enable sripts and Jupyter to connect to Postgresql DB.
* _jupyter_ (+ dependencies) to enable Jupyter Notebook.
* _ipython-sql_ (https://anaconda.org/conda-forge/ipython-sql) to make Jupyter Notebook and SQL queries to Postgresql work together. NOTE: you may need to install this library from command line.

### Run create_tables.py

Type to command line:

`python3 create_tables.py`

Output: Script writes _"Tables dropped successfully"_ and _"Tables created successfully"_ if all tables were dropped and created without errors.

### Run etl.py

Type to command line:

`python3 etl.py`

Output: Script crawls through all the data directories, tells how many files it has to process, and writes to console the progress of the script as it processes them through. After successfully processing through a directory, script summarised the results:

* _"All xx files processed OK in aaa/abc123"_ (e.g. data/song_data) and
* _"All xx files processed OK in aaa/def456"_ (e.g. data/log_data).

## Data cleaning process

`etl.py`works the following way to clean-up and process the source data:

* Scripts crawls through all source data JSON files.
* From each file in ./data/song_data directory, script selects songs table values to a song_data DataFrame and inserts them to songs table, and artist table values to artist_data DataFrame and inserts them to artists table.
* From each file in ./data/log*data directory, script filters items with NextSong value in page parameter. It then processes \_time_data* from ts parameter value to be inserted in _time_ table and _user_data_ to be inserted in _users_ table.
* ./data/song*data directory also contains data which is processed into \_songplay_data*. User_id and artist_id fields are fetched from users and artists table using song_select query. Other parameters are selected from log_data. Formed songplay_data data is finally inserted into songplays table.

## Other

Project-1 also contains the following files:

* **etl.ipynb**: Jupyter Notebook for interactively develop and run python code to be used in etl.py.
* **test.ipynb**: Jupyter Notebook for interactively run test SQL queries against used DB.

## Summary

Project-1 provides customer startup Sparkify tools to analyse their service data and help them answer their key business questions like _"What songs users are listening to"_.
