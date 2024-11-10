class NoDuplicates:
    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for i in new_items:
            if i not in self.list:
                self.list.append(i)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.list)





