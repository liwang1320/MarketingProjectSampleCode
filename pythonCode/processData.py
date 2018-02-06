import numpy as np
import pandas as pd
import math

fbFile = pd.read_csv("fb_by_hour2.csv")
revFile = pd.read_csv('rev_by_hour2.csv')

#processes the FB data and re-writes it to a new csv file
#hour index should be an integer
#delete avg. session and pages/session
#input gaps with averages of the 2 surround days
def processFBData():
	numEntries = len(fbFile['Social Network']) #number of entries
	hourIndexOld = fbFile['Hour Index']
	sessionsOld = fbFile['Sessions']
	pageviewsOld = fbFile['Pageviews']

	lastHourIndex = hourIndexOld[0]

	hourIndexNew = [hourIndexOld[0]] #list with the old value as its first value
	sessionsNew = [sessionsOld[0]]
	pageviewNew = [pageviewsOld[0]]

	for i in range(1, numEntries):
		thisHour = hourIndexOld[i]
		if isinstance(thisHour, str):
			thisHour = int(thisHour)
			#convert hour index to int, if it is a string

		if isinstance(thisHour, int):
			#Already an int, ready to do stuff (we check this regardless of step 1)
			if (thisHour > lastHourIndex+2):
				print("We have a problem")
			if (thisHour==lastHourIndex+2):
				# we are disontinuous from the previous hour
				# we add an approx in between the 2 values
				midHour = (lastHourIndex + thisHour)/2
				midSessions = (sessionsOld[i-1] + sessionsOld[i])/2
				midPageviews = (pageviewsOld[i-1] + [pageviewsOld[i]])/2

				hourIndexNew.append(midHour)
				sessionsNew.append(midSessions)
				pageviewNew.append(midPageviews)

			#we add the old to the new
			hourIndexNew.append(thisHour)
			sessionsNew.append(sessionsOld[i])
			pageviewNew.append(pageviewsOld[i])

			lastHourIndex = thisHour

	allData = {'HourIndex' : hourIndexNew, 'Sessions' : sessionsNew, 'Pageviews' : pageviewNew}
	vectorload = pd.DataFrame(allData, columns=['HourIndex', 'Sessions', 'Pageviews'])
	vectorload.to_csv('fb_data_processed')

processFBData()













