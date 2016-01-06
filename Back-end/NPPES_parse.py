# from multiprocessing import Pool
import sys
import csv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

TAX_CODE = 0
TAX_DESC = 1

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

client = MongoClient()
db = client.testdb2
coll = db.testcollection

coord_dict = {}
taxonomy_dict = {}


def build_coord_dict(coord_csv):
    with open(coord_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            state = row[0]
            coord_dict.setdefault(state, []).append(row[1:])
        """for keys, values in coord_dict.items():
            print(keys)
            print(values)"""


def build_taxonomy_dict(taxonomy_csv):
    with open(taxonomy_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            taxonomy_dict[row[TAX_CODE]] = row[TAX_DESC]


def build_doctor_dict(doctors_csv):
    with open(doctors_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            try:
                taxonomy = row[TAXONOMY_FIELD]
                taxonomy_description = taxonomy_dict[taxonomy]

                doctor_dict = {'NPI': row[NPI_FIELD],
                               'Last Name': row[LAST_NAME_FIELD],
                               'First Name': row[FIRST_NAME_FIELD],
                               'Middle Name': row[MIDDLE_NAME_FIELD],
                               'License': row[LICENSE_FIELD],
                               'Taxonomy': taxonomy,
                               'Specialization': taxonomy_description,
                               'Address': {'Street_1': row[STREET_1_FIELD],
                                           'Street_2': row[STREET_2_FIELD],
                                           'City': row[CITY_FIELD],
                                           'State': row[STATE_FIELD],
                                           'Zip Code': row[ZIP_CODE_FIELD]}
                               }

                coord_state = doctor_dict.get('Address', None).get('State', None)
                coord_city = doctor_dict.get('Address', None).get('City', None)
                lat = coord_dict[coord_state][coord_city]
                # lng = coord_dict[coord_state][coord_city]
                # coll.insert(doctor_dict)
            except:
                # TODO: exception handling needed
                pass


def main(argv):
    if not len(argv) == 3:
        print("Usage: NPPES_parse.py <doctors_csv.csv> <taxonomy_csv.csv> <coordinates_csv.csv>")
    else:
        try:
            # TODO: is this part needed?
            # client = MongoClient()
            print ("Connected to MongoDB successfully.")
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        build_coord_dict(argv[2])
        build_taxonomy_dict(argv[1])
        build_doctor_dict(argv[0])

        client.close()


if __name__ == "__main__":
    main(sys.argv[1:])
