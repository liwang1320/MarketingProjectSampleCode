
import pandas as pd
import math 

dataSet = pd.read_csv('HighNoteData.csv')

#if data is not available it is given a "NaN"
#math.isnan returns True if the value is NaN
#delta2 shouts have no vals

#Vector: ['age', 'male', 'friend_cnt', 'avg_friend_age', 'avg_friend_male', 'friend_country_cnt', 'subscriber_friend_cnt', 'songsListened', 'lovedTracks', 'posts', 'playlists', 'shouts', 'delta1_friend_cnt', 'delta1_avg_friend_age', 'delta1_avg_friend_male', 'delta1_friend_country_cnt', 'delta1_subscriber_friend_cnt', 'delta1_subscriber_friend_cnt', 'delta1_songsListened', 'delta1_lovedTracks', 'delta1_posts', 'delta1_playlists', 'delta1_shouts', 'tenure', 'good_country', 'delta1_good_country', 'delta2_friend_cnt', 'delta2_avg_friend_age', 'delta2_avg_friend_male', 'delta2_friend_country_cnt', 'delta2_subscriber_friend_cnt', 'delta2_songsListened', 'delta2_lovedTracks', 'delta2_posts', 'delta2_playlists', 'delta2_good_country']
#Output: adopter
def parseAllRemoveIncomplete():
	age = dataSet['age']
	male = dataSet['male']
	friend_cnt = dataSet['friend_cnt']
	avg_friend_age = dataSet['avg_friend_age']
	avg_friend_male = dataSet['avg_friend_male']
	friend_country_cnt = dataSet['friend_country_cnt']
	subscriber_friend_cnt = dataSet['subscriber_friend_cnt']
	songsListened = dataSet['songsListened']
	lovedTracks = dataSet['lovedTracks']
	posts = dataSet['posts']
	playlists = dataSet['playlists']
	shouts = dataSet['shouts']
	delta1_friend_cnt = dataSet['delta1_friend_cnt']
	delta1_avg_friend_age = dataSet['delta1_avg_friend_age']
	delta1_avg_friend_male = dataSet['delta1_avg_friend_male']
	delta1_friend_country_cnt = dataSet['delta1_friend_country_cnt']
	delta1_subscriber_friend_cnt = dataSet['delta1_subscriber_friend_cnt']
	delta1_subscriber_friend_cnt = dataSet['delta1_subscriber_friend_cnt']
	delta1_songsListened = dataSet['delta1_songsListened']
	delta1_lovedTracks = dataSet['delta1_lovedTracks']
	delta1_posts = dataSet['delta1_posts']
	delta1_playlists = dataSet['delta1_playlists']
	delta1_shouts = dataSet['delta1_shouts']
	tenure = dataSet['tenure']
	good_country = dataSet['good_country']
	delta1_good_country = dataSet['delta1_good_country']
	delta2_friend_cnt = dataSet['delta2_friend_cnt']
	delta2_avg_friend_age = dataSet['delta2_avg_friend_age']
	delta2_avg_friend_male = dataSet['delta2_avg_friend_male']
	delta2_friend_country_cnt = dataSet['delta2_friend_country_cnt']
	delta2_subscriber_friend_cnt = dataSet['delta2_subscriber_friend_cnt']
	delta2_songsListened = dataSet['delta2_songsListened']
	delta2_lovedTracks = dataSet['delta2_lovedTracks']
	delta2_posts = dataSet['delta2_posts']
	delta2_playlists = dataSet['delta2_playlists']
	# delta2_shouts = dataSet['delta2_shouts']
	delta2_good_country = dataSet['delta2_good_country']

	adopter = dataSet['adopter']

	numVectors = len(dataSet['net_user']) #number of vectors there are 
	# numVectors = 200

	Y = []
	X = []
	numVectors = 3
	for i in range(numVectors):
		output = adopter[i]
		# print("im here")

		if (not math.isnan(output)):
			# print("im here")
			inputVector = []
			inputVector.append(age[i])
			inputVector.append(male[i])
			inputVector.append(friend_cnt[i])
			inputVector.append(avg_friend_age[i])
			inputVector.append(avg_friend_male[i])
			inputVector.append(friend_country_cnt[i])
			inputVector.append(subscriber_friend_cnt[i])
			inputVector.append(songsListened[i])
			inputVector.append(lovedTracks[i])
			inputVector.append(posts[i])
			inputVector.append(playlists[i])
			inputVector.append(shouts[i])
			inputVector.append(delta1_friend_cnt[i])
			inputVector.append(delta1_avg_friend_age[i])
			inputVector.append(delta1_avg_friend_male[i])
			inputVector.append(delta1_friend_country_cnt[i])
			inputVector.append(delta1_subscriber_friend_cnt[i])
			inputVector.append(delta1_subscriber_friend_cnt[i])
			inputVector.append(delta1_songsListened[i])
			inputVector.append(delta1_lovedTracks[i])
			inputVector.append(delta1_posts[i])
			inputVector.append(delta1_playlists[i])
			inputVector.append(delta1_shouts[i])
			inputVector.append(tenure[i])
			inputVector.append(good_country[i])
			inputVector.append(delta1_good_country[i])
			inputVector.append(delta2_friend_cnt[i])
			inputVector.append(delta2_avg_friend_age[i])
			inputVector.append(delta2_avg_friend_male[i])
			inputVector.append(delta2_friend_country_cnt[i])
			inputVector.append(delta2_subscriber_friend_cnt[i])
			inputVector.append(delta2_songsListened[i])
			inputVector.append(delta2_lovedTracks[i])
			inputVector.append(delta2_posts[i])
			inputVector.append(delta2_playlists[i])
			# inputVector.append(delta2_shouts[i])
			inputVector.append(delta2_good_country[i])

			# print("new vect")
			noNan = True
			for k in inputVector:
				if (math.isnan(k)):
					# print("this vec is no good")
					noNan = False
			if (noNan):
				Y.append(output)
				X.append(inputVector)
	return X, Y





# 

print(parseAllRemoveIncomplete())