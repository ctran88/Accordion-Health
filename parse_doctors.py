from multiprocessing import Pool
import sys, getopt

# These globals represent corresponding index locations inside the CSV we parse.
# TODO: Add the field indexes we need
NPI_FIELD = 0
LAST_NAME_FIELD = 5
FIRST_NAME_FIELD = 6
MIDDLE_NAME_FIELD = 7
TAXONOMY_FIELD = 47
LICENSE_FIELD = 48

taxonomy_dict = {}


class USAddress:
    """ A simple address data structure """
    street_1 = ""
    street_2 = ""
    city = ""
    state = ""
    zip_code = ""


class MedicalDoctor:
    """ A simple doctor data structure """
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


def build_taxonomy_dict(taxonomy_csv):
    fp = open(taxonomy_csv)
    for i, line in enumerate(fp):
        if not i == 0:
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

            doctor = MedicalDoctor(taxonomy, taxonomy_description)

            #TODO: Fill in the address and name information of the doctor struct

            # insert into DB
        except:
            # Taxonomy not found in list
            pass
    fp.close()


def main(argv):
    if not len(argv) == 2:
        print("Useage: parse_doctors.py <doctors.csv> <taxonomy_codes.csv>")
    else:
        build_taxonomy_dict(argv[1])
        parse_doctors(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
