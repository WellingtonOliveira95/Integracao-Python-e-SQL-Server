from PyQt5 import  uic,QtWidgets
import pyodbc

cnxn = (
    "Driver={SQL Server};"
    "Server=DESKTOP-00A2R6S;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)

conexao = pyodbc.connect(cnxn)
print("Conexão bem sucedida!")

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    
    print("Nome cliente: ",linha1)
    print("E-Mail: ",linha2)
    print("Telefone:",linha3)
    print("Código do produto: ",linha4)
    print("Descrição do produto: ",linha5)
    print("CEP: ",linha6)

    cursor = conexao.cursor()
    comando = "INSERT INTO IntencaoCompra(nome, email, telefone, codigo, produto, cep) VALUES (?, ?, ?, ?, ?, ?)", (linha1, linha2, linha3, linha4, linha5, linha6)
    cursor.execute(*comando)
    cursor.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton_2.clicked.connect(funcao_principal)

formulario.show()
app.exec()