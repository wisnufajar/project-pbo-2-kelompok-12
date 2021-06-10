from Database import *

class Model:
	"""docstring for Model"""
	def __init__(self):
		self.database = Database()
		self.table_barang = ('id_barang','jenis_barang','merk','warna','ukuran','jumlahstok')
		self.table_admin = ['ID','Nama', 'Username', 'Password']
		self.table_detail_transaksi = ["id_transaksi","id_barang","jumlah","masuk/keluar","tanggal"]


	def getDataBarang(self):
		return self.database.fetchall("SELECT * FROM barang")

	def userValidation(self,usr,passwd):
		query = f"SELECT * FROM admin WHERE username='{usr}' AND password='{passwd}'"
		try:
			return self.database.fetchall(query)[0][0]
		except Exception as e:
			return False

	def deleteByID(self,id_item):
		query = f"DELETE FROM barang WHERE id_barang={id_item}"
		return self.database.execute(query)

	def insertBarang(self,data):
		query = f"""INSERT INTO `barang` (`jenis_barang`,`merk`,`warna`,`ukuran`,`jumlahstok`) VALUES {data};"""
		return self.database.execute(query)

	def getBarangByID(self,id_item):
		query = f"SELECT * FROM barang WHERE id_barang='{id_item}'"
		return self.database.fetchone(query)

	def updateBarang(self, data):
		query = f"UPDATE barang SET {self.table_barang[1]}='{data[1]}',{self.table_barang[2]}='{data[2]}',{self.table_barang[3]}='{data[3]}',{self.table_barang[4]}='{data[4]}',{self.table_barang[5]}='{data[5]}' WHERE {self.table_barang[0]} = {data[0]}"
		return self.database.execute(query)

	def searchByKeyword(self,keyword):
		query = f"SELECT * FROM barang WHERE {self.table_barang[0]} LIKE '%{keyword}%' OR {self.table_barang[1]} LIKE '%{keyword}%' OR {self.table_barang[2]} LIKE '%{keyword}%' OR {self.table_barang[3]} LIKE '%{keyword}%' OR {self.table_barang[4]} LIKE '%{keyword}%' OR {self.table_barang[5]} LIKE '%{keyword}%'"
		return self.database.fetchall(query)

	def searchByKeywordTr(self,keyword):
		query = f"SELECT * FROM detail_transaksi WHERE {self.table_detail_transaksi[1]} LIKE '%{keyword}%' OR {self.table_detail_transaksi[2]} LIKE '%{keyword}%' OR {self.table_detail_transaksi[4]} LIKE '%{keyword}%'"
		return self.database.fetchall(query)


	def getDataAdmin(self):
		return self.database.fetchall("SELECT * FROM admin")

	def getAdminByID(self,id_item):
		query = f"SELECT * FROM admin WHERE id_admin='{id_item}'"
		return self.database.fetchone(query)

	def updateAdmin(self, *data):
		query = f"UPDATE admin SET {self.table_admin[2]}='{data[1]}',{self.table_admin[3]}='{data[2]}' WHERE id_admin = {data[0]}"
		return self.database.execute(query)

	def getDataTransaksi(self):
		return self.database.fetchall("SELECT * FROM detail_transaksi")

	def updateBrgMasuk(self, data):
		query = f"UPDATE barang SET {self.table_barang[5]} = {self.table_barang[5]} + {data[5]} WHERE id_barang = {data[0]}"
		return self.database.execute(query)

	def insertBrgMasuk(self,data):
		query = f"""INSERT INTO `detail_transaksi` (`id_barang`,`jumlah`,`masuk/keluar`,`tanggal`) VALUES {data};"""
		return self.database.execute(query)

	def updateBrgKeluar(self, data):
		query = f"UPDATE barang SET {self.table_barang[5]} = {self.table_barang[5]} - {data[5]} WHERE id_barang = {data[0]}"
		return self.database.execute(query)

	def insertBrgKeluar(self,data):
		query = f"""INSERT INTO `detail_transaksi` (`id_barang`,`jumlah`,`masuk/keluar`,`tanggal`) VALUES {data};"""
		return self.database.execute(query)

	def getJumlahStokByID(self,id_barang) :
		query = f"SELECT jumlahstok FROM barang WHERE id_barang='{id_barang}'"
		return self.database.fetchone(query)

