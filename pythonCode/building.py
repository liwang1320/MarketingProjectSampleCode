

# vec = ['age', 'male', 'friend_cnt', 'avg_friend_age', 'avg_friend_male', 'friend_country_cnt', 'subscriber_friend_cnt', 'songsListened', 'lovedTracks', 'posts', 'playlists', 'shouts', 'delta1_friend_cnt', 'delta1_avg_friend_age', 'delta1_avg_friend_male', 'delta1_friend_country_cnt', 'delta1_subscriber_friend_cnt', 'delta1_subscriber_friend_cnt', 'delta1_songsListened', 'delta1_lovedTracks', 'delta1_posts', 'delta1_playlists', 'delta1_shouts', 'tenure', 'good_country', 'delta1_good_country', 'delta2_friend_cnt', 'delta2_avg_friend_age', 'delta2_avg_friend_male', 'delta2_friend_country_cnt', 'delta2_subscriber_friend_cnt', 'delta2_songsListened', 'delta2_lovedTracks', 'delta2_posts', 'delta2_playlists', 'delta2_good_country']

# for i in vec:
# 	# print(i + " = dataSet['" + i + "']"  )
# 	print("inputVector.append(" + i + "[i])")

import pandas as pd
import math 

dataSet = pd.read_csv('HighNoteData.csv')

adopter = dataSet['adopter']


def findAOne(count):
	countOfAdopts = count
	for i in range(len(adopter)):
		if countOfAdopts==1:
			print("im here")
			return i

		if (adopter[i]==1):
			print("somone adopted")
			print()
			countOfAdopts+=1

print(findAOne(0))