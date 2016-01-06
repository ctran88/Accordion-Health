# Start mongo client, connects to windows service server
C:\mongodb\bin\mongo.exe

# Import .csv file to new database
C:\mongodb\bin\mongoimport -d NPPES -c test --type csv --file test.csv --headerline

# Testing mongo query for doctors in test collection
db.test.find({"Provider Credential Text":{$regex: /M.?D/}}, {"NPI":1, "Provider Last Name (Legal Name)":1, "Provider First Name":1, "Provider Middle Name":1, "Provider Credential Text":1}).pretty()

