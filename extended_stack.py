class ExtendedStack(list):
    def check(self):
        print(self)
        return len(self) >=2

    def sum(self):
        if self.check():
            result=self[-1]+self[-2]
            del self[-2::]
            self.append(result)

    def sub(self):
         if self.check():
            result=self[-1]-self[-2]
            del self[-2::]
            self.append(result)

    def mul(self):
         if self.check():
            result=self[-1]*self[-2]
            del self[-2::]
            self.append(result)

    def div(self):
         if self.check() and self[-2]!=0:
            result=self[-1]//self[-2]
            del self[-2::]
            self.append(result)
