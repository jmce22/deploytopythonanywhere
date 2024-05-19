# Gym DAO

import pymysql
import pymysql.cursors
import pa as cfg
class GymDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = pymysql.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql= "select * from gym"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from gym where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, gym):
        cursor = self.getcursor()
        sql="insert into gym (name, sex, age, height, weight) values (%s,%s,%s,%s,%s)"
        values = (gym.get("name"), gym.get("sex"), gym.get("age"), gym.get("height"), gym.get("weight"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        gym["id"] = newid
        self.closeAll()
        return gym

    def update(self, id, gym):
        cursor = self.getcursor()
        sql="update gym set name= %s, sex=%s, age=%s, height=%s, weight=%s where id = %s"
        values = (gym.get("name"), gym.get("sex"), gym.get("age"), gym.get("height"), gym.get("weight"), id)
        cursor.execute(sql, values)
        
        self.connection.commit()
        self.closeAll()
        return gym
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from gym where id = %s"
        values = (id,)
        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        # print("delete done")
        return True

    def convertToDictionary(self, resultLine):
        attkeys=['id','name','sex', 'age', 'height', 'weight']
        gym = {}
        currentkey = 0
        for attrib in resultLine:
            gym[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return gym

        
gymDAO = GymDAO()