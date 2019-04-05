# 定义一个学生类，
'''
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return max(self.score)


luowen = Student('罗文', 18, [90, 99, 45])
print(luowen.get_name())
print(luowen.get_age())
print(luowen.get_score())


# 定义一个字典类

class DictClass(object):
    def __init__(self, dict1):
        self.dict = dict1

    def del_dict(self, key):
        # 判断key是否在字典里
        if key not in self.dict.keys():
            return 'key不在字典里'
        else:
            self.dict.pop(key)
            return '删除成功'

    def get_dict(self, key):
        if key not in self.dict.keys():
            return 'not found'
        else:
            return self.dict[key]

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()

d = DictClass({'a': 1, 'b': 2})
print(d.del_dict('a'))
print(d.get_key())
print(d.update_dict({'c': 78}))




# 定义一个列表操作类

class ListInfo(object):
    def __init__(self, list_val):
        self.list = list_val

    # 添加的key必须是数字或者字符串
    def add_key(self, key_name):
        if isinstance(key_name, (str, int)):
            self.list.append(key_name)
            print(self.list)
            return 'ok'
        else:
            return '我要字符串或数字'

    def get_key(self, index):
        # 判断索引是否超出了列表
        if 0 <= index <= len(self.list):
            return self.list[index]
        else:
            return '你输入的太多，想太多了'

    def update_list(self, new_list):
        self.list.extend(new_list)
        print(self.list)
        return 'ok,更新成功'

    # 需要判断列表中是否有元素
    def del_key(self):
        if len(self.list) >= 0:
            return self.list.pop()
        else:
            return '列表是空的'


l = ListInfo([1, 2, 3, 4, 5])
print(l.add_key([1,2,3,3]))
print(l.get_key(99))
print(l.update_list([99, 88]))
print(l.del_key())



# 定义一个集合的操作类

class SecInfo(object):
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self, keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett & unioninfo
        else:
            return '传入的不是set'

    def get_union(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett | unioninfo
        else:
            return '你传入的不是set'

    def del_different(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett - unioninfo
        else:
            return '你传入的不是set'


A = set([1, 2, 3, 4, 5, 6])
B = [5, 6, 9]
myset = SecInfo(A)
print(myset.add_setinfo(0))
print(myset.get_intersection(B))
print(myset.get_union(B))
print(myset.del_different(B))
'''

