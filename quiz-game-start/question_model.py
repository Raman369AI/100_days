import data
import random


class Question:
    def __init__(self,qtext,qanswer):
        self.text = qtext
        self.answer = qanswer

m=Question('Raman',"True")
print(m.text)
print(m.answer)



