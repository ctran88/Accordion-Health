# Accordion-Health

This repository is used to track updates and show my progression for my interview project for Accordion Health.

###### Dependencies:
- [Python 2.7.11] (https://www.python.org/downloads/)
- [MongoDB] (https://www.mongodb.org/downloads#production)
- [Node.js] (https://nodejs.org/en/download/)
- [Full Replacement Monthly NPI File] (http://download.cms.gov/nppes/NPI_Files.html)


###### To initialize database:

1. Make sure PyMongo package is installed.  If not, install via the command line with **python -m pip install pymongo**.
2. Unzip the Full Replacement Monthly NPI File and place **npidata_20050523-20151213.csv** file in the **Back-end** folder.
3. Double-click **init.sh**.

###### To run local instance of map:

1. Double-click **localrun.sh**.
2. Open browser and go to **localhost:8000**.