#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector as sql

connection = sql.connect(
    host="localhost",
    user="root",
    password="20030701Ae.moon",
    auth_plugin='mysql_native_password',
    database ='foodly3'
)

print(connection)


# In[2]:


cursor = connection.cursor()

cursor.execute("SELECT * FROM aliment")
tables = cursor.fetchall()
for table in tables:
    print(table)

connection.commit()


# In[3]:


cursor.execute("SELECT * FROM `aliment` WHERE `calories` < 90")
tables = cursor.fetchall()
for table in tables:
    print(table)


# In[4]:


cursor.execute("SELECT COUNT(*) FROM `utilisateur` WHERE `email` LIKE '%gmail.com'")
tables = cursor.fetchall()
for table in tables:
    print(table)


# In[5]:


cursor.execute("SELECT * FROM `aliment` ORDER BY `calories` ASC")
tables = cursor.fetchall()
for table in tables:
    print(table)


# In[6]:


cursor.execute("SELECT * FROM utilisateur")
tables = cursor.fetchall()
for table in tables:
    print(table)

connection.commit()


# In[7]:


insert_sexe = """
    ALTER TABLE utilisateur 
    ADD `sexe` VARCHAR(255)
"""
cursor.execute(insert_sexe)
connection.commit()


# In[8]:


cursor.execute("SELECT  * FROM utilisateur")
tables = cursor.fetchall()
for table in tables:
    print(table)


# In[9]:


cursor.execute("UPDATE utilisateur SET sexe = 'Homme' WHERE id  = '3'")
connection.commit()


# In[10]:


insert = """
    INSERT INTO `utilisateur` (`nom`, `prenom`, `email`, `langue_id`, `sexe`)
    VALUES
    ('bayar', 'moon', 'moonb@yahoo.fr', 1, 'Homme'),
    ('chaipas', 'hadjer', 'hadjerc@hotmail.com', 1, 'Femme'),
    ('chikri', 'hassan', 'hassanc@orange.fr', 1, 'Homme'),
    ('Marti', 'Emil', 'emilm@gmail.com', 1, 'Femme')
"""
cursor.execute(insert)
connection.commit()


# In[11]:


cursor.execute("ALTER TABLE utilisateur DROP COLUMN `sexe`")


# In[ ]:




