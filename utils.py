import joblib
import pickle

title = "Recommendation System"
similarity = joblib.load("similarities.joblib")
with open('dataset.dat', 'rb') as file:
    df = pickle.load(file)

def recommend(item_name, top_n =5):
    result = []
    index = df[df['title']==item_name].index[0]
    responce = similarity[index]
    value = sorted(enumerate(responce), key= lambda x : x[1], reverse= True)[1:top_n+1]
    for i in value:
        result.append(df['title'][i[0]])
    return result
