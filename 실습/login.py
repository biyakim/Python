def login(id,pw):
    if id=="idid" and pw==1010:
        return True
    else:
        return False
print("login(id=idid,pw=1010)",login("idid",1010))
print("login(id=idd,pw=1020)",login("idd",1020))