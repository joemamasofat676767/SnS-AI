from random import choices
import json

try:
    with open("knowledge.json", "r") as file:
        knowledge = json.load(file)
except:
    with open("knowledge.json", "w") as file:
        json.dump({}, file)
        knowledge = {}

temp = 0.3
ValidChar = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",
             "r","s","t","u","v","w","x","y","z"," ","."}
text = "obama love fried chicken. obama is sigma. he is good."
text = text.lower()
text = text.split(".")
vocab = set()

def filter(text):
    FinalText = []
    for sentance in text:
        filtered = sentance
        for letter in sentance:
            if not letter in ValidChar: filtered = filtered.replace(letter,"")
        FinalText.append(filtered)
    return FinalText
    
def CalcChance(vect, multi):
    ChanceMulti = 1 / multi
    return [abs(item ** ChanceMulti) for item in vect.values()]

class words:
    def __init__(self, word):
        self.word = word
        try:
            self.next = knowledge[word]
        except:
            self.next = {}
        
    def predict(self):
        next_choices = list(self.next.keys())
        if next_choices:
            print(self.next)
            return choices(next_choices, weights=CalcChance(self.next, temp))[0]
        return ""
    
FirstIter = True
for sentance in filter(text):
    words_in_sentence = sentance.split()
    if not words_in_sentence:
        continue
        
    for word in words_in_sentence:
        if word not in vocab:
            knowledge[word] = words(word)
            vocab.add(word)
        if FirstIter:
            LastWord = word
            FirstIter = False
            continue
        if word not in knowledge[LastWord].next:
            knowledge[LastWord].next[word] = 1
        else:
            knowledge[LastWord].next[word] += 1
        LastWord = word
    FirstIter = True

predicted = "obama"
sentance = predicted + " "
finished = False

while not finished:
    if predicted in knowledge:
        next_word = knowledge[predicted].predict()
        if next_word != "":
            predicted = next_word
            sentance += predicted + " "
        else:
            finished = True
    else:
        finished = True

with open("knowledge.json", "w") as file:
    KnowledgeDump = {}
    for key in knowledge.keys():
        KnowledgeDump[key] = knowledge[key].next
    json.dump(KnowledgeDump, file, indent=2)
    
print(sentance)
