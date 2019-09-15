import pymongo
import random

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["election"]
mycol = mydb["candidate_keyword"]

people = ["Cristinao Ronaldo","Leo Messi","Sergio Ramos","Gareth Bale","Toni Kroos","Luka Modric","Eden Hazard","Neymar JR."]
text = "I know your eyes in the morning sun I feel you touch my hand in the pouring rain And the moment that you wander far from me I wanna feel you in my arms again And you come to me on a summer breeze Keep you warm in your love then you softly leave And me you need to show How deep is your love"
keywords = text.split()

candidates = []

size = 1000

def generatePersonId(name):
    return name.replace(" ","").lower()

def generateKeyword():
    for i in range(500):
        person = random.choice(people)
        candidates.append({
            "person_id":generatePersonId(person),
            # "name": person,
            "text": random.choice(keywords),
            "value": random.randint(1,60)
        })

    mycol.insert_many(candidates)

def createCandidateInfo():
    infoCol = mydb['candidate_info']
    cans_info = []
    for person in people:
        cans_info.append({
            "person_id" : generatePersonId(person),
            "name" : person
        })
    infoCol.insert_many(cans_info)


if __name__ == "__main__":
    createCandidateInfo()


# print(candidates)
# print("ok created Data")

