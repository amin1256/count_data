import csv
counter = {}


def poll (input_file_name):
    with open (input_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            for word in row[1:]:
                if word not in counter:
                    counter[word] = 0
                counter[word] +=1
    print(counter)

print(poll(input_file_name))                    

                