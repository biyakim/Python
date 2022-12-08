class Card:

    def __init__(self,number,kind):
        if 1<=number<=13:
            self.number=number
        else:
            print("경고")
        if kind =="heart" or kind =="diamond" or kind == "club" or kind =="spade":
            self.kind=kind
        else:
            print("경고")
