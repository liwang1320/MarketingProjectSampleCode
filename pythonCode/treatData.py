#We will have 10% of people increase their playlist number by 1

import pandas as pd
import math
import random  

dataSet = pd.read_csv('HighNoteData.csv')

columns = ['net_user', 'age', 'male', 'friend_cnt', 'avg_friend_age', 'avg_friend_male', 'friend_country_cnt', 'subscriber_friend_cnt', 'songsListened', 'lovedTracks', 'posts', 'playlists', 'shouts', 'delta1_friend_cnt', 'delta1_avg_friend_age', 'delta1_avg_friend_male', 'delta1_friend_country_cnt', 'delta1_subscriber_friend_cnt', 'delta1_subscriber_friend_cnt', 'delta1_songsListened', 'delta1_lovedTracks', 'delta1_posts', 'delta1_playlists', 'delta1_shouts', 'adopter', 'tenure', 'good_country', 'delta1_good_country', 'delta2_friend_cnt', 'delta2_avg_friend_age', 'delta2_avg_friend_male', 'delta2_friend_country_cnt', 'delta2_subscriber_friend_cnt', 'delta2_songsListened', 'delta2_lovedTracks', 'delta2_posts', 'delta2_playlists', 'delta2_shouts', 'delta2_good_country']

columnsToTreat = {'subscriber_friend_cnt': 0.99} 
#dictionary of which columns we are treating and by what percentage we raise the param by 1

treatedData = {}

for column in columns:
	listOfColumnsToTreat = columnsToTreat.keys()
	if column not in listOfColumnsToTreat:
		treatedData[column] = dataSet[column]
	else:
		oldValues = dataSet[column]
		newValues = []
		percentTreat = columnsToTreat[column]


		for i in oldValues:

			randFloat = random.random()
			newVal = i
			if not math.isnan(i): 
				if randFloat < percentTreat:
					newVal = i+1

			newValues.append(newVal)

	
		treatedData[column] = newValues

# print("treated number of playlists total")
# print(sum(treatedData['playlists']))
# print("number of original playlists total")
# print(sum(dataSet['playlists']))

vectorLoad = pd.DataFrame(treatedData, columns = columns)
vectorLoad.to_csv('SFCTreated99.csv')




