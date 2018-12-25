# -*- coding: utf-8 -*-
import random

from data.group import random_string
def test_add_group(app):
    #запуск приложения
    application=app
    old_list=application.get_group_list()
    newgroup=random_string('Group_',10)
    application.add_new_group(newgroup)
    new_list=application.get_group_list()
    old_list.append(newgroup)
    assert sorted(old_list)  == sorted(new_list)



def test_delete_group(app):
    #запуск приложения
    application=app
    old_list=application.get_group_list()
    rand_num=random.randrange(0,len(old_list))
    application.delete_group(rand_num)
    new_list=application.get_group_list()
    old_list.pop(rand_num)
    assert sorted(old_list)  == sorted(new_list)


#def TestControlTypeX():
#    pass
