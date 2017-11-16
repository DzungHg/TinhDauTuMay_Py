from TinhToan import giaTriTheoKhuc

from MayInNhanh import *
# Tính thử về lợi nhuận 50% trên chi phí
daySoLuong = [1,50,100,150,200]
dayLoiNhuan = [50,60,70,80,90]

#print(giaTriTheoKhuc(daySoLuong, dayLoiNhuan, 52))
#1). tính thử giá theo máy nhớ số lượng bắt đầu 1
daySoLuongCB01 = [1,50,100,150,200]
dayLoiNhuanCB01 = [50,50,50,50,50]
#cung cấp dữ liệu để tính dựa trên thông tin hiện tại
dayTrang01 = [50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,999]
#Dãy trang theo tháng
mayinC6085 = MayInDigi(450, 760000, 0.08, daySoLuongCB01, dayLoiNhuanCB01, 2500) #tốc độ hiệu suất 2500 a4/giờ
tyLeSales = 0;
giaIn01 = GiaInMayDigi(mayinC6085, 0, tyLeSales)
#tính toán 01:
for i in range(1,len(dayTrang01)):
    giaIn01.SoTrangA4 = dayTrang01[i]
    print('Gói trang: {0} / {1} / Gia TB/A4: {2}'.format( dayTrang01[i], \
            round(giaIn01.GiaSales()), giaIn01.GiaSales() / dayTrang01[i]))

