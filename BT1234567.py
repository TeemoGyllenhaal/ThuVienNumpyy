#1
import numpy as np
#2
def tao_vecto(n,a,b):
    v1 = np.arange(n, dtype=int)
    v2 = np.arange(start=a, stop =b, dtype=int)
    print(v1)
    print(v2)
tao_vecto(15,-5,5)
#3
#Tạo 1 vector các giá trị số thực tăng dần và cách đều nhau
#Giá trị mỗi phần tử ngẫu nhiên trong -5, 6, 10 phần tử
def tao_vecto_tang_dan_cach_deu_nhau(a,b,n):
    v3 = np.linspace(start=a, stop=b, num=n, dtype=float)
    print(v3)
tao_vecto_tang_dan_cach_deu_nhau(-5,6,10)
#4
#Sinh ngẫu nhiên 1 vector các số nguyên trong khoảng [a, b)
np.random.seed(123)
#Sinh ngẫu nhiên 1 vector số nguyên 10 phần tử
#Giá trị mỗi phần tử ngẫu nhiên trong -3, 3
def sinh_ngau_nhien_so_nguyen(a,b,n):
    v4 = np.random.randint(low = a, high= b, size=n )
    print(v4)
    return v4
sinh_ngau_nhien_so_nguyen(-3,3,10)
#5
#Sinh ngẫu nhiên 1 vector số thực trong khoảng [a, b)
#Giá trị mỗi phần tử ngẫu nhiên trong -2, 3
def sinh_ngau_nhien_so_thuc(a,b,n):
    v5 = (b -a)*np.random.random_sample(n) + a
    print(v5)
sinh_ngau_nhien_so_thuc(-2,3,10)
#6
#a = -5; b = 5; c = -10; d= 10
def nhap_gia_tri():
    a = int(input("Nhập giá trị a: "))
    b = int(input("Nhập giá trị b: "))
    c = int(input("Nhập giá trị c: "))
    d = int(input("Nhập giá trị d: "))
    n = int(input("Nhập giá trị phần tử n: "))
    return a,b,c,d,n
def main():
    a,b,c,d,n=nhap_gia_tri()
    tao_vecto(n,a,b)
    tao_vecto_tang_dan_cach_deu_nhau(c,d,n)
    v4 = sinh_ngau_nhien_so_nguyen(a,b,n)
    sinh_ngau_nhien_so_thuc(c,d,n)
    #7
    print(v4.shape)
    print(v4.ndim)
if __name__ == "__main__":
    main()