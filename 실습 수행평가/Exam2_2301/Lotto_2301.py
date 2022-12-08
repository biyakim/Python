#2310 김비야
#로또 번호 나오게하기
import random

def func_lotto():
    lot=random.sample(range(1,45),6)
    lot.sort()
    lot_str = str(lot)[1:-1]
    print("당첨 번호 : ",lot_str)

func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()