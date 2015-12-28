from multiprocessing import Pool
import sys, getopt
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


class USAddress(object):
    # A simple address data structure
    street_1 = ""
    street_2 = ""
    city = ""
    state = ""
    zip_code = ""

    # toString for address struct
    def __repr__(self):
        return """ Address:
                   %s %s
                   %s, %s %s """ % (self.street_1, self.street_2, self.city, self.state,
                                    self.zip_code)


class MedicalDoctor(object):
    # A simple doctor data structure
    first_name = ""
    last_name = ""
    middle_name = ""
    address = USAddress()
    taxonomy = ""
    specialization = ""
    npi = ""
    license = ""
    tags = ""

    def __init__(self, taxonomy, specialization):
        self.taxonomy = taxonomy
        self.specialization = specialization

    # toString for doctor struct
    def __repr__(self):
        return """ Doctor Information:
                   First Name: %s
                   Middle Name: %s
                   Last Name: %s
                   Taxonomy: %s
                   Specialization: %s
                   NPI: %s
                   License: %s """ % (self.first_name, self.middle_name,
                                      self.last_name, self.taxonomy,
                                      self.specialization, self.npi,
                                      self.license)


def build_taxonomy_dict(taxonomy_csv):
    fp = open(taxonomy_csv)
    for i, line in enumerate(fp):
        if not i == 0:
            line = line.rstrip()
            items = line.split(',')
            taxonomy_dict[items[0]] = items[1]
    fp.close()


def parse_doctors(doctors_csv):
    fp = open(doctors_csv)
    for i, line in enumerate(fp):
        try:
            items = line.split(',')
            taxonomy = items[TAXONOMY_FIELD]
            taxonomy_description = taxonomy_dict[taxonomy]
			
            # Fills out address class instance
            address = USAddress()
            address.street_1 = items[STREET_1_FIELD]
            address.street_2 = items[STREET_2_FIELD]
            address.city = items[CITY_FIELD]
            address.state = items[STATE_FIELD]
            address.zip_code = items[ZIP_CODE_FIELD]
			
            # Fills out doctor class instance
            doctor = MedicalDoctor(taxonomy, taxonomy_description)
            doctor.first_name = items[FIRST_NAME_FIELD]
            doctor.last_name = items[LAST_NAME_FIELD]
            doctor.middle_name = items[MIDDLE_NAME_FIELD]
            doctor.npi = items[NPI_FIELD]
            doctor.license = items[LICENSE_FIELD]
            # Attempting to convert into dictionary to persist to mongoDB
            doctor.__dict__
            
			# For validation of doctor and address information
            print doctor
            print address
            
			# insert into DB, needs work
            db.testCollection.insert(doctor)
        except:
            # Taxonomy not found in list
			# Proper exception handling?
            pass
    fp.close()


def main(argv):
    if not len(argv) == 2:
        # Useage text reflects test data
        print("Useage: parse_doctors.py <doctors_test.csv> <taxonomy_test.csv>")
    else:
        try:
            client = MongoClient()
            print ("Connected to MongoDB successfully.")
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)        

        db = client.testdb
		
        build_taxonomy_dict(argv[1])
        parse_doctors(argv[0])
		
        client.close()


if __name__ == "__main__":
    main(sys.argv[1:])
