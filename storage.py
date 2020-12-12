import sqlite3

class DataBase:
	def __init__(self):
		self.cnct = sqlite3.connect('info.db')
		self.crs = self.cnct.cursor()
		self.create_table()

	def create_table(self):
		self.crs = self.cnct.execute('''CREATE TABLE IF NOT EXISTS point_table (
											user text, point int		)''')

	def insert_into(self, name_usr, point):
		self.crs.execute(f'''INSERT INTO point_table (user, point) 
								VALUES('{name_usr}', '{point}')''')
		self.cnct.commit()

	def select_all(self):
		self.crs.execute('''SELECT * FROM point_table ''')
		return self.crs.fetchall()

	def __del__(self):
		self.cnct.close()
