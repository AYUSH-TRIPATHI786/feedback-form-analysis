from monkeylearn import MonkeyLearn


def sentiment(s):

	ml = MonkeyLearn('9ad4bee6b5e1a1f32ba54b9c4c68528e5d465442')
	data = [s]
	model_id = 'cl_pi3C7JiL'
	result = ml.classifiers.classify(model_id, data)
	li = (result.body)

	#li is in the below format:
	#[
	#   {
	#     "text": "This is a great app!",
	#     "external_id": null,
	#     "error": false,
	#     "classifications": [
	#       {
	#         "tag_name": "Positive",
	#         "tag_id": 33767179,
	#         "confidence": 0.998
	#       }
	#     ]
	#   }
	# ]
	
	li = li[0]['classifications'][0]
	if li['tag_name']=='Positive':
 		return li['confidence']
	else:
		return 1-li['confidence']

#list of answers given in a feedback form
feedback = ["This is a great app!"]


for i,s in enumerate(feedback):
	#if element in feedback list is string if runs sentiment function and give a rating out of 1.
	if type(s) == str:
		feedback[i] = sentiment(s)

#print the average of the ratings
print(sum(feedback)/len(feedback))



