#导入 sign 应用下的 models.py 中的 Event 表和 Guest 表
from sign.models import Event,Guest

#因为要设置时间   在.../settings.py 文件中设置：USE_TZ = False
from datetime import datetime

#table.objects.all()
#获得 table（Event、Gues 表）中的所有对象
Event.objects.all()
Guest.objects.all()

#-----插入数据-------

# #创建数据
# e1 = Event(id=2,name='红米 Pro 发布会',limit=2000,status=True,address='北京水立方',
#            start_time=datetime(2016,8,10,14,0,0))
# #保存到数据库
# e1.save()

#创建数据并保存到数据库
Event.objects.create(id=5,name='红米 MAX 发布会',limit=2000,status=True,
address='北京会展中心',start_time=datetime(2016,9,22,14,0,0))

Guest.objects.create(realname='andy',phone=13611001101,
                     email='andy@mail.com',sign=False,event_id=5)

#-----更新数据-------
# g3=Guest.objects.get(phone='13611001101')
# g3.realname='andy2'
# g3.save()
Guest.objects.select_for_update().filter(phone='13611001101').update(realname='andy2')

#-----查询数据-------
#table.objects.get()方法用于从数据库表中取得一条匹配的结果，返回一个对象，如果记录不存在的话，那
#么它会报 DoesNotExist 类型错误。
e1 = Event.objects.get(name='红米 MAX 发布会')
print(e1.address)
e2 = Event.objects.filter(name__contains='发布会')
print(e2)
g1 = Guest.objects.get(phone='13611001101')
print(g1.realname,g1.event,g1.event.name)

#-----删除数据-------
#通过 delete()方法删除。
e1 = Event.objects.get(name='红米 MAX 发布会')
e1.delete()

g2 = Guest.objects.get(phone='13611001101')
g2.delete()

