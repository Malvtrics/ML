import pickle

class myobject:
    def __init__(self,x,y):
        self.x = x
        self.y = y

obj = myobject(100,200)
s_obj = pickle.dumps(obj)
print(type(s_obj))
print(s_obj)

obj2 = pickle.loads(s_obj)
print(type(obj2))
print(obj2.x,obj2.y)