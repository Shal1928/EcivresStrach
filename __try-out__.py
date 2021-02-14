# from store.dao import Session, RWI, WorkType
#
# s = Session()
#
# work_types = s.query(WorkType).all()
# print('### All Work Types:')
# for wt in work_types:
#     print(f'{wt.rowid} = ')
#
# wt_dic = {wt.rowid: wt.title for wt in work_types}
# print(wt_dic)
#
# rwi = RWI()
# rwi.title = 'rwi_test_1'
# rwi.comment = 'comment_1'
# rwi.tshirt = 1
# rwi.work_type = 3
# rwi.is_plan = False
# s.add(rwi)
# s.commit()
#
# rwis = s.query(RWI).all()
# print('### All RWIs:')
# for r in rwis:
#     print(f'{r.work_type_obj.title} = {r.tshirt_obj.title}')
from tkinter import Tk
from view.tkmodel import TkWorkType, TkTShirt, TkRWI

tk = Tk()
wt1 = TkWorkType()
tsh1 = TkTShirt()

rwi1 = TkRWI()

print(repr(rwi1))
print(rwi1)


