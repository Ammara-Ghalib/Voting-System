import sqlite3
def main():
    db=sqlite3.connect("vote_system3.db")

    #create voters table and dummy data
    db.execute('drop table if exists registered_voters')
    sql='create table registered_voters(id INTEGER PRIMARY KEY AUTOINCREMENT,cnic text NOT NULL,name text NOT NULL,city text NOT NULL,gender text NOT NULL,age text NOT NULL)'
    db.execute(sql)
    #sql='insert into registered_voters(cnic,name,city,gender,age) values(?,?,?,?,?)'
    #db.execute(sql,("3740695988764","Fizzah","Lahore","Female","25"))
    db.commit()

    #create votes_casted table and dummy data
    db.execute('drop table if exists votes_casted')
    sql='create table votes_casted(id INTEGER PRIMARY KEY AUTOINCREMENT,cnic text NOT NULL,candidate text NOT NULL,city text NOT NULL)'
    db.execute(sql)


    #create candidates table and dummy data
    db.execute('drop table if exists candidates')
    sql='create table candidates(id INTEGER PRIMARY KEY AUTOINCREMENT,name text NOT NULL,city text NOT NULL,image text NOT NULL,party text NOT NULL)'
    db.execute(sql)
  

    #create location table and dummy data
    db.execute('drop table if exists location')
    sql='create table location(id INTEGER PRIMARY KEY AUTOINCREMENT,city text NOT NULL)'
    db.execute(sql)
    sql='insert into location(city) values(?)'
    db.execute(sql,("Rawalpindi",))
    sql='insert into location(city) values(?)'
    db.execute(sql,("Lahore",))
    sql='insert into location(city) values(?)'
    db.execute(sql,("Peshawar",))
    sql='insert into location(city) values(?)'
    db.execute(sql,("Karachi",))
    db.commit()

if __name__ == "__main__":main()
