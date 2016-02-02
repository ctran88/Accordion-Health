import multiprocessing as mp
import os
import sys
import csv
import time
from pymongo import MongoClient

# Constants for coordinates function
ZIP = 0
COORD_START = 3

# Constants for taxonomy function
TAX_CODE = 0
TAX_DESC = 1

# Constants for doctor function
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

# Global MongoDB variables
client = MongoClient()
db = client.NPPES
coll = db.NPI_collection

# Global coordinate and taxonomy dictionaries
coord_dict = {}
taxonomy_dict = {}


# This function builds a dictionary to reference all US city coordinates
def build_coord_dict(coord_csv):
    start = time.time()
    with open(coord_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            key = row[ZIP]
            if key in coord_dict:
                pass
            coord_dict[key] = row[COORD_START:]
    end = time.time()
    print 'Time to build coord_dict:', end-start


# This function builds a dictionary to reference all January 2016 taxonomy codes
def build_taxonomy_dict(taxonomy_csv):
    start = time.time()
    with open(taxonomy_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            taxonomy_dict[row[TAX_CODE]] = row[TAX_DESC]
    end = time.time()
    print 'Time to build taxonomy_dict:', end-start


# This function builds one dictionary per doctor and attaches the corresponding coordinates before sending to database
def build_doctor_dict(doctors_csv):
    start = time.time()
    with open(doctors_csv) as fp:
        reader = csv.reader(fp)
        next(reader, None)
        for row in reader:
            try:
                taxonomy = row[TAXONOMY_FIELD]
                taxonomy_description = taxonomy_dict[taxonomy]

                # Fills initial doctor information
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
                                           'Zip Code': row[ZIP_CODE_FIELD][:5]}
                               }

                # Gets the coordinates for the doctor's city
                doc_zip = doctor_dict.get('Address', None).get('Zip Code', None)
                latitude = coord_dict[doc_zip][0]
                longitude = coord_dict[doc_zip][1]

                # Updates Address dictionary with coordinates
                doctor_dict['Address']['Latitude'] = latitude
                doctor_dict['Address']['Longitude'] = longitude

                # Insert into database
                coll.insert(doctor_dict)
            except (KeyError, RuntimeError):
                pass
    end = time.time()
    print 'Time to build doctor_dict:', end-start


def main(argv):
    if not len(argv) == 3:
        print("Usage: NPPES_parse.py <npidata_20050523-20151213.csv> <taxonomy.csv> <coordinates.csv>")
    else:
        # file_size = os.path.getsize(argv[0])
        # split_size = 100*1024*1024
        #
        # if file_size > split_size:
        #     pool = mp.Pool(mp.cpu_count())
        #     cursor = 0
        #     results = []
        #     with open(argv[0]) as f:
        #         for chunk in xrange(file_size // split_size):
        #             if cursor + split_size > file_size:
        #                 end = file_size
        #             else:
        #                 end = cursor + split_size
        #
        #             f.seek(end)
        #             f.readline()
        #
        #             end = f.tell()
        #
        #             proc = pool.apply_async(func_wrapper, argv)
        #             results.append(proc)
        #
        #             cursor = end

        build_coord_dict(argv[2])
        build_taxonomy_dict(argv[1])
        build_doctor_dict(argv[0])

        client.close()

        print("Database setup complete.")


if __name__ == "__main__":
    main(sys.argv[1:])
