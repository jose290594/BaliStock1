from datetime import  datetime
import time
import sys
import os
print(os.getcwd())
import mysql.connector
from mysql.connector import errors
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QTableView, QPushButton, QLineEdit, QDateEdit, QListWidget, QTableWidget, QListWidgetItem, QTableWidgetItem, QLabel, QSpinBox, QComboBox, QAbstractItemView
from PySide2.QtCore import QFile, QSize, QAbstractListModel, QAbstractItemModel, QModelIndex
from PySide2.QtGui import QWindow
import sqlite3
import csv
usus1=input('Usuario: ')
passpass1=input('Contraseña: ')
os.system('cls')
ssl={'cert':'keys/client-cert.pem', 'key':'keys/client-key.pem', 'ca':'keys/server-ca.pem'}
try:
    connection = mysql.connector.connect(host='x.x.x.x',
                                         database='x',
                                         user=usus1,
                                         password=passpass1,
                                         ssl_ca=ssl.get('ca'),
                                         ssl_cert=ssl.get('cert'),
                                         ssl_key=ssl.get('key'))

except Error as e:
    print("Error while connecting to MySQL", e)


print('''
Bienvenido a BaliStock, por favor espere mientras carga y se muestra la interfaz principal...

''')

print('1...')
#### Declaracion de aplicacion
app = QApplication(sys.argv)
#### Conexion a base de datos local
# try:
    
#     connection = mysql.connector.connect(host='localhost',
#                                             database='balibetov',
#                                             user='*****',
#                                             password='*****')
# except errors:
#     print('error')

#### Interfaz Principal
mainUIfile = QFile("main-ui.ui")
mainUIfile.open(QFile.ReadOnly)
loader = QUiLoader()
mainUIwindow = loader.load(mainUIfile)
add_in1 = mainUIwindow.findChild(QPushButton, 'addIn1')
add_out1 = mainUIwindow.findChild(QPushButton, 'addOut1')
view_stock1= mainUIwindow.findChild(QPushButton, 'viewStock1')
view_log1 = mainUIwindow.findChild(QPushButton, 'viewLog1')
sReportB1= mainUIwindow.findChild(QPushButton, 'sReport1')
rReportB1= mainUIwindow.findChild(QPushButton, 'rReport1')
print('2...')

#####     Interfaz Añadir entrada
addinfile1 = QFile("addinw1.ui")
addinfile1.open(QFile.ReadOnly)
loaderIn = QUiLoader()
addinwindow1 = loaderIn.load(addinfile1)
combprov1 = addinwindow1.findChild(QComboBox, 'proveedor1')
combprod1 = addinwindow1.findChild(QComboBox, 'SKUprod1')
cantsp1 = addinwindow1.findChild(QSpinBox, 'cantidadin1')
indatef1 = addinwindow1.findChild(QDateEdit, 'fechain1')
butGo1 = addinwindow1.findChild(QPushButton, 'goAct1')
statusLabel1 = addinwindow1.findChild(QLabel, 'status1')

#####     Interfaz Añadir salida
addoutfile1 = QFile("addout1.ui")
addoutfile1.open(QFile.ReadOnly)
loaderOut = QUiLoader()
addoutwindow1 = loaderOut.load(addoutfile1)
butGo2 = addoutwindow1.findChild(QPushButton, 'goAct2')
cantsp2 = addoutwindow1.findChild(QSpinBox, 'cantidadout1')
outdatef1 = addoutwindow1.findChild(QDateEdit, 'fechaout1')
combdestout1 = addoutwindow1.findChild(QComboBox, 'destino1')
combprodout1 = addoutwindow1.findChild(QComboBox, 'SKUprod2')
statusLabel2 = addoutwindow1.findChild(QLabel, 'status2')

#####     Interfaz Stock
stockviewfile1 = QFile("stockview1.ui")
stockviewfile1.open(QFile.ReadOnly)
loaderStock = QUiLoader()
stockviewwindow1 = loaderStock.load(stockviewfile1)
mainstocktab1 = stockviewwindow1.findChild(QTableWidget, 'tablaStock1')
mainstocktab1.horizontalHeader()
mainstocktab1.horizontalHeader()#.setResizeMode(0, QtGui.QHeaderView.Stretch)
mainstocktab1.horizontalHeader()#.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
#print(type(mainstocktab1))

#####     Interfaz Registro
logfile1 = QFile("logview1.ui")
logfile1.open(QFile.ReadOnly)
loaderLog = QUiLoader()
logwindow1 = loaderLog.load(logfile1)
mainlogtab1 = logwindow1.findChild(QTableWidget, 'tablaLog1')
#print('low')
#print(type(mainlogtab1))

### Funcion para Entrada
def addinf1():
    print('hel')
    conprov1 = connection
    cursorObjp2 = conprov1.cursor(buffered=True)
    cursorObjp2.execute("SELECT proveedores FROM proveedores ;")
    #conprov1.commit()
    prov_data1 = cursorObjp2.fetchall()
    for prov1 in range(0, len(prov_data1)):
        combprov1.addItem(prov_data1[prov1][0])
    conprodsku1 = connection
    cursorObjp3 = conprodsku1.cursor()
    cursorObjp3.execute("SELECT Producto FROM stock1;")
    #conprodsku1.commit()
    prodsku_data1 = cursorObjp3.fetchall()

    for prodsku1 in range(0, len(prodsku_data1)):
        combprod1.addItem(prodsku_data1[prodsku1][0])
 
    addinwindow1.show()
###### Accion de Entrada
def inFunct1():
    statusLabel1.setText('cargando...')
    provGo1=str(combprov1.currentText())
    prodGo1=str(combprod1.currentText())
    cantGo1=int(cantsp1.text())
    dateGo1=str(indatef1.text())
    statusLabel1.setText('data creada...')
    #print(indatef1.text())

    statusLabel1.setText('obteniendo valores...')
    conGetent1 = connection
    cursorGetent1 = conGetent1.cursor(buffered=True)
    cursorGetent1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(prodGo1)+"';")
    #conGetent1.commit()
    actProdcant1 = cursorGetent1.fetchall()
    cantGonew1=int(int(cantsp1.text())+int(actProdcant1[0][0]))

    try:
        statusLabel1.setText('conectando a DB...')
        conGoent1 = connection
        cursorGoent1 = conGoent1.cursor(buffered=True)
        sqlGo2stock = """UPDATE stock1
                SET cantidad = """+"'"+str(cantGonew1)+"'"+" WHERE producto = "+"'"+str(prodGo1)+"';"
        cursorGoent1.execute(str(sqlGo2stock))
        conGoent1.commit()
        statusLabel1.setText('cargado en DB')
        statusLabel1.setText('Hecho!')
    except EnvironmentError:
        print('error')
        statusLabel1.setText('Error!')
    



    try:
        statusLabel1.setText('conectando a DB...')
        conGoent2 = connection
        cursorGoent2 = conGoent2.cursor(buffered=True)
        sqlGo2stock = """INSERT INTO registro(fecha,tipo,producto,cantidad,destino,proveedor)
                VALUES("""+"'"+str(dateGo1)+"',"+"'"+str('entrada')+"',"+"'"+str(prodGo1)+"',"+"'"+str(cantGo1)+"',"+"'"+str('na')+"',"+"'"+str(provGo1)+"'"+");"
        cursorGoent2.execute(str(sqlGo2stock))
        conGoent2.commit()
        print('arre')
        statusLabel1.setText('cargado en DB')
        statusLabel1.setText('Hecho!')
    except EnvironmentError:
        print('error')
        statusLabel1.setText('Error!')
    
    print('listo')

### Funcion para Salida
def addoutf1():
    conprov4 = connection
    cursorObjp4 = conprov4.cursor(buffered=True)
    cursorObjp4.execute("SELECT proveedores FROM proveedores;")
    #conprov4.commit()
    prov_data2 = ['USA', 'EUR']
    for prov2 in range(0, len(prov_data2)):
        combdestout1.addItem(prov_data2[prov2])
    conprodsku2 = connection
    cursorObjp5 = conprodsku2.cursor(buffered=True)
    cursorObjp5.execute("SELECT Producto FROM stock1;")
    #conprodsku2.commit()
    prodsku_data2 = cursorObjp5.fetchall()
    for prodsku2 in range(0, len(prodsku_data2)):
        combprodout1.addItem(prodsku_data2[prodsku2][0])
    addoutwindow1.show()
###### Accion de Salidad
def outFunct1():
    statusLabel2.setText('cargando...')
    destGo1=str(combdestout1.currentText())
    prodGo2=str(combprodout1.currentText())
    cantGo2=int(cantsp2.text())
    dateGo2=str(outdatef1.text())
    statusLabel2.setText('data creada...')
    #print(indatef1.text())
    if prodGo2 != ('bombilla1' or 'bombilla2' or 'caja1' or 'caja2' or 'caja3' or 'folleto1' or 'cuchara1' or 'limpia1' or 'bolsatela1'):
        statusLabel2.setText('obteniendo valores...')
        conGetsal1 = connection
        cursorGetsal1 = conGetsal1.cursor()
        cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(prodGo2)+"';")
        #conGetsal1.commit()
        actProdcant2 = cursorGetsal1.fetchall()
        cantGo1=int(int(actProdcant2[0][0])-int(cantsp2.text()))
        cursorGetsal1.execute("SELECT caja, bombilla, cuchara, limpiador, folleto, bolsatela  FROM stock1 WHERE producto = "+"'"+str(prodGo2)+"';")
        #conGetsal1.commit()
        loteObj1 = cursorGetsal1.fetchall()
        print(loteObj1)
        bombSKU1=int(loteObj1[0][1])
        cajaSKU1=int(loteObj1[0][0])
        cucharaMark1=int(loteObj1[0][2])
        limpiMark1=int(loteObj1[0][3])
        folletoMark1=int(loteObj1[0][4])
        bolteMark1=int(loteObj1[0][5])
        bombSKUvalr2=None
        ######### obteniendo SKU de bombilla
        print(bombSKU1)
        if bombSKU1 == 1:

            bombSKUvalr2=str('bombilla1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(bombSKUvalr2)+"';")
            #conGetsal1.commit()
            totbomval1 = int(cursorGetsal1.fetchall()[0][0])

        if bombSKU1 == 2:
            bombSKUvalr2=str('bombilla2')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(bombSKUvalr2)+"';")
            #conGetsal1.commit()
            totbomval1 = int(cursorGetsal1.fetchall()[0][0])

        if bombSKU1 == 0: 
            totbomval1=0
            bombSKUvalr2=0

        ######### obteniendo SKU de cajas

        if cajaSKU1 == 1:
            cajaSKUvalr2=str('caja1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(cajaSKUvalr2)+"';")
            #conGetsal1.commit()
            totcajval1 = int(cursorGetsal1.fetchall()[0][0])

        if cajaSKU1 == 2:
            cajaSKUvalr2=str('caja2')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(cajaSKUvalr2)+"';")
            #conGetsal1.commit()
            totcajval1= int(cursorGetsal1.fetchall()[0][0])

        if cajaSKU1 == 3:
            cajaSKUvalr2=str('caja3')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(cajaSKUvalr2)+"';")
            #conGetsal1.commit()
            totcajval1 = int(cursorGetsal1.fetchall()[0][0])

        if cajaSKU1 == 0: 
            cajaSKUvalr2=0

        ######### obteniendo SKU de cuchara
        if cucharaMark1 != 0:
            cucharaSKUvalr2=str('cuchara1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(cucharaSKUvalr2)+"';")
            #conGetsal1.commit()
            totcucval1 = int(cursorGetsal1.fetchall()[0][0])
        else:
            cucharaSKUvalr2=0
        ######### obteniendo SKU de limpiador
        if limpiMark1 != 0:
            limpiSKUvalr2=str('limpia1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(limpiSKUvalr2)+"';")
            #conGetsal1.commit()
            totlimval1=int(cursorGetsal1.fetchall()[0][0])

        else:
            limpiSKUvalr2=0
        ######### obteniendo SKU de folleto
        if folletoMark1 != 0:
            folletoSKUvalr2=str('folleto1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(folletoSKUvalr2)+"';")
            #conGetsal1.commit()
            totlfolval1= int(cursorGetsal1.fetchall()[0][0])

        else:
            folletoSKUvalr2=0
                                
        ######### obteniendo SKU de bolsa de tela
        if bolteMark1 != 0:
            bolsatelaSKUvalr2=str('bolsatela1')
            cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(bolsatelaSKUvalr2)+"';")
            #conGetsal1.commit()
            totbotval1 = int(cursorGetsal1.fetchall()[0][0])

        else:
            bolsatelaSKUvalr2=0              
        print(totbomval1)
        try:
            statusLabel2.setText('conectando a DB...')
            conGosal1 = connection
            cursorGosal1 = conGosal1.cursor()
            sqlGo2stock = """UPDATE stock1
                    SET cantidad = """+"'"+str(int(actProdcant2[0][0])-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(prodGo2)+"';"
            
            if bombSKUvalr2 != 0:
                print(str(bombSKUvalr2)+'revisa aqui')
                susBom1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totbomval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(bombSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susBom1)

            if cajaSKUvalr2 != 0:
                print(str(cajaSKUvalr2)+'revisa aqui')
                susCaj1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totcajval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(cajaSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susCaj1)
            if cucharaSKUvalr2 != 0:
                susCuc1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totcucval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(cucharaSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susCuc1)

            if limpiSKUvalr2 != 0:
                susLim1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totlimval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(limpiSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susLim1)

            if folletoSKUvalr2 != 0:
                susFol1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totlfolval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(folletoSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susFol1)

            if bolsatelaSKUvalr2 != 0:
                susBot1 = str(""" UPDATE stock1
                    SET cantidad = """+"'"+str(int(totbotval1)-int(cantsp2.text()))+"'"+" WHERE producto = "+"'"+str(bolsatelaSKUvalr2)+"';")
                sqlGo2stock=str(sqlGo2stock)+str(susBot1)

            cursorGosal1.execute(str(sqlGo2stock))
            conGosal1.commit()
            statusLabel2.setText('cargado en DB')
            statusLabel2.setText('Hecho!')
        except EnvironmentError:
            print('error')
            statusLabel2.setText('Error!')
        



        try:
            statusLabel1.setText('conectando a DB...')
            conGoent2 = connection
            cursorGoent2 = conGoent2.cursor()
            sqlGo2stock = """INSERT INTO registro(fecha,tipo,producto,cantidad,destino,proveedor)
                    VALUES("""+"'"+str(dateGo2)+"',"+"'"+str('salida')+"',"+"'"+str(prodGo2)+"',"+"'"+str(cantGo2)+"',"+"'"+str(destGo1)+"',"+"'"+str('na')+"'"+");"
            cursorGoent2.execute(str(sqlGo2stock))
            conGoent2.commit()
            print('arre')
            statusLabel2.setText('cargado en DB')
            statusLabel2.setText('Hecho!')
        except EnvironmentError:
            print('error')
            statusLabel2.setText('Error!')
    ###### Cuando es Bombilla, Caja, Cuchara, Limpiador o Folleto
    else:
        statusLabel2.setText('obteniendo valores...')
        conGetsal1 = connection
        cursorGetsal1 = conGetsal1.cursor()
        cursorGetsal1.execute("SELECT cantidad FROM stock1 WHERE producto = "+"'"+str(prodGo2)+"';")
        #conGetsal1.commit()
        actProdcant1 = cursorGetsal1.fetchall()
        cantGo1=int(int(actProdcant1[0][0])-int(cantsp1.text()))
        try:
            statusLabel2.setText('conectando a DB...')
            conGetsal1 = connection
            cursorGetsal1 = conGetsal1.cursor()
            sqlGo2stock = """UPDATE stock1
                    SET cantidad = """+"'"+str(cantGo2)+"'"+" WHERE producto = "+"'"+str(prodGo2)+"';"
            cursorGetsal1.execute(str(sqlGo2stock))
            conGetsal1.commit()
            statusLabel2.setText('cargado en DB')
            statusLabel2.setText('Hecho!')
        except EnvironmentError:
            print('error')
            statusLabel2.setText('Error!')
        



        try:
            statusLabel1.setText('conectando a DB...')
            conGoent2 = connection
            cursorGoent2 = conGoent2.cursor()
            sqlGo2stock = """INSERT INTO registro(fecha,tipo,producto,cantidad,destino,proveedor)
                    VALUES("""+"'"+str(dateGo2)+"',"+"'"+str('salida')+"',"+"'"+str(prodGo2)+"',"+"'"+str(cantGo2)+"',"+"'"+str(destGo1)+"',"+"'"+str('na')+"'"+");"
            cursorGoent2.execute(str(sqlGo2stock))
            conGoent2.commit()
            print('arre')
            statusLabel1.setText('cargado en DB')
            statusLabel1.setText('Hecho!')
        except EnvironmentError:
            print('error')
            statusLabel1.setText('Error!')

    print('listo')
    print('hel')

### Funcion para Stock
def viewstockf1(self):
    print(sys.executable)
    print(os.getcwd())
    mainstocktab1.setRowCount(0)
    print('hel')
    conStock = connection
    cursorObjs1 = conStock.cursor()
    cursorObjs1.execute("SELECT producto, cantidad FROM stock1;")

    #conStock.commit()
    
    stock_data1 = cursorObjs1.fetchall()
 
    header_labels = ['Producto', 'Cantidad']  
    mainstocktab1.setRowCount(len(stock_data1))
    print(stock_data1[0][0])

    for row in range(0, len(stock_data1)):

        obj11=QTableWidgetItem()

        obj22=QTableWidgetItem()

        mainstocktab1.setItem(row,0,obj11) # Y is the column that you want to insert data
        mainstocktab1.item(row,0).setText(str(stock_data1[row][0]))
        mainstocktab1.setItem(row,1,obj22) # Y is the column that you want to insert data
        mainstocktab1.item(row,1).setText(str(stock_data1[row][1]))


    stockviewwindow1.show()

### Funcion para Registro
def viewlogf1():

    mainlogtab1.setRowCount(0)
    print('hel')
    conLog1 = connection
    cursorObjl1 = conLog1.cursor()
    cursorObjl1.execute("SELECT fecha, tipo, producto, cantidad, destino, proveedor FROM registro;")

    #conLog1.commit()
    
    log_data1 = cursorObjl1.fetchall()
 
    header_labels = ['fecha', 'tipo', 'producto', 'cantidad', 'destino', 'proveedor']  
    mainlogtab1.setRowCount(len(log_data1))
 

    for row in range(0, len(log_data1)):

        obj31=QTableWidgetItem()
        obj32=QTableWidgetItem()
        obj33=QTableWidgetItem()
        obj34=QTableWidgetItem()
        obj35=QTableWidgetItem()
        obj36=QTableWidgetItem()

        mainlogtab1.setItem(row,0,obj31) # Y is the column that you want to insert data
        mainlogtab1.item(row,0).setText(str(log_data1[row][0]))
        mainlogtab1.setItem(row,1,obj32) # Y is the column that you want to insert data
        mainlogtab1.item(row,1).setText(str(log_data1[row][1]))
        mainlogtab1.setItem(row,2,obj33) # Y is the column that you want to insert data
        mainlogtab1.item(row,2).setText(str(log_data1[row][2]))
        mainlogtab1.setItem(row,3,obj34) # Y is the column that you want to insert data
        mainlogtab1.item(row,3).setText(str(log_data1[row][3]))
        mainlogtab1.setItem(row,4,obj35) # Y is the column that you want to insert data
        mainlogtab1.item(row,4).setText(str(log_data1[row][4]))
        mainlogtab1.setItem(row,5,obj36) # Y is the column that you want to insert data
        mainlogtab1.item(row,5).setText(str(log_data1[row][5]))

    logwindow1.show()

### Funcion Vaciar Reporte Stock
def dumpStockR():
    FinalDump1=[]
    conStockR = connection
    cursorObjsR1 = conStockR.cursor()
    cursorObjsR1.execute("SELECT producto, cantidad FROM stock1;")
    #conStockR.commit()
    stock_R_data1 = cursorObjsR1.fetchall()
    header_labels = ['Producto', 'Cantidad']  
    #mainstocktab1.setRowCount(len(stock_R_data1))
    for row in range(0, len(stock_R_data1)):

        tempDump1=[]
        tempDump1.append(str(stock_R_data1[row][0]))
        tempDump1.append(str(stock_R_data1[row][1]))
        FinalDump1.append(tempDump1)
    namecsvf1= str(str(int(time.time()))+'_'+'stock_report.csv')
    with open('reportes/'+namecsvf1, 'w') as f:
        write = csv.writer(f) 
        #write = csv.DictWriter(open(namecsvf1,'w'), delimiter=',', lineterminator='\n', fieldnames=header_labels)
        #write.writerow(dict((fn,fn) for fn in header_labels))
        write.writerow(header_labels) 
        write.writerows(FinalDump1)
    
### Funcion Vaciar Reporte Registro
def dumpLogR():
    
    FinalDumpR1=[]
    conLogR1 = connection
    cursorObjlR1 = conLogR1.cursor()
    cursorObjlR1.execute("SELECT fecha, tipo, producto, cantidad, destino, proveedor FROM registro;")
    #conLogR1.commit()    
    log_R_data1 = cursorObjlR1.fetchall()
    header_labels = ['fecha', 'tipo', 'producto', 'cantidad', 'destino', 'proveedor']  
    for row in range(0, len(log_R_data1)):

        tempDump1=[]
        tempDump1.append(str(log_R_data1[row][0]))
        tempDump1.append(str(log_R_data1[row][1]))
        tempDump1.append(str(log_R_data1[row][2]))
        tempDump1.append(str(log_R_data1[row][3]))
        tempDump1.append(str(log_R_data1[row][4]))
        tempDump1.append(str(log_R_data1[row][5]))
        FinalDumpR1.append(tempDump1)
    namecsvf2= str(str(int(time.time()))+'_'+'registro_report.csv')
    with open('reportes/'+namecsvf2, 'w') as f:
        write = csv.writer(f) 
        write.writerow(header_labels)
        write.writerows(FinalDumpR1)


# conectar botones

##entrada
add_in1.clicked.connect(addinf1)
butGo1.clicked.connect(inFunct1)

##salida
add_out1.clicked.connect(addoutf1)
butGo2.clicked.connect(outFunct1)

#stock
view_stock1.clicked.connect(viewstockf1)

#registro
view_log1.clicked.connect(viewlogf1)
#reportes
sReportB1.clicked.connect(dumpStockR)
rReportB1.clicked.connect(dumpLogR)

print('3...')
mainUIwindow.show()
sys.exit(app.exec_())
print('4...')
