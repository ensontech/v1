###########################################################
### This is the matrix of python functions that run V1 on the server! ###
###########################################################

### The following modules must be imported first ###

import _mysql as mysql

### From here, we have functions ###

### The following functions are all related to sql queries ###

### This is a select query function for sql ###

def sqlselect(field,table,where,var,verbose):
    db = mysql.connect(host="localhost", port=3306, user="root", passwd="Cheddar1$", db="v1")
    q = 'SELECT {field} FROM `{table}` WHERE {where}="{var}"'.format(field=field,table=table,where=where,var=var)
    db.query(q)
    if verbose == 'v':
        results = db.store_result()
        for r in results.fetch_row(0):
            return str(r[0])
    else:
        results = db.store_result()
        return results.fetch_row(0)

### This is a insert command function for sql ###

def sqlinsert(table,var):
    db = mysql.connect(host="localhost", port=3306, user="root", passwd="Cheddar1$", db="v1")
    q = 'INSERT INTO `{table}` VALUES {var}'.format(table=table,var=var)
    db.query(q)

### This is an update command function for sql ###

def sqlupdate(table,setv,val,where,var):
    db = mysql.connect(host="localhost", port=3306, user="root", passwd="Cheddar1$", db="v1")
    q = 'UPDATE `{table}` SET {setv}="{val}" WHERE {where}="{var}"'.format(table=table,setv=setv,val=val,where=where,var=var)
    db.query(q)

### This is a delete command function for sql ###

def sqldelete(table,where,var):
    db = mysql.connect(host="localhost", port=3306, user="root", passwd="Cheddar1$", db="v1")
    q = 'DELETE FROM `{table}` WHERE {where}="{var}"'.format(table=table,where=where,var=var)
    db.query(q)

### This sql function creates tables copied from current table templates ###

def sqlcreate(tablename,template):
    db = mysql.connect(host="localhost", port=3306, user="root", passwd="Cheddar1$", db="v1")
    q = 'CREATE TABLE `{tablename}` LIKE {template}'.format(tablename=tablename,template=template)
    db.query(q)
    
    
    ### END OF FILE ###
