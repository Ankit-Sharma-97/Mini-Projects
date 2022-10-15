# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class teachers:
    valu=2
    def __init__(self,name,age,salary):
        self.n=name
        self.a=age
        self.s=salary
    def get_salary(self):
        return self.s
class college:
    def __init__(self,name,max_teachers):
        self.name=name
        self.max_teachers=max_teachers
        self.teachers=[]
    def add_teacher(self,teacher):
        if len(self.teachers) < self.max_teachers:
            self.teachers.append(teacher)
            return True
        else :
            return False
            
    def avg_teacher(self):
        summ=0
        for i in self.teachers:
            summ=summ+i.s
        return summ/len(self.teachers)
t=teachers("ankit",24,2000)
t1=teachers("robot",23,1000)
t2=teachers("robot",23,1000)
c1=college("jnu",2)
c1.add_teacher(t)
print(c1.add_teacher(t1))
print(c1.add_teacher(t2))
c1.avg_teacher()
