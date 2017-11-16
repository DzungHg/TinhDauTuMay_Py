from TinhToan import giaTriTheoKhuc

from MayInNhanh import *
# Tính thử về lợi nhuận
daySoLuong = [1,50,100,150,200]
dayLoiNhuan = [50,60,70,80,90]
#print(giaTriTheoKhuc(daySoLuong, dayLoiNhuan, 52))
#1). tính thử giá theo máy nhớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200]
dayLoiNhuanCB01 = [0,0,0,0,0]
#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
dayThangIn = [50000, 70000,100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]

mayinXerox1000i = MayInDigi(450, 1700000, 0.08, daySoLuongCB01, dayLoiNhuanCB01, 1800) #tốc độ hiệu suất 2500 a4/giờ
tyLeSales = 0;
giaIn01 = GiaInMayDigi(mayinXerox1000i, 0, tyLeSales)
#tính toán 01:
for i in range(1, len(dayThangIn)):
    giaIn01.SoTrangA4 = dayThangIn[i]
    print("Tháng in: {0}a4 /Sales: {1}đ/ Chi phí: {2}đ /Lãi: {3}đ /Giá bán TB/A4: {4}".format(dayThangIn[i], \
                                                         round(giaIn01.GiaSales()), giaIn01.chiPhi(), \
                                                     round(giaIn01.GiaSales() - giaIn01.chiPhi()), \
                                            round(giaIn01.GiaSales()/dayThangIn[i])))


