# Assignment: MathDojo

class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for a in i:
                    self.total += a
            else:
                self.total += i
        return self

    def subtract(self, *args):
        for a in args:
            if type(a) == list or type(a) == tuple:
                for x in a:
                    self.total -= x
            else:
                self.total -= a
        return self

    def result(self):
        print self.total

md = MathDojo()

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()