'''
array = ['路人甲','路人乙','路人丙'];
print(array);
len   = array.insert(2,'中途加入'); #指定位置插入
#print(len);
#array.append( '新增的值' );
#len(array);
print(array);

array.pop(-1); #删除元素

print(array);

#加入数组
add = ['小明','小宝'];
array.append(add);
print(array[3]);


print('tuple元素组');
#tuple

tuple = (1,3,[2,3]);
tuple[2][0] = '改变1';
tuple[2][1] = '改变2';

print( tuple);
'''

#if else

# 生成随机数
# import random
# age =  random.randint(0,99)
# print(age)
# if age > 23 :
# 	print('大于23岁')
# elif age == 23 :
# 	print('等于23岁')
# else:
# 	print('小于23岁')

# x = input('birth:')
# x = int(x);
# if x > 10:
#     print('您输入的是数字大于10')
# elif x > 0 and x < 10:
#     print('您输入的是数字大于0小于10')
# else:
#     print('您输入的是数字小于0')

#+------
# 循环
#+------

# strinput = input('猜文字中大奖:')
# str = str( strinput )

# ## Prize 抽奖
# def Prize(str):
#     arr = {'7p':'恭喜您获得了iphone7 Push 128G','7':'恭喜您获得了iphone7 64G','6':'恭喜您获得了iphone6'}
#     prz    = ''
#     for item in arr:
#         if str in arr:
#             if arr[str] == arr[item]:
#                 prz = arr[item]
#                 break
#     return prz
# ## End Prize
# ##调用方法
# prz = Prize(str)
# if prz != '':
#     print(prz)
# else:
#     print('很遗憾您没有中奖!再接再厉.')

#jhjjjjjjjjjjjjdddsafdsafsdafdsf
