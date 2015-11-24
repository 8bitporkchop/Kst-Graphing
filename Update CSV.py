import datetime
import random


for i in range(5):
	timee = int(round(random.randint(1000,6000),2))

	click = True
	with open("test.csv","r+") as CSV:
		lastline=len(CSV.readlines()) -1
		CSV.seek(0)
		for i,line in enumerate(CSV):
			if i == lastline:
				time_stamp =  line[:8]
				if line[23] == 'C':
					click = False
				
		t1 = datetime.datetime.strptime(time_stamp, '%H:%M:%S')
		t = datetime.timedelta(milliseconds=timee*10)
		final = t1 + t
		new_timestamp = final.strftime("%H:%M:%S")
		if click:
			string = "%s,%s,system A Cliick record,machine10002,1,1" % (new_timestamp,timee)
			CSV.write(string + "\n")
		else:
			string = "%s,%s,system A Login,machine10002,1,1" % (new_timestamp,timee)
			CSV.write(string + "\n")


	