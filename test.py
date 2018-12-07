import sys
file = sys.argv[1]
input = open(file, 'r')
output= open('output.txt', 'w')
for line in input:
    s = line.split(',')
    l= str(s[1]) + "," +str(s[0])+ "," + str(s[3]) + "," + str(s[2]) + ","+ str(s[5]) + "," + str(s[4]) + "," + str(int(s[7])) + "," + str(s[6])
    output.write(l)
    output.write("\n")

