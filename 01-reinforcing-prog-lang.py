# Programming Fundementals: 

# # ''' Create an emotions dict, 
#  where the keys are the names of different human emotions 
#  and the values are the degree to which the emotion is being felt on a scale from 1 to 3. 
#  '''

emotions = {
    'sad': 1,
    'content': 2,
    'happy': 3
}

#Exercise 2 : class and characteristics

class Person: 

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions
    
    def how_are_you(self):
        if emotion(value) in emotions == 1:
            


cora = Person('Cora', 'happy') 
hugo = Person('Hugo', 'sad')
print(cora.emotions)
print(hugo.emotions)