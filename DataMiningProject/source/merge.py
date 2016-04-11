fout=open("data/raw_tweets.csv","a")
# first file:
for line in open("data/raw.csv"):
    fout.write(line)
# now the rest:
for num in range(1,1):
    f = open("data/raw1"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()