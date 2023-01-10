import pickle

class Group:
    def __init__(self):
        self.group = [0, [0]]
    def getGroup(self):
        return self.group
    def addObject(self, obj):
        self.group.append(obj)
        self.group.append([obj])
    def removeObject(self, obj):
        if (obj in self.group) and (obj != 0):
            self.group.remove(obj)
            self.group.remove([obj])
        elif obj == 0:
            if self.group.count(0) > 1:
                self.group.remove(0)
                self.group.remove([0])
            else:
                print('You cannot remove the additive identity from a group')
        elif obj not in self.group:
            print('Objects must be members of a group to remove')
    def __str__(self):
        return 'Group: {}'.format(self.group)
    def __eq__(self, obj):
        return self.group == obj.group
    def add(self, obj1, obj2):
        if (obj1 in self.group) and (obj2 in self.group):
            if (obj1 == [obj2]) or (obj2 == [obj1]):
                self.group.append(0)
                self.group.append([0])
            else:
                if (type(obj1) == list) or (type(obj2) == list):
                    new_list = []
                    for x in [obj1, obj2]:
                        if type(x) is list:
                            for y in x:
                                new_list.append(y)
                        else:
                            new_list.append(x)
                    self.group.append(new_list)
                else:
                    self.group.append([obj1, obj2])
        else:
            print('Objects must be members of a group to add')

a = Group()
a.addObject('banana')

with open('group.pkl', 'wb') as f:
    pickle.dump(a, f)
    print('Pickling completed')

with open('group.pkl', 'rb') as f:
    obj = pickle.load(f)
    print('Unpickling completed')
    print(obj)
