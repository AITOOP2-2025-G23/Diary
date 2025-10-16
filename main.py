from diaries.DiarySample import DiarySample
from diaries.IwasakiDiary import IwasakiDiary
from diaries.MiriDiary import MiriDiary
from diaries.TsukadaDiary import TsukadaDiary
from diaries.rioDiary import rioDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           IwasakiDiary(),
           MiriDiary(),
           TsukadaDiary(),
           rioDiary(),
           ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()