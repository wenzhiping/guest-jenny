from django.core.paginator import Paginator # 导入 Paginator 类
from sign.models  import Guest # Guest 下的所有表
guest_list = Guest.objects.all() # 查询 uest 表的所有数据
p = Paginator(guest_list,2) # 创建每页 2 条数据的分页器
print().p.count # 查看共多少条数据
print().page_range #查看共分多少页（每页 2 条数据）循环结果为 1，2，3（共 3 页）
