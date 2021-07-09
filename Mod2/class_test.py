class MyClass:
    myClassVariable = ["Hello"]

    def __init__(self):
        self.myInstanceVariable=[1,2,3]

object1 = MyClass()
object2 = MyClass()



#print("---a")
#object1.myClassVariable = ["Hello","World"]
#print(object1.myClassVariable)
#print(object2.myClassVariable)
#print(MyClass.myClassVariable)

#print("---b")
#object1.myClassVariable.append("World")
#print(object1.myClassVariable)
#print(object2.myClassVariable)
#print(MyClass.myClassVariable)

#print("---c")
#MyClass.myClassVariable = ["Hello", "World"]
#print(object1.myClassVariable)
#print(object2.myClassVariable)
#print(MyClass.myClassVariable)

print("---d")
object1.myInstanceVariable.append(4)
print(object1.myInstanceVariable)
print(object2.myInstanceVariable)


