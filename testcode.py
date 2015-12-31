# from multiprocessing import Pool
import sys
import csv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# These globals represent corresponding index locations inside the CSV.
NPI_FIELD = 0
LAST_NAME_FIELD = 5
FIRST_NAME_FIELD = 6
MIDDLE_NAME_FIELD = 7
TAXONOMY_FIELD = 47
LICENSE_FIELD = 48
STREET_1_FIELD = 28
STREET_2_FIELD = 29
CITY_FIELD = 30
STATE_FIELD = 31
ZIP_CODE_FIELD = 32

taxonomy_dict = {}

client = MongoClient()
db = client.testdb
coll = db.testcollection


def build_taxonomy_dict(taxonomy_csv):
    with open(taxonomy_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            taxonomy_dict[row[0]] = row[1]


def build_doctor_dict(doctors_csv):
    with open(doctors_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            try:
                taxonomy = row[TAXONOMY_FIELD]
                taxonomy_description = taxonomy_dict[taxonomy]

                # TODO: Still need to import address information
                doctor_dict = {'NPI': row[NPI_FIELD],
                               'Last Name': row[LAST_NAME_FIELD],
                               'First Name': row[FIRST_NAME_FIELD],
                               'Middle Name': row[MIDDLE_NAME_FIELD],
                               'License': row[LICENSE_FIELD],
                               'Taxonomy': taxonomy,
                               'Specialization': taxonomy_description}
                coll.insert(doctor_dict)
            except:
                # TODO: exception handling needed
                pass


def main(argv):
    if not len(argv) == 2:
        # Usage text reflects test data
        print("Usage: parse_doctors.py <doctors_test.csv> <taxonomy_test.csv>")
    else:
        try:
            # TODO: is this part needed?
            #client = MongoClient()
            print ("Connected to MongoDB successfully.")
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        build_taxonomy_dict(argv[1])
        build_doctor_dict(argv[0])

        client.close()


if __name__ == "__main__":
    main(sys.argv[1:])
