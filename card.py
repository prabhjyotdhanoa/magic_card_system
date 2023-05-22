#description of card system
#https://docs.google.com/document/d/1fClkaQPMhDGGG1d-NNFrV7GBK0uJ0_AzPM2elNNpcv4/edit

"""
Card Types:
'Creature'
'Spell'

"""
class Card:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return repr(self.name + " " + self.type)
    



    