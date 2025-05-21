import json
def du_lieu_json():
    try:
        with open("mon_an.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def luu_du_lieu_json(mon_an):
    with open("mon_an.json", "w", encoding="utf-8") as file:
        json.dump(mon_an, file, ensure_ascii=False, indent=4)

# === QUẢN LÝ DANH SÁCH MÓN ĂN YÊU THÍCH ===
# 1. Thêm món ăn mới
# 2. Hiển thị danh sách món ăn
# 3. Tìm món ăn theo tên
# 4. Tìm món ăn theo nguyên liệu
# 5. Tìm món ăn theo cách nấu
# 6. Tìm món ăn theo quốc gia
# 7. Xóa món ăn
# 8. Thoát
# ========================

def them_mon_an(mon_an):
    ten_mon = input("Nhập tên món ăn: ")
    for mon in mon_an:
        if mon['ten'] == ten_mon:
            print("Món ăn đã tồn tại!")
            return
    nguyen_lieu = input("Nguyên liệu chính: ")
    cach_nau = input("Ghi chú về cách nấu: ")
    quoc_gia = input("Quốc gia của món ăn: ")
    mon_an.append({"ten": ten_mon, "nguyen_lieu": nguyen_lieu, "cach_nau": cach_nau, "quoc_gia": quoc_gia})
    print("Thêm món ăn thành công.")
    luu_du_lieu_json(mon_an)

def hien_thi_danh_sach(mon_an):
    if not mon_an:
        print("Danh sách trống!")
        return
    print("Tên món ăn        | Nguyên liệu chính | Cách nấu | Quốc gia")
    for thong_tin in mon_an:
        print(f"{thong_tin['ten']:<15} | {thong_tin['nguyen_lieu']:<18} | {thong_tin['cach_nau']} | {thong_tin['quoc_gia']}")

def tim_mon_an_theo_ten(mon_an):
    ten_mon = input("Nhập tên món ăn cần tìm: ").lower()
    found = False
    for thong_tin in mon_an:
        if ten_mon in thong_tin['ten'].lower():
            print(f"Tên món ăn: {thong_tin['ten']}")
            print(f"Nguyên liệu chính: {thong_tin['nguyen_lieu']}")
            print(f"Cách nấu: {thong_tin['cach_nau']}")
            print(f"Quốc gia: {thong_tin['quoc_gia']}")
            found = True
    if not found:
        print("Không tìm thấy món ăn.")

def tim_mon_an_theo_nguyen_lieu(mon_an):
    nguyen_lieu = input("Nhập nguyên liệu chính cần tìm: ").lower()
    found = False
    for thong_tin in mon_an:
        if nguyen_lieu in thong_tin['nguyen_lieu'].lower():
            print(f"Tên món ăn: {thong_tin['ten']}")
            print(f"Nguyên liệu chính: {thong_tin['nguyen_lieu']}")
            print(f"Cách nấu: {thong_tin['cach_nau']}")
            print(f"Quốc gia: {thong_tin['quoc_gia']}")
            found = True
    if not found:
        print("Không tìm thấy món ăn với nguyên liệu này.")

def tim_mon_an_theo_cach_nau(mon_an):
    cach_nau = input("Nhập từ khóa về cách nấu cần tìm: ").lower()
    found = False
    for thong_tin in mon_an:
        if cach_nau in thong_tin['cach_nau'].lower():
            print(f"Tên món ăn: {thong_tin['ten']}")
            print(f"Nguyên liệu chính: {thong_tin['nguyen_lieu']}")
            print(f"Cách nấu: {thong_tin['cach_nau']}")
            print(f"Quốc gia: {thong_tin['quoc_gia']}")
            found = True
    if not found:
        print("Không tìm thấy món ăn với cách nấu này.")

def tim_mon_an_theo_quoc_gia(mon_an):
    quoc_gia = input("Nhập quốc gia cần tìm: ").lower()
    found = False
    for thong_tin in mon_an:
        if quoc_gia in thong_tin['quoc_gia'].lower():
            print(f"Tên món ăn: {thong_tin['ten']}")
            print(f"Nguyên liệu chính: {thong_tin['nguyen_lieu']}")
            print(f"Cách nấu: {thong_tin['cach_nau']}")
            print(f"Quốc gia: {thong_tin['quoc_gia']}")
            found = True
    if not found:
        print("Không tìm thấy món ăn từ quốc gia này.")

def xoa_mon_an(mon_an):
    ten_mon = input("Nhập tên món ăn cần xóa: ")
    for i, thong_tin in enumerate(mon_an):
        if thong_tin['ten'] == ten_mon:
            mon_an.pop(i)
            print("Xóa món ăn thành công.")
            luu_du_lieu_json(mon_an)
            return
    print("Món ăn không tồn tại.")

if __name__ == "__main__":
    mon_an = du_lieu_json()
    while True:
        print("=== QUẢN LÝ DANH SÁCH MÓN ĂN YÊU THÍCH ===")
        print("1. Thêm món ăn mới")
        print("2. Hiển thị danh sách món ăn")
        print("3. Tìm món ăn theo tên")
        print("4. Tìm món ăn theo nguyên liệu")
        print("5. Tìm món ăn theo cách nấu")
        print("6. Tìm món ăn theo quốc gia")
        print("7. Xóa món ăn")
        print("8. Thoát")
        print("============================")

        lua_chon = int(input("Nhập lựa chọn của bạn (1–8): "))

        if lua_chon == 1:
            them_mon_an(mon_an)
        elif lua_chon == 2:
            hien_thi_danh_sach(mon_an)
        elif lua_chon == 3:
            tim_mon_an_theo_ten(mon_an)
        elif lua_chon == 4:
            tim_mon_an_theo_nguyen_lieu(mon_an)
        elif lua_chon == 5:
            tim_mon_an_theo_cach_nau(mon_an)
        elif lua_chon == 6:
            tim_mon_an_theo_quoc_gia(mon_an)
        elif lua_chon == 7:
            xoa_mon_an(mon_an)
        elif lua_chon == 8:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
