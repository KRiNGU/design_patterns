class Singletone(object):
    instance = None
    value = None

    def __new__(self, value):
        if self.instance is None:
            self.instance = object.__new__(self)
            self.value = value
        return self.instance


firstInitialize = Singletone('Im first initializatin.')
print('First initialize: ', firstInitialize.value)
secondInitialize = Singletone('Im second initializatin.')
print('Second initialize: ', secondInitialize.value)
print('Are they equal without overloading __eq__ method?',
      firstInitialize == secondInitialize)
print('As we can see they are equal. It is because they both reffer one memory area.')
