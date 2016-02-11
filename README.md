# Accordion-Health

This repository is used to track updates and show my progression for my interview project for Accordion Health.

###### Dependencies:
- [Python 2.7.11] (https://www.python.org/downloads/)
- [MongoDB] (https://www.mongodb.org/downloads#production)
- [Node.js] (https://nodejs.org/en/download/)
- [Full Replacement Monthly NPI File] (http://download.cms.gov/nppes/NPI_Files.html)

###### Preparing Python and MongoDB:
1. Install the PyMongo package via the command line with **C:\Python27\python.exe -m pip install pymongo**.
2. Script assumes that Python is installed at the default location: C:\Python27.
3. Follow the steps [here] (https://docs.mongodb.org/manual/administration/install-community/) to properly setup MongoDB.

###### To initialize database:
1. Unzip the Full Replacement Monthly NPI File and place **npidata_20050523-20151213.csv** in the **Back-end** folder.
2. Initialize MongoDB server by typing **cd (mongodb installation dir)/bin/mongod** in the command line.
3. Double-click **init.sh** (Mac users) or **init.bat** (Windows users).

###### To run local instance of map:
1. Double-click **localrun.sh** (Mac users) or **localrun.bat** (Windows users).
2. Open browser and go to **localhost:8000**.
