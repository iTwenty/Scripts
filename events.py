input_file_name=raw_input("input file : ")
r=open(input_file_name,"r+")


print "public enum ActionId {"
for line in r :
        row = line.split(",")
        output = row[0] + "( \"" + row[1] + "\", \"" + row[2] + "\"),"
        print output

print "}"
