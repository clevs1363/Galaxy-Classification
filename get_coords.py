import csv
import sys

if len(sys.argv) < 2:
    print("Please include the number of lines to parse as a command line input.")
    exit(0)

if not(sys.argv[1].isdigit()):
    print("Please provide the number of lines to parse as an integer.")
    exit(0)

num_lines = int(sys.argv[1])
data = []
with open("gz2_hart16.csv") as f:
        reader = csv.DictReader(f) # automatically skips header line

        count = 0
        for row in reader:
            data.append((row['ra'], row['dec']))
            count += 1
            if count >= num_lines:
                  break

with open("coords_list.csv", 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)

# with open('coords_list.txt','w') as file:
#     for line in data:
#         file.write(line)
#         file.write('\n')