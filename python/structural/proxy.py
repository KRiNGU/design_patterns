from abc import ABC, abstractmethod


class DBAccessI(ABC):
    @abstractmethod
    def getData(self):
        pass


class DBAccess(DBAccessI):
    data: str = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data


class DBAccessProxy(DBAccessI):
    db_access: DBAccess = None
    password: str = None

    def __init__(self, db_access, password):
        self.db_access = db_access
        self.password = password

    def getData(self, password):
        if (self.password != password):
            return('Access denied.')
        return self.db_access.getData()

    def setData(self, data, password):
        if (self.password != password):
            print('Access denied.')
            return
        self.db_access.setData(data)


db_access: DBAccessI = DBAccess()
db_access_proxy: DBAccessI = DBAccessProxy(db_access, 'password')
db_access_proxy.setData('data', 'password')
print('Input wrong password:')
print(db_access_proxy.getData('wrong'))
print('Input correct password:')
print('data: ', db_access_proxy.getData('password'))
