def sumofk(list1,num):
    dict_={}
    for val in list1:
        value=num-val
        dict_[value]=0
        if val in dict_:
            return True

num=5
list1=[1,8,7,6,3,2,12]
print(sumofk(list1,num))