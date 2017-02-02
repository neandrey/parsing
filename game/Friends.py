class Friends:
    def __init__(self, connections):
        self.connections = list(connections)
#-------------------------------------------
    def add(self, connection):
        for i in self.connections:
            if i == connection:
                return False
        self.connections.append(connection)
        return True
#-------------------------------------------
    def remove(self, connection):
        for i in self.connections:
            if i == connection:
                self.connections.remove(i)
                return True
        #self.connections.append(connection)
        return False
#--------------------------------------------
    def names(self):
        a = (self.connections)[0]
        for i in self.connections:
            p = i | a
        (list(p)).sort()
        return set(p)
#----------------------------------------------
    def connected(self, name):
        a = set()
        for i in self.connections:
            if name in i:
                i.remove(name)
                a = a | i
        return a
#------------------------------------------------

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.names() == {"nikola", "sophia", "robot", "pilot", "stephen"}
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"