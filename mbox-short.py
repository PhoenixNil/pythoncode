# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    k = line.find('0')
    total += float(line[k:])
    count = count + 1
print('Average spam confidence:', total / count)
