class TempoMixn:
    def method(self):
        print(self.arg)


class A(TempoMixn):
    def __init__(self):
        self.arg = 123
    
    def call(self):
        self.method()


class B(TempoMixn, A):
    def __init__(self):
        self.arg = 234
    
    def fight(self):
        self.method()
        self.call()
