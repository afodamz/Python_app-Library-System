import sqlite3
#=============backend================

def ConnectData():
    con = sqlite3.connect("Libbooks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks (id INTEGER PRIMARY KEY, MTy text,Ref text,Tit text, Fna text,\
                Sna text,Adr1 text,Adr2 text,pcd text,MNo text,BkID text,Atr text,DBo text,\
                Ddu text,spr text,LrF text,Dod text, DonL text)")
    con.commit()
    con.close()

def addDataRec(MTy,Ref,Tit,Fna,Sna,Adr1,Adr2,Pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                (MTy,Ref,Tit,Fna,Sna,Adr1,Adr2,Pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM  libbooks")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("DELETE FROM  libbooks WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(MTy="",Ref="",Tit="",Fna="",Sna="",
               Adr1="",Adr2="",Pcd="",MNo="",BkID="",
               Bkt="",Atr="",DBo="",Ddu="",sPr="",LrF="",DoD="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM libbooks WHERE MTy=? OR Ref=? OR Tit=? OR Fna=? OR Sna=? OR\
               Adr1=? OR Adr2=? OR Pcd=? OR MNo=? OR BkID=? OR Bkt=? OR Atr=? OR DBo=? OR Ddu=? OR\
               sPr=? OR LrF=? OR DoD=? OR DonL=?", \
                      (MTy,Ref,Tit,Fna,Sna,Adr1,Adr2,Pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL))
    rows=cur.fetchall()
    con.close()
    return rows

def dataUpdate(id, MTy="",Ref="",Tit="",Fna="",Sna="",
               Adr1="",Adr2="",Pcd="",MNo="",BkID="",
               Bkt="",Atr="",DBo="",Ddu="",sPr="",LrF="",DoD="",DonL=""):
    con=sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("UPDATE libbooks SET MTy=?, Ref=?, Tit=?, Fna=?, Sna=?,\
               Adr1=?, Adr2=?, Pcd=?, MNo=?, BkID=?, Bkt=?, Atr=?, DBo=?, Ddu=?,\
               sPr=?, LrF=?, DoD=?, DonL=? WHERE id=?", \
                      (MTy,Ref,Tit,Fna,Sna,Adr1,Adr2,Pcd,MNo,BkID,Bkt,Atr,DBo,Ddu,sPr,LrF,DoD,DonL, id))
    con.commit()
    con.close()

ConnectData()