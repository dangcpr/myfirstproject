import random
import re
import os
vongquay = [100,200,300,400,500,600,700,800,900,1000,2000,"May mắn","Mất điểm","Nhân đôi","Chia đôi"]
phanthuong = ["1 chiếc bàn chải điện tử trị giá 900k","1 chai xịt thơm miệng trị giá 240k","1 bàn chải đánh răng trị giá 20k"]
ochu=input("Nhap o chu: ")
ochu=ochu.upper()
ochu=ochu.replace(" ","")
Chinhxac=ochu
ochu = re.sub(r'[ÀÁẠẢÃ]', 'a', ochu)
ochu = re.sub(r'[ẦẤẬẨẪ]', 'â', ochu)
ochu = re.sub(r'[ẰẮẶẲẴ]', 'ă', ochu)
ochu = re.sub(r'[ÈÉẸẺẼ]', 'E', ochu)
ochu = re.sub(r'[ỀẾỆỂỄ]', 'Ê', ochu)
ochu = re.sub(r'[ÒÓỌỎÕ]', 'O', ochu)
ochu = re.sub(r'[ỒỐỘỔỖ]', 'Ô', ochu)
ochu = re.sub(r'[ÌÍỊỈĨ]', 'I', ochu)
ochu = re.sub(r'[ÙÚỤỦŨ]', 'U', ochu)
ocho = re.sub(r'[ỪỨỰỬỮ]', 'Ư', ochu)
ochu = re.sub(r'[ỲÝỴỶỸ]', 'Y', ochu)
print(ochu.count('A'))

