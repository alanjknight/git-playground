class Student(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print("Get Value")
        return self._age

    @age.setter
    def age(self, value):
        print("Set Value")
        if value <0:
            raise ValueError("Age below 0 is not allowed")
        self._age=value


st = Student("Mark",20)
print(st.age)
st.age=25
print(st.age)
