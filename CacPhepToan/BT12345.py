import numpy as np

def sinh_ngau_nhien_so_nguyen(a,b,n):
    v1 = np.random.randint(low = a, high= b, size=n )
    return v1
def nhan_mot_so_voi_1_vector(x,a):
    v2 = x * a
    print("Vecto sau khi nhân: ", v2)
    return v2
def cong_hai_vecto(x,y):
    s = x + y
    print("Vecto sau khi cộng: ",s)
    return s
def nhan_hai_vecto_vo_huong(x,y):
    p = np.dot(x,y)
    print("Vecto sau khi nhân vô hướng: ",p)
    return p
def nhan_hai_vecto_hadamard(x,y):
    h = np.multiply(x, y)
    print("Vecto sau khi nhân Hadamard: ",h)
    return h
def main():
    a = int(input("Nhập giá trị khoảng bắt đầu a: "))
    b = int(input("Nhập giá trị khoảng kết thúc b: "))
    n = int(input("Nhập số lượng phần tử n: "))
    x = sinh_ngau_nhien_so_nguyen(a,b,n)
    y = sinh_ngau_nhien_so_nguyen(a,b,n)
    print("Vecto a: ",x)
    print("Vecto b: ",y)
    nhan_mot_so_voi_1_vector(x,6)
    cong_hai_vecto(x,y)
    nhan_hai_vecto_vo_huong(x,y)
    nhan_hai_vecto_hadamard(x,y)
if __name__ == "__main__":
    main()
    