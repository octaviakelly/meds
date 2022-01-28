import os
import sqlite3 as sqlite

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
        dbConnCur.close()


create_database()