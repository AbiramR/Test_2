# def _dict(lst2):
#     dict_inside={}

#     for key in lst2:
#         if key in dict_inside:
#             dict_inside[key]=dict_inside[key]+1
#         else:
#             dict_inside[key]=1  
#     return dict_inside

def max_prof(lst):
    max_profit=0
    min_=lst[0]
    for val in lst:
        if val-min_ >= max_profit:
            max_profit=val-min_
        if val < min_:
            min_=val
    return max_profit
        
# lst2=[1,2,4,5,3,1,2]
# print(_dict(lst2))

st_price=[9, 11, 8, 5, 7, 10]
print(max_prof(st_price))