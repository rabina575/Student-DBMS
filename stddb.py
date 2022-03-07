import mysql.connector as A


def studentData():
    mycon=A.connect(host="localhost", user="root",password="sakuya",database="mis")
    con=mycon.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY, AdmissionNo text, StudentName text, Class text, DateOfBirth text, Age text,Gender text, Address text, ContactNo text)")
    mycon.commit()
    mycon.close()

def viewData():
    mycon=A.connect(host="localhost", user="root",password="sakuya",database="mis")
    con=mycon.cursor()
    con.execute("SELECT * FROM student")
    rows=con.fetchall()
    mycon.close()
    return rows


def addStdRec(AdmissionNo, StudentName, Class, DateOfBirth, Age,Gender, Address, ContactNo):
    mycon=A.connect(host="localhost", user="root",password="sakuya",database="mis")
    con=mycon.cursor()
    con.execute("INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(AdmissionNo, StudentName, Class, DateOfBirth, Age,Gender, Address, ContactNo))
    mycon.commit()
    mycon.close()

def deleteRec(id):
    mycon=A.connect(host="localhost", user="root",password="sakuya",database="mis")
    con=mycon.cursor()

    con.execute("DELETE FROM student WHERE id=%s",(id,))
    mycon.commit()
    mycon.close()


def dataUpdate(id,AdmissionNo="", StudentName="", Class="", DateOfBirth="", Age="",Gender="", Address="", ContactNo=""):
    mycon=A.connect(host="localhost", user="root",password="sakuya",database="mis")
    con=mycon.cursor()
    con.execute("UPDATE student SET AdmissionNo=%s, StudentName=%s, Class=%s, DateOfBirth=%s, Age=%s,Gender=%s, Address=%s, ContactNo=%s WHERE id='%s'",\
                (AdmissionNo, StudentName, Class, DateOfBirth, Age,Gender, Address, ContactNo,id))
    mycon.commit()
    mycon.close()



# studentData()
# viewData()
