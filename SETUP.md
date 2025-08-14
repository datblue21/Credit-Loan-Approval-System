# Hướng dẫn thiết lập nhanh

## Bước 1: Clone repository
```bash
git clone https://github.com/datblue21/Credit-Loan-Approval-System.git
cd Credit-Loan-Approval-System
```

## Bước 2: Tạo virtual environment (khuyến nghị)
```bash
# Sử dụng conda
conda create -n credit-loan python=3.8
conda activate credit-loan

# Hoặc sử dụng venv
python -m venv credit-loan-env
source credit-loan-env/bin/activate  # macOS/Linux
# credit-loan-env\Scripts\activate   # Windows
```

## Bước 3: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

## Bước 4: Chạy ứng dụng
```bash
# Chạy notebook EDA
jupyter notebook codeEDA.ipynb

# Chạy GUI chính
cd GUI
python Main.py

# Hoặc chạy CSV viewer
python Readdata.py
```

## Lưu ý quan trọng:
- Đảm bảo file `RFT_model.pkl` tồn tại trong thư mục gốc
- Dataset cần có trong thư mục `dataset/`
- Để có kết quả dự đoán chính xác, cần có file `column.csv` và `column_remove.csv` trong thư mục `GUI/`
