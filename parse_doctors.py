from multiprocessing import Pool

# These globals represent corresponding index locations inside the CSV we parse.
LAST_NAME_FIELD = 5
FIRST_NAME_FIELD = 6
MIDDLE_NAME_FIELD = 7
NPI_FIELD = 0
ORGANIZATION_FIELD = 4
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
	last_name      = ""
	first_name     = ""
	middle_name    = ""
	organization   = ""
    address        = USAddress()
	npi            = ""
    taxonomy       = ""
    specialization = ""
    tags           = ""

    def __init__(self, taxonomy, specialization, tags):
        self.taxonomy       = taxonomy
        self.specialization = specialization
        self.tags           = tags

# Possible taxonomy index structure
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