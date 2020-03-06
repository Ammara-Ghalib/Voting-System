import sqlite3
def main():
    cnic=sqlite3.connect('Cdatabase.db')
    cnic.execute('drop table if exists cnic_numbers')
    sql='create table cnic_numbers(id INTEGER PRIMARY KEY AUTOINCREMENT,cnic text NOT NULL,name text NOT NULL,city text NOT NULL,gender text NOT NULL,age text NOT NULL)'
    cnic.execute(sql)
    sql='insert into cnic_numbers(cnic,name,city,gender,age) values(?,?,?,?,?)'
    cnic.execute(sql,("3740695988764","Fizzah Hashmi","Lahore","Female","19"))
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (6110184227822, 'Iqra Shahid', 'Islamabad','Female',20 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3740588435886, 'Ammara Ghalib', 'RawalPindi','Female',19 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3840378745742, 'Shifa Shariq', 'Wah','Female',20)")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3420215817806, 'Mariam Nasim', 'Khariyan','Female',20 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3530276257352, 'Noor Naqvi', 'RawalPindi','Female',19 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3820198714765, 'Fatima Arshad', 'RawalPindi','Female',19 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (4220108092368, 'Hamnah', 'Abu Daibi','Female',20 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (3620220031668, 'Mona Fiaz', 'Saudia Arab','Female',21 )")
    cnic.execute("INSERT INTO cnic_numbers (cnic,name,city,gender,age) \
      VALUES (6110117041696, 'Tehreem', 'Islamabad','Female',20 )");

    cnic.commit()
    cursor = cnic.execute("SELECT id,cnic, name, city, gender,age from cnic_numbers")
    for row in cursor :
        print( "ID  =  ",row[0])
        print( "cnic  =  ",row[1])
        print( "name  =  ",row[2])
        print( "city  =  ",row[3])
        print( "gender  =  ",row[4])
        print ("age  =  ",row[5]," \n")

    cnic.close()
if __name__ == "__main__":main()
        
        
