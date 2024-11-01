def search_medium_number():
    num1=[1,2,5,6,9,7]
    num2=[2,5,4,4,8,7,5,6]
    new_num=num1+num2
    new_num.sort()
    lenth=len(new_num)
    print(new_num[lenth-1])
search_medium_number()