from astroquery.sdss import SDSS
import json

"""
Table column names:
    Elliptical:   t01_smooth_or_features_a01_smooth_flag == 1
    Edge-on Disk: t02_edgeon_a04_yes_flag                == 1
    Oblique Disk: t02_edgeon_a05_no_flag                 == 1
    Spiral Disk:  t04_spiral_a08_spiral_flag             == 1
    Ring:         t08_odd_feature_a19_ring_flag          == 1
    Merger:       t08_odd_feature_a24_merger_flag        == 1
"""

# 0: Elliptical, 1: Edge-on Disk, 2: Oblique Disk, 3: Spiral Disk, 4: Ring, 5: Merger
nums_to_classes = ["Elliptical", "Edge-on Disk", "Oblique Disk", "Spiral Disk", "Ring", "Merger"]
id_to_class = {} # map of galaxy IDs to their type

def get_galaxy_class_map(column_name, class_num):
    galaxies = SDSS.query_sql(f"SELECT dr8objid FROM zoo2MainSpecz WHERE {column_name} = 1")
    for galaxy in galaxies:
        id_to_class[str(galaxy["dr8objid"])] = class_num # json requires keys to be string

for i, class_columns in enumerate(["t01_smooth_or_features_a01_smooth_flag", "t02_edgeon_a04_yes_flag", "t02_edgeon_a05_no_flag", "t04_spiral_a08_spiral_flag", "t08_odd_feature_a19_ring_flag", "t08_odd_feature_a24_merger_flag"]):
    # print(class_columns)
    # print(i)
    print(f"Processing column {class_columns}")
    get_galaxy_class_map(class_columns, i)

# print(len(id_to_class))
with open('galaxy_class_labels.json', 'w', encoding='utf-8') as f:
    json.dump(id_to_class, f, ensure_ascii=False, indent=4)
