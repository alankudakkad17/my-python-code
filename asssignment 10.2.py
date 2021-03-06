#"""10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""


#Use mbox-short.txt File name

name = input("Enter file:")
f = open(name)
dic = {}
for i in f:
    if i.startswith("From") and len(i.split()) > 2:
        line = i.split()
        if not dic.has_key(line[5][:2]):
            dic[line[5][:2]] = 1
        else:
            dic[line[5][:2]] += 1
                
key = sorted(dic)
for i in key:
    print (i, dic[i])
