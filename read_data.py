from collections import defaultdict
from pathlib import Path

import csv
import re
import json

'''
Takes the gz2 class string and returns the type of galaxy (used in Gonzalez et al 2018):
Possible galaxy types: Elliptical, Edge-on Disk, Oblique Disk, Spiral Disk, Ring, Merger
TODO: review inclusion of irregular galaxies
'''
def parse_galaxy_type(gz2_class):
    if gz2_class == 'A':
        return "Star"
    if gz2_class.endswith("(r)"):
        return "Ring"
    if gz2_class.endswith("(m)"):
        return "Merger"
    if gz2_class.startswith('E'):
        return "Elliptical"
    if gz2_class.startswith('S'):
        if gz2_class.startswith(("Ser", "Seb", "Sen")):
            return "Edge-on Disk"
        elif re.search(r"1|2|3|4|\+|\?", gz2_class):
            return "Spiral Disk"
        else:
            return "Oblique Disk"
    return gz2_class + ": Unsure" # above classes should be comprehensive, should not reach this point


'''
Takes in a dictionary and makes sure none of the galaxiers are of the "Unsure" type
'''
def validate_data(data):
    data_valid = True
    invalid_galaxies = []
    for galaxy_id, type in data.items():
        if type.endswith("Unsure"):
            data_valid = False
            invalid_galaxies.append((galaxy_id, type))
    
    return data_valid, invalid_galaxies

'''
Returns number of each type of galaxy in the data dictionary
'''
def class_nums(data):
    stats = defaultdict(int)
    for galaxy_id, type in data.items():
        stats[type] += 1
    return stats

'''
Writes classification map to file if file does not already exist, reads from file if already exists (faster than processing original data file)
'''
classification_file = Path("gz2_classifications.json")
if not classification_file.is_file():
    print("Classification file does not exist. Loading from source data file")
    with open("gz2_hart16.csv") as f:
        reader = csv.DictReader(f) # automatically skips header line
        data = {}

        for row in reader:
            data[int(row["dr7objid"])] = parse_galaxy_type(row["gz2_class"]) # adds to data dictionary using object ID as the key

        data_valid, invalid_galaxies = validate_data(data) # Makes sure there are no "Unsure" answers
        if not data_valid:
            print(invalid_galaxies)
            exit(0)
        else:
            print(class_nums(data))
            with open('gz2_classifications.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
else:
    print("Classification file exists. Loading it")
    f = open("gz2_classifications.json")
    data = json.load(f)
    print(class_nums(data))
    print(data['587732591714893851'])

# TODO: how to get SDSS data