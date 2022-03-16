import csv

with open("file_Handling/1st_csv.csv","r") as f:
    read=csv.reader(f)
    # read=list(read)
    # print(read)
    for data in read:
        for jdata in data:
            print(jdata,"\t",end="")
        print()
            
        