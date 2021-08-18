#
# class cat :
#     name="catddd"
#     print(name)
# class dog(object):
#     name="dog"
#     print(name)
# x=cat
# y=dog
# print("cat",dir(x))
# print("dog",dir(y))


class Person:
    """
    不带object
    """
    name = "zhengtong"
    print(name)


class Animal(object):
    """
    带有object
    """
    name = "chonghong"
    print(name)


if __name__ == "__main__":
    x = Person()
    print("Person", dir(x))

    y = Animal()
    print("Animal", dir(y))

# if __name__=='__main__':

# 实现字符串添加到列表的函数
image_name_list = []
