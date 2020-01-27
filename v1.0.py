# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_guif.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from xlrd import open_workbook



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(390, 450, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.password.setPlaceholderText("Account Password")
        self.first = QtWidgets.QRadioButton(self.centralwidget)
        self.first.setGeometry(QtCore.QRect(390, 310, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.first.setFont(font)
        self.first.setObjectName("first")
        book = open_workbook("som.xlsx")
        sheet = book.sheet_by_index(0)  # If your data is on sheet 1
        list_j = []
        for k in range(1, 5395):
            list_j.append(str(sheet.row_values(k)[2]))
        completer = QCompleter(list_j)
        self.destination_station = QtWidgets.QLineEdit(self.centralwidget)
        self.destination_station.setGeometry(QtCore.QRect(390, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.destination_station.setFont(font)
        self.destination_station.setObjectName("destination_station")
        self.destination_station.setPlaceholderText("To Station")
        self.destination_station.setCompleter(completer)
        self.check_price = QtWidgets.QPushButton(self.centralwidget)
        self.check_price.setGeometry(QtCore.QRect(440, 520, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.check_price.setFont(font)
        self.check_price.setObjectName("check_price")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(390, 400, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(390, 160, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(390, 160, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setMinimumDate(QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.second = QtWidgets.QRadioButton(self.centralwidget)
        self.second.setEnabled(True)
        self.second.setGeometry(QtCore.QRect(520, 310, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.second.setFont(font)
        self.second.setTabletTracking(False)
        self.second.setAcceptDrops(False)
        self.second.setAutoFillBackground(False)
        self.second.setChecked(True)
        self.second.setObjectName("second")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(390, 400, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.username.setPlaceholderText("Account Username")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 310, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 450, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(390, 210, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit.setTime(QtCore.QTime.currentTime())
        #self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.timeEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 101, 81))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("images.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.origin_station = QtWidgets.QLineEdit(self.centralwidget)
        self.origin_station.setGeometry(QtCore.QRect(390, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.origin_station.setFont(font)
        self.origin_station.setObjectName("origin_station")
        self.origin_station.setPlaceholderText("From Station")
        self.origin_station.setFocus()
        self.origin_station.setCompleter(completer)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 210, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 110, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.book_ticket = QtWidgets.QPushButton(self.centralwidget)
        self.book_ticket.setGeometry(QtCore.QRect(220, 520, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.book_ticket.setFont(font)
        self.book_ticket.setObjectName("book_ticket")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 400, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 160, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.book_ticket.clicked.connect(self.book_ticket_now)
        self.check_price.clicked.connect(self.check_price_now)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DB Auto Booking"))
        self.first.setText(_translate("MainWindow", "1st Class"))
        self.check_price.setText(_translate("MainWindow", "Check Price"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "h:mm AP"))
        self.second.setText(_translate("MainWindow", "2nd Class"))
        self.label_6.setText(_translate("MainWindow", "Travel Class"))
        self.label_8.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Time of Journey"))
        self.label_2.setText(_translate("MainWindow", "Destination Station"))
        self.book_ticket.setText(_translate("MainWindow", "Book Ticket"))
        self.label_7.setText(_translate("MainWindow", "User Name"))
        self.label.setText(_translate("MainWindow", "Origin Station"))
        self.label_3.setText(_translate("MainWindow", "Date of Journey"))

    def book_ticket_now(self):
        origin_station = self.origin_station.text()
        destination_station = self.destination_station.text()
        DOJ_i = self.dateEdit.date()
        DOJ = DOJ_i.toString('dd.MM.yyyy')
        time_of_journey_i = self.timeEdit.time()
        time_of_journey = time_of_journey_i.toString()
        if self.second.isChecked():
            travel_class = self.second.text()
        else:
            travel_class = self.first.text()
        username = self.username.text()
        password = self.password.text()

        driver = webdriver.Chrome(r"chromedriver.exe")
        driver.maximize_window()
        driver.get('https://www.bahn.com/en/view/index.shtml')
        act = ActionChains(driver)


        origin = driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-from']")
        destination = driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-to']")

        ##Passenger details
        no_of_travellers = '1 traveller'
        reserve_ticket = 'No'

        ##Home_page
        origin.clear()
        origin.send_keys(origin_station)
        destination.clear()
        destination.send_keys(destination_station)
        date = driver.find_element_by_xpath(
            "//body/div[@id='doc']/div[@class='content clearfix']/div[@id='content']/div[@id='inhalt']/div[@class='section clearfix full-width']/div[@id='sectionQF']/div[@id='js-tab-auskunft']/div/form/fieldset[@class='connection']/div[@class='fieldset-wrapper-inner clearfix']/div[@class='date-wrapper pull-left']/button[1]")
        date_i = driver.find_element_by_xpath("//input[@placeholder='Outward journey']")
        date_i.clear()
        date_i.click()
        driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-from']").click()
        date_i.send_keys(DOJ)
        time_travel = driver.find_element_by_xpath("//div[@id='js-auskunft-timeinput']//input[@placeholder='Time']")
        time_travel.click()
        for i in range(0, 2):
            time_travel.send_keys(Keys.BACK_SPACE)
        for i in range(0, 3):
            time_travel.send_keys(Keys.DELETE)
        time_travel.send_keys(time_of_journey)
        time_travel.click()
        if travel_class == '2nd Class':
            driver.find_element_by_xpath("//div[@id='js-tab-auskunft']//div//label[contains(text(),'2nd class')]").click()
        else:
            driver.find_element_by_xpath("//div[@id='js-tab-auskunft']//div//label[contains(text(),'1st class')]").click()
        search = driver.find_element_by_xpath("//input[@class='btn pull-right js-submit-btn']").click()
        driver.implicitly_wait(5)

        ##Search_page
        choose_train = driver.find_element_by_xpath("//body//tbody[2]")
        fair_price = driver.find_elements_by_xpath("//span[@class='fareOutput']")
        train_time = driver.find_element_by_xpath("//td[@class='time' ]")
        offer_selection = driver.find_element_by_xpath("//a[@class='buttonbold']").click()

        ##Class_selection_page
        availablity_offer = driver.find_element_by_xpath("//label[contains(@title,'Outward journey')]").click()
        next_page = driver.find_element_by_xpath("//input[@id='availContinueButton']").click()

        ##Bahn_card
        try:
            bahn_card = driver.find_element_by_xpath("//img[@title = 'Did you know? With the BahnCard you save money each time you travel.']")
            driver.find_element_by_xpath("//label[@for='bc_no']").click()
            driver.find_element_by_xpath("//button[@name='dummy']").click()
        except NoSuchElementException:
            pass

        ##Login_page
        username_login = driver.find_element_by_xpath("//input[@id='login-input-loginname']")
        username_login.send_keys(username)
        password_login = driver.find_element_by_xpath("//input[@id='password']")
        password_login.send_keys(password)
        driver.find_element_by_xpath("//input[@id='button.login']").click()

        ##Ticket_reservation
        if reserve_ticket == 'No':
            driver.find_element_by_xpath("//input[@id='buchenwunsch-button-weiter-id']").click()
        driver.find_element_by_xpath("//input[@id='button.weiter']").click()
        if travel_class == '1st Class':
            driver.find_element_by_xpath("//input[@id='button.weiter']").click()
    def check_price_now(self):
        origin_station = self.origin_station.text()
        destination_station = self.destination_station.text()
        DOJ_i = self.dateEdit.date()
        DOJ = DOJ_i.toString('dd.MM.yyyy')
        time_of_journey_i = self.timeEdit.time()
        time_of_journey = time_of_journey_i.toString()
        if self.second.isChecked():
            travel_class = self.second.text()
        else:
            travel_class = self.first.text()
        username = self.username.text()
        password = self.password.text()

        driver = webdriver.Chrome(r"chromedriver.exe")
        driver.maximize_window()
        driver.get('https://www.bahn.com/en/view/index.shtml')
        act = ActionChains(driver)

        origin = driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-from']")
        destination = driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-to']")

            ##Passenger details
        no_of_travellers = '1 traveller'
        reserve_ticket = 'No'

        ##Home_page
        origin.clear()
        origin.send_keys(origin_station)
        destination.clear()
        destination.send_keys(destination_station)
        date = driver.find_element_by_xpath(
            "//body/div[@id='doc']/div[@class='content clearfix']/div[@id='content']/div[@id='inhalt']/div[@class='section clearfix full-width']/div[@id='sectionQF']/div[@id='js-tab-auskunft']/div/form/fieldset[@class='connection']/div[@class='fieldset-wrapper-inner clearfix']/div[@class='date-wrapper pull-left']/button[1]")
        date_i = driver.find_element_by_xpath("//input[@placeholder='Outward journey']")
        date_i.clear()
        date_i.click()
        driver.find_element_by_xpath("//input[@id='js-auskunft-autocomplete-from']").click()
        date_i.send_keys(DOJ)
        time_travel = driver.find_element_by_xpath("//div[@id='js-auskunft-timeinput']//input[@placeholder='Time']")
        time_travel.click()
        for i in range(0, 2):
            time_travel.send_keys(Keys.BACK_SPACE)
        for i in range(0, 3):
            time_travel.send_keys(Keys.DELETE)
        time_travel.send_keys(time_of_journey)
        time_travel.click()
        if travel_class == '2nd Class':
            driver.find_element_by_xpath(
                "//div[@id='js-tab-auskunft']//div//label[contains(text(),'2nd class')]").click()
        else:
            driver.find_element_by_xpath(
                "//div[@id='js-tab-auskunft']//div//label[contains(text(),'1st class')]").click()
        search = driver.find_element_by_xpath("//input[@class='btn pull-right js-submit-btn']").click()
        driver.implicitly_wait(5)

        ##Search_page
        choose_train = driver.find_element_by_xpath("//body//tbody[2]")
        fair_price = driver.find_elements_by_xpath("//span[@class='fareOutput']")
        train_time = driver.find_element_by_xpath("//td[@class='time' ]")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
