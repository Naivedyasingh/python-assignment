# 1.write a python program to find similar item to dictionary list

# list1=[4,2,2,4,5,6,7,65,4,2,21,3,4,9,0,0]
# result={}
# for i in list1:
#     if i in result:
#         result[i].append(i)
#     else:
#         result[i]=[i]    
# print(result)   


# count_dict={key:len(value) for key,value in result.items()}
# print(count_dict)


# 2.write a pyhton program to convert list of dict to list of list 

# input1=[{'gfg':123,'best':10},{'gfg':51,'best':7}]

# keys=list(input1[0].keys())
# result=[]
# result.append(keys)
# for i in input1:
#     row=[]
#     for j in i.values():
#         row.append(j)
#     result.append(row)
# print(result)


# 3.write program to print all distinct values in a dictionary

# original_list=[{'V':'S001'},{'V':'S002'},{'VI':'S001'},{'VI':'S005'},{'VII':'S005'},{'V':'S009'},{'VIII':'S007'}]
# unique_values=set()
# for i in original_list:
#     for j in i.values():
#         unique_values.add(j)
# print(unique_values)        


# 4.write a program to find the highest 3 values corresponding keys in dictionaries.
# values={'a':100,'b':50,'c':200,'d':500,'e':10}
# sort_values=sorted(values.items(),key=lambda x:x[1],reverse=True)

# top_3=sort_values[:3]
# top_keys=[]
# for i  in top_3:
#     top_keys.append(i[1])
# print(top_keys)    



# 5.write a program to combine the values in list
# list1=[{'item':'item1','amount':2000},{'item':'item1','amount':1000},{'item':'item2','amount':2000}]
# combine={}
# for i in list1:
#     name=i['item']
#     value=i['amount']
#     if name in combine:
#         combine[name]+=value
#     else:
#         combine[name]=value
# print(combine)           


# 6.write a python program to sort the alphabetically in dictionary

# num={'n1':[1,2,3],'n2':[100,22,53],'n3':[10,9,21],}
# for n in num:
#     num[n]=sorted(num[n])
#     print(num[n])
# print(num) 
# 
# 


# 7.write a pyhton program to count the number values in dictionay 

#values1={'alex':['sing','work','fight'],'max':['work','fight'],'alice':['sing','work','fight','mind']}

# count_keys={k:len(val) for k,val in values1.items()}
# num=0
# for i in count_keys:
#     num+=count_keys[i]
# print(num)    
#OR
# count=0
# for i in values1.values():
#     count+=len(i)
# print(count)    



# 8. write program for remove the  duplicate values from dictionary
data = {
    'a': [1, 2, 3],
    'b': [2, 3, 4],
    'c': [4, 5, 6],
    'd': [1, 7]
}

seen = set()
result = {}

for key in data:
    unique_values = []
    for val in data[key]:
        if val not in seen:
            unique_values.append(val)
            seen.add(val)
    result[key] = unique_values
print(result)



# 9.write a python program counting the frequency in the list using dictionary
# list1=[4,2,2,4,5,6,7,65,4,2,21,3,4,9,0,0]
# count={}
# for i in list1:
#     if i in count:
#         count[i].append(i)
#     else:
#         count[i]=[i]   

# count_vales={k:len(v) for k,v in count.items()}

# print(count_vales)