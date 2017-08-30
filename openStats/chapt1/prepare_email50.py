import csv
def xable(x):
    return headers.index(x)
with open('../Data from openintro.org/email50.txt', 'r') as dirty_50:
    headers = dirty_50.readline().replace('\n', '').split('\t')
    idxs = ['spam', 'num_char', 'line_breaks', 'format', 'number']
    interestKeys = [xable(i) for i in idxs]

    
    with open('../Data from openintro.org/email50.mine.txt', 'w') as clean_50:
        reading = csv.reader(dirty_50, delimiter='\t')
        writing = csv.writer(clean_50, delimiter='\t') 
        writing.writerow([headers[i] for i in interestKeys])
        for line in reading:
            writing.writerow([line[i] + " " *(len(headers[i]) - len(line[i]))  for i in interestKeys]) #stupid but fixed my OCD