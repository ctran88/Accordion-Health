from multiprocessing import Pool

# These globals represent corresponding index locations inside the CSV we parse.
NAME_AND_TITLE_FIELD = 1
TAXONOMY_FIELD = 47

class USAddress:
    """ A simple address data structure """
    street_1 = ""
    street_2 = ""
    city     = ""
    state    = ""
    zip_code = ""

class MedicalDoctor:
    """ A simple doctor data structure """
    name_and_title = ""
    address        = USAddress()
    taxonomy       = ""
    specialization = ""
    tags           = ""

    def __init__(self, taxonomy, specialization, tags):
        self.taxonomy       = taxonomy
        self.specialization = specialization
        self.tags           = tags

taxonomies = {'207X00000X': MedicalDoctor('207X00000X', 'Orthopaedic Surgery', ['trauma', 'sports injuries', 'degenerative disease', 'infection', 'tumor', 'congenital disorder'])}

def parse_line(line):
    items = line.split(',')

    try:
        doctor = taxonomies[items[TAXONOMY_FIELD]]
        doctor.name_and_title = "test"
        return doctor

    except:
        # Taxonomy not found in list
        return None

fp = open("/Users/THANATOS/Downloads/test.csv")
for i, line in enumerate(fp):
    parse_line(line)
fp.close()