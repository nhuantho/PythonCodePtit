#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

struct sinhvien
{
	char masv[50], hoten[50];
	float tongdiem;
	sinhvien(char m[50], char h[50], float t){
		strcpy(masv, m);
		strcpy(hoten, h);
		this->tongdiem=t;
	}
};
void nhap(vector<sinhvien*>&danhsach){
	printf("So luong sinh vien can nhap: ");
	int n;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		fflush(stdin);
		printf("Sinh vien %d : \n", i+1);
		char masv[50], hoten[50];
		float tongdiem;
		printf("Nhap ma sinh vien: ");
		gets(masv);
		printf("Nhap ho ten: ");
		gets(hoten);
		printf("Nhap tong diem: ");
		scanf("%f", &tongdiem);
		sinhvien* x=new sinhvien(masv, hoten, tongdiem);
		danhsach.push_back(x);
	}
}
void inRa(vector<sinhvien*>&danhsach){
	for(int i=0; i<danhsach.size(); i++){
		printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
	}
}
void inRaSinhVienCoTongDiemCaoNhat(vector<sinhvien*>&danhsach){
	float MAX;
	for(int i=0; i<danhsach.size(); i++){
		if(danhsach[i]->tongdiem>MAX) MAX=danhsach[i]->tongdiem;
	}
	for(int i=0; i<danhsach.size(); i++){
		if(danhsach[i]->tongdiem==MAX){
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
		}
	}
}
void danhSachSinhVienDo(vector<sinhvien*>&danhsach){
	bool check=false;
	for(int i=0; i<danhsach.size(); i++){
		if(danhsach[i]->tongdiem>=17){
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
			check=true;
		}
	}
	if(check==false) printf("Khong co ai do\n");
}
void xepLoaiSinhVien(vector<sinhvien*>&danhsach){
	for(int i=0; i<danhsach.size(); i++){
		if(danhsach[i]->tongdiem<6){
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f: Kem\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
		}else if(danhsach[i]->tongdiem>=6&&danhsach[i]->tongdiem<7){
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f: Trung binh\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
		}else if(danhsach[i]->tongdiem>=7&&danhsach[i]->tongdiem<8){
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f: Kha\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
		}else{
			printf("Ma sinh vien: %s Ho ten: %s Tong diem: %.2f: Gioi\n", danhsach[i]->masv, danhsach[i]->hoten, danhsach[i]->tongdiem);
		}
	}
}
int main() {
	vector<sinhvien*>danhsach;
	int x;
	while (true)
	{
		printf("-------------------Menu------------------\n");
		printf("1. Nhap vao sinh vien\n");
		printf("2. Xuat ra danh sach sinh vien\n");
		printf("3. In ra sinh vien co tong diem cao nhat\n");
		printf("4. Danh sach sinh vien do\n");
		printf("5. Xep loai cho sinh vien\n");
		printf("0. An so 0 de thoai\n");
		printf("-----------------------------------------\n");
		printf("Moi ban chon\n");
		scanf("%d", &x);
		switch (x)
		{
		case 1:nhap(danhsach);
			break;
		case 2:inRa(danhsach);
			break;
		case 3:inRaSinhVienCoTongDiemCaoNhat(danhsach);
			break;
		case 4:danhSachSinhVienDo(danhsach);
			break;
		case 5:xepLoaiSinhVien(danhsach);
			break;
		case 0: return 0;
		default:printf("Nhap tu 0-5\n");
			break;
		}
	}
	return 0;
}