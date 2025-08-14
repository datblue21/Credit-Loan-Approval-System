import sys
import pandas as pd
from Predict import Modelpredict
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QTableWidget,
    QHBoxLayout,
    QTableWidgetItem,
     
)






class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.model= Modelpredict()
       
        self.setWindowTitle("My CSV App")
        self.kq=pd.array([])
        # Create layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Label to display file status
        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

   

        # Create the table widget (initially hidden)
        self.table = QTableWidget()
        self.table.setColumnCount(0)  # Adjust column count after reading data
        self.table.setRowCount(0)  # Adjust row count after reading data
        self.table.horizontalHeader().setVisible(False)  # Hide headers initially
        self.table.verticalHeader().setVisible(False)  # Hide headers initially
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)  # Make cells read-only
        self.table.hide()
        self.layout.addWidget(self.table)

        self.open_button = QPushButton("Open CSV File")
        self.open_button.clicked.connect(self.open_csv_file)
        self.layout.addWidget(self.open_button)

        self.open_button = QPushButton("Predict")
        self.open_button.clicked.connect(self.runPredict)
        self.layout.addWidget(self.open_button)
    def runPredict(self):
        self.kq=self.model.predict(self.data)
        print(self.kq.head(6))
        self.update_table_color()


    def open_csv_file(self):
        # Open file dialog to select a CSV file
        filename, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "*.csv")
        print(filename)
        if not filename:
            return  # User canceled or no file selected

        self.status_label.setText("Reading file...")

        # Read the CSV file content
        try:
           with open(filename, 'r') as f:
                self.data =pd.read_csv(filename,encoding='cp1252',header=0)
                self.data=self.data.head(100)
        except FileNotFoundError:
            self.status_label.setText("Error: File not found.")
            return

        # Update table based on data
        print(self.data.shape)
        self.update_table()

        self.table.show()
        self.status_label.setText("File loaded successfully.")

    def getcolor(self,pr):
        if pr==0:
            return  QColor(255, 0, 0,127)
        else:
            return QColor(0, 255, 0,127)

    def save_csv_result(self):
        dt=self.data
        kq=self.kq
    def update_table(self):
        # Set column count based on the first row (assuming consistent headers)
        self.table.setColumnCount(self.data.shape[1])
        columns=list(self.data.columns)
        
        # Set row count based on the number of data rows
        self.table.setRowCount(self.data.shape[0])  # Exclude header row
    
        # Set headers (optional, uncomment if you want headers)
      
        for i in range(len(columns)):
             header_item = QTableWidgetItem(str(columns[i]))
             self.table.setHorizontalHeaderItem(i,header_item)

        # Fill table cells
        
        X,Y=self.data.shape
        for row in range(X):
            for col in range(Y):
                item =QTableWidgetItem(str(self.data.iloc[row][col]))                
                self.table.setItem(row, col,item )
                
        #self.table.setHorizontalHeaderLabels(self.data.columns)

    def update_table_color(self):
        X,Y=self.data.shape
        for row in range(X):
            for col in range(Y):              
                item=self.table.item(row,col)
                item=QTableWidgetItem(item)
                item.setBackground(self.getcolor(self.kq.iloc[row][1]))
                self.table.setItem(row, col,item )
                
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
