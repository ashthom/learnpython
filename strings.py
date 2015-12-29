import re;

fname='C:\\temp\\mbox-short.txt'



fh = open(fname);
confidence_list = list();

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    counter=counter+1
    confidence=re.findall('.*: ([0-9]\.[0-9]+)', line)
    confidence_list.extend(confidence)

print 'Average spam confidence:', sum(map(float,confidence_list))/len(confidence_list);



