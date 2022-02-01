import os
import sqlite3 as sqlite

import matplotlib.pyplot as plt

def create_database():
    os.chdir(os.path.dirname(__file__))
    curPath = os.getcwd()
    print("curPath: ",curPath)
    dbPath = curPath+"\meds.db"
    dbConn = sqlite.connect(dbPath)
    with dbConn:
        dbConnCur=dbConn.cursor()
        medsDb_selectAll="""SELECT * FROM meds"""
        dbConnCur.execute(medsDb_selectAll)
        medRecs=dbConnCur.fetchall()
        lenMedRecs=len(medRecs)
        print("No. of records in meds.db: ",lenMedRecs)
        for row in medRecs:
            print("ID: ",row[0])
            print("Date: ", row[3])
            print("Height: ", row[1])
            print("Weight: ", row[2])
            print("Systolic: ", row[4])
            print("Diastolic: ", row[5])
            print("Heart rate: ", row[6])
            print("Dose: ", row[7])
            print("\n")
        heartRate = dbConnCur.execute("SELECT Heart_rate FROM meds")
        global heartRateTup
        heartRateTup=()
        for item in heartRate:
            heartRateTup+=item
        dose = dbConnCur.execute("SELECT dose FROM meds")
        global doseTup
        doseTup=()
        for item in dose:
            doseTup+=item
        systolic = dbConnCur.execute("SELECT Systolic_BP FROM meds")
        global systolicTup
        systolicTup = ()
        for item in systolic:
            systolicTup += item

        dbConnCur.close()

create_database()

plt.subplot(2,1,1)
plt.plot(doseTup, heartRateTup)
plt.xlabel("Dose (mg)")
plt.ylabel("Heart rate (bpm)")
plt.subplot(2,1,2)
plt.plot(doseTup, systolicTup)
plt.xlabel("Dose (mg)")
plt.ylabel("Systolic bp")
plt.show()
plt.boxplot(systolicTup)
plt.title("Looking for outlying systolic bp measurements")
plt.ylabel("Systolic bp")
plt.show()


