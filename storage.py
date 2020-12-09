import sqlite3


class Storage:
	def __init__(self, name='data.db'):
		self.nameDB = name
		self.cnct = sqlite3.connect(self.nameDB)
		self.crs = self.cnct.cursor()
		self.create_table()

	def create_table(self, name='init'):
		self.crs = self.cnct.execute(f'''CREATE TABLE IF NOT EXISTS '{name}' (
											name text, score int		)''')

	def insert_into(self, name_usr, score, name='init'):
		self.crs.execute(f'''INSERT INTO {name} (name, score) VALUES('{name_usr}', '{score}')''')
		self.cnct.commit()

	def select_all(self, name='init'):
		self.crs.execute(f'''SELECT * FROM {name} ''')
		return self.crs.fetchall()

	def del_table(self, name='init'):
		self.crs.execute(f'''DROP TABLE '{name}' ''')

	def __del__(self):
		self.cnct.close()
