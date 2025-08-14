# Credit Loan Approval System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PySide6](https://img.shields.io/badge/PySide6-GUI-green.svg)](https://pypi.org/project/PySide6/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange.svg)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-red.svg)](https://scikit-learn.org/)

## 📝 Mô tả dự án

Hệ thống phê duyệt khoản vay tín dụng sử dụng Machine Learning để dự đoán khả năng trả nợ của khách hàng. Dự án bao gồm phân tích dữ liệu khám phá (EDA), huấn luyện mô hình Random Forest, và giao diện người dùng để thực hiện dự đoán.

## ✨ Tính năng chính

- **Phân tích dữ liệu khám phá (EDA)**: Notebook Jupyter chi tiết với hơn 150 cells phân tích
- **Mô hình Machine Learning**: Random Forest đã được huấn luyện và tối ưu hóa
- **Giao diện người dùng**: GUI sử dụng PySide6 để dễ dàng sử dụng
- **Xử lý dữ liệu**: Tự động làm sạch và tiền xử lý dữ liệu đầu vào
- **Dự đoán real-time**: Khả năng dự đoán nhanh chóng cho từng hồ sơ

## 🏗️ Cấu trúc dự án

```text
Credit-Loan-Approval-System/
├── README.md                 # Tài liệu hướng dẫn
├── LICENSE                   # Giấy phép sử dụng
├── requirements.txt          # Dependencies Python
├── .gitignore               # Git ignore rules
├── SETUP.md                 # Hướng dẫn thiết lập nhanh
├── codeEDA.ipynb            # Notebook phân tích dữ liệu khám phá
├── RFT_model.pkl            # Mô hình Random Forest đã huấn luyện
├── dataset/                 # Dữ liệu đầu vào
│   ├── application_train.csv    # Dữ liệu huấn luyện
│   ├── application_test.csv     # Dữ liệu kiểm thử
│   └── dataset.zip             # Dữ liệu nén
└── GUI/                     # Giao diện người dùng
    ├── Main.py                 # Giao diện chính (PySide6)
    ├── Predict.py              # Module dự đoán và xử lý dữ liệu
    ├── Readdata.py             # Module đọc và hiển thị dữ liệu CSV
    ├── tt.py                   # GUI thử nghiệm (PyQt5)
    ├── Untitled-1.ipynb        # Notebook thử nghiệm
    └── application_train.csv   # Dữ liệu mẫu cho GUI
```

## 🚀 Cài đặt và sử dụng

### Yêu cầu hệ thống

- Python 3.8 hoặc cao hơn
- Jupyter Notebook (cho EDA)

### Cài đặt dependencies

```bash
# Clone repository
git clone https://github.com/datblue21/Credit-Loan-Approval-System.git
cd Credit-Loan-Approval-System

# Cài đặt thư viện cần thiết
pip install -r requirements.txt

# Hoặc cài đặt thủ công
pip install pandas numpy scikit-learn matplotlib seaborn
pip install PySide6
pip install jupyter notebook
pip install pickle-mixin
```

**⚠️ Lưu ý quan trọng:** Dự án cần các file bổ sung để hoạt động hoàn chỉnh:

- `column.csv` và `column_remove.csv` trong thư mục `GUI/` (cần tạo từ notebook EDA)
- Đảm bảo file `RFT_model.pkl` tồn tại và được tạo từ quá trình training

### Chạy ứng dụng

#### 1. Phân tích dữ liệu (EDA)

```bash
jupyter notebook codeEDA.ipynb
```

#### 2. Giao diện người dùng

```bash
cd GUI
python Main.py
```

#### 3. Đọc và xem dữ liệu CSV

```bash
cd GUI
python Readdata.py
```

## 📊 Mô tả dữ liệu

### Dataset chính

- **application_train.csv**: Dữ liệu huấn luyện với thông tin khách hàng và kết quả phê duyệt
- **application_test.csv**: Dữ liệu kiểm thử để đánh giá mô hình

### Các đặc trưng chính

- Thông tin cá nhân: Tuổi, giới tính, tình trạng hôn nhân
- Thông tin tài chính: Thu nhập, số tiền vay, thời hạn vay
- Lịch sử tín dụng: Các khoản vay trước đó, tình trạng thanh toán
- Thông tin việc làm: Loại công việc, thời gian làm việc

## 🤖 Mô hình Machine Learning

### Thuật toán sử dụng

- **Random Forest Classifier**: Mô hình ensemble với hiệu suất cao
- **Feature Engineering**: Tạo các đặc trưng mới từ dữ liệu gốc
- **Data Preprocessing**: Xử lý giá trị thiếu, mã hóa categorical variables

### Quy trình xử lý dữ liệu

1. **Làm sạch dữ liệu**: Xử lý outliers và giá trị bất thường
2. **Feature Engineering**: Tạo các tỷ lệ tài chính quan trọng
3. **Encoding**: Chuyển đổi categorical variables thành dạng số
4. **Normalization**: Chuẩn hóa dữ liệu đầu vào
5. **Feature Selection**: Loại bỏ các đặc trưng không quan trọng

## 🖥️ Modules chính

### 1. Main.py

- Giao diện chính sử dụng PySide6
- Hiển thị form nhập liệu và kết quả dự đoán
- Tích hợp với module Predict.py

### 2. Predict.py

- **Class ModelPredict**: Xử lý dự đoán chính
- **Phương thức cleandata()**: Tiền xử lý dữ liệu đầu vào
- **Phương thức predict()**: Thực hiện dự đoán và trả về kết quả
- Tự động load mô hình đã huấn luyện từ RFT_model.pkl

### 3. Readdata.py

- Giao diện đọc và hiển thị file CSV
- Sử dụng Tkinter để tạo bảng dữ liệu
- Hỗ trợ mở file CSV từ dialog

### 4. codeEDA.ipynb

- Phân tích dữ liệu khám phá chi tiết
- Visualizations và insights về dữ liệu
- Quy trình từ raw data đến trained model

## 📈 Kết quả và hiệu suất

- **Accuracy**: [Cần chạy notebook để cập nhật]
- **Precision**: [Cần chạy notebook để cập nhật]  
- **Recall**: [Cần chạy notebook để cập nhật]
- **F1-Score**: [Cần chạy notebook để cập nhật]

## 🔧 Phát triển và đóng góp

### ⚠️ Vấn đề cần khắc phục trước khi sử dụng

1. **Missing files**: Cần tạo `column.csv` và `column_remove.csv` từ notebook EDA
2. **GUI Framework**: Hiện có cả PySide6 (Main.py) và PyQt5 (tt.py) - nên thống nhất
3. **File cleanup**: Xem xét loại bỏ các file thử nghiệm không cần thiết

### Cải tiến có thể thực hiện

1. Thêm các thuật toán ML khác (XGBoost, LightGBM)
2. Tối ưu hóa hyperparameters
3. Xây dựng API RESTful
4. Cải thiện giao diện người dùng
5. Thêm tính năng export báo cáo
6. Thống nhất GUI framework
7. Tạo unit tests

### Đóng góp

1. Fork repository
2. Tạo feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m 'Add some AmazingFeature'`
4. Push to branch: `git push origin feature/AmazingFeature`
5. Open Pull Request


## 🙏 Acknowledgments

- Dataset từ Kaggle Home Credit
- Cảm ơn cộng đồng Python và Machine Learning
- Tham khảo từ các competition trên Kaggle

---


