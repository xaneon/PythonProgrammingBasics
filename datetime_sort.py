import datetime

d1=datetime.date(1988,2,23)
d2=datetime.date(1988,3,25)
d3=datetime.date(1988,2,24)

dates=sorted((d1,d2,d3))
print(dates)

myformat = '%d %b %Y'
print(d1.strftime(myformat))

teststrs=['17 Jan 1980', '14 Feb 1980']
ltest=[]

for t in teststrs:
	d=datetime.datetime.strptime(t, myformat)
	ltest.append(d)

print(sorted(ltest))

