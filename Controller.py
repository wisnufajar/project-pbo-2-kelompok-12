import wx
import Views
import Model
from datetime import datetime

class Gudang:
	"""docstring for Gudang"""
	def __init__(self):
		self.model = Model.Model()
		self.viewLogin = Views.loginFrame(None)
		self.viewBeranda = Views.beranda(None)
		self.viewStok = Views.cekStok(None)
		self.viewTambahBarang = Views.TambahBarang(None)
		self.viewEditBarang = Views.EditBarang(None)
		self.viewAdmin = Views.DataAdmin(None)
		self.viewTransaksi = Views.transaksi(None)
		self.viewDetailTransaksi = Views.DetailTransaksi(None)
		self.viewBrgMasuk = Views.BrgMasuk (None)
		self.viewBrgKeluar = Views.BrgKeluar (None)

		# Connect Events
		self.set_event_login()
		self.set_event_beranda()
		self.set_event_stok()
		self.set_event_tambahbarang()
		self.set_event_editbarang()
		self.set_event_admin()
		self.set_event_transaksi()
		self.set_event_detail_transaksi()
		self.set_event_Brg_masuk()
		self.set_event_Brg_keluar()

		# inital attribute
		self.stokSelected = None
		self.adminSelected = None
		self.TransaksiSelected = None

###########################################################################
## Edit Barang
###########################################################################
	def set_event_editbarang(self):
		self.viewEditBarang.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandleEditBarangBack )
		self.viewEditBarang.m_buttonSimpan.Bind( wx.EVT_BUTTON, self.HandleSimpanBarang )

	def HandleEditBarangBack(self,event):
		self.viewEditBarang.Hide()
		return self.viewStok.Show()

	def HandleSimpanBarang(self, event):
		jenis = self.viewEditBarang.m_textCtrlJenisBarang.GetValue()
		merk = self.viewEditBarang.m_textCtrlMerk.GetValue()
		warna = self.viewEditBarang.m_textCtrlWarna.GetValue()
		ukuran = self.viewEditBarang.m_textCtrlUkuran.GetValue()
		stok = self.viewEditBarang.m_textCtrlJumlahStok.GetValue()
		if stok.isnumeric():
			id_barang = self.viewStok.m_listCtrl4.GetItemText(self.stokSelected,0)
			self.model.updateBarang((id_barang,jenis,merk,warna,ukuran,int(stok)))
			self.resetFormEdit()
			self.viewEditBarang.Hide()
			self.viewStok.LimitData.SetMax(len(self.getDataBarang()))
			self.viewStok.Show()
			return self.set_BodyTableBarang()

	def resetFormEdit(self):
		self.viewEditBarang.m_textCtrlJenisBarang.SetValue('')
		self.viewEditBarang.m_textCtrlMerk.SetValue('')
		self.viewEditBarang.m_textCtrlWarna.SetValue('')
		self.viewEditBarang.m_textCtrlUkuran.SetValue('')
		self.viewEditBarang.m_textCtrlJumlahStok.SetValue('')
		self.stokSelected = None


###########################################################################
## Tambah Barang
###########################################################################
	def set_event_tambahbarang(self):
		self.viewTambahBarang.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandleTambahBarangBack )
		self.viewTambahBarang.m_buttonTambah.Bind( wx.EVT_BUTTON, self.HandleTambahBarang )		

	def HandleTambahBarangBack(self,event):
		self.resetForm()
		self.viewTambahBarang.Hide()
		return self.viewStok.Show()

	def HandleTambahBarang(self,event):
		jenis = self.viewTambahBarang.m_textCtrlJenisBarang.GetValue()
		merk = self.viewTambahBarang.m_textCtrlMerk.GetValue()
		warna = self.viewTambahBarang.m_textCtrlWarna.GetValue()
		ukuran = self.viewTambahBarang.m_textCtrlUkuran.GetValue()
		stok = self.viewTambahBarang.m_textCtrlJumlahStok.GetValue()
		if stok.isnumeric():
			self.model.insertBarang((jenis,merk,warna,ukuran,int(stok)))
			self.resetForm()
			self.viewStok.LimitData.SetMax(len(self.getDataBarang()))
			self.viewTambahBarang.Hide()
			self.viewStok.Show()
			return self.set_BodyTableBarang()

	def resetForm(self):
		self.viewTambahBarang.m_textCtrlJenisBarang.SetValue('')
		self.viewTambahBarang.m_textCtrlMerk.SetValue('')
		self.viewTambahBarang.m_textCtrlWarna.SetValue('')
		self.viewTambahBarang.m_textCtrlUkuran.SetValue('')
		self.viewTambahBarang.m_textCtrlJumlahStok.SetValue('')

###########################################################################
## Login
###########################################################################
	def set_event_login(self):
		self.viewLogin.btn_login.Bind( wx.EVT_BUTTON, self.btn_login_onclick )

	def btn_login_onclick(self,event):
		usr = self.viewLogin.text_email.GetValue()
		passwd = self.viewLogin.text_password.GetValue()
		if self.model.userValidation(usr,passwd):
			self.viewLogin.Destroy()
			return self.viewBeranda.Show()
		return wx.MessageDialog(None,f"Username/Password Salah",'Gagal!',wx.OK|wx.ICON_INFORMATION).ShowModal()

###########################################################################
## Beranda
###########################################################################
	def set_event_beranda(self):
		self.viewBeranda.btnCekStok.Bind( wx.EVT_BUTTON, self.HandleBtnTampilStok )
		self.viewBeranda.btnAkunSetting.Bind( wx.EVT_BUTTON, self.HandleBtnAkunSeting )
		self.viewBeranda.btnTransaksi.Bind( wx.EVT_BUTTON, self.HandleBtnTransaksi )

	def HandleBtnTampilStok(self, event):
		self.viewBeranda.Hide()
		self.viewStok.Show()
		self.set_BodyTableBarang()

	def HandleBtnAkunSeting(self, event):
		self.viewBeranda.Hide()
		self.viewAdmin.Show()
		self.set_BodyTableAdmin()

	def HandleBtnTransaksi(self, event):
		self.viewBeranda.Hide()
		self.viewTransaksi.Show()
		self.set_BodyTableBarangTr()

###########################################################################
## Cek Stok
###########################################################################
	def set_event_stok(self):
		self.viewStok.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItem )
		self.viewStok.LimitData.Bind( wx.EVT_SPINCTRL, self.limitData )
		self.viewStok.LimitData.Bind( wx.EVT_TEXT, self.limitData )
		self.viewStok.LimitData.Bind( wx.EVT_TEXT_ENTER, self.limitData )
		self.viewStok.LimitData.SetMax(len(self.getDataBarang()))
		self.viewStok.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBack )
		self.viewStok.BtnHapusData.Bind( wx.EVT_BUTTON, self.HandleBtnHapus )
		self.viewStok.BtnEditData.Bind( wx.EVT_BUTTON, self.HandleBtnEdit )
		self.viewStok.BtnTambahData.Bind( wx.EVT_BUTTON, self.HandleBtnTambah )
		self.viewStok.m_searchCtrl1.Bind( wx.EVT_TEXT, self.onSearch )

	def onSearch(self,event):
		keyword = self.viewStok.m_searchCtrl1.GetValue()
		if keyword != '':
			result = self.model.searchByKeyword(keyword)
			return self.set_BodyTableBarang(result)
		return self.set_BodyTableBarang()


	def valueLimitData(self):
		return self.viewStok.LimitData.GetValue()

	def limitData(self,event):
		return self.set_BodyTableBarang()

	def HandleSelectItem(self,event):
		self.stokSelected = event.GetIndex()

	def HandleBtnBack(self,event):
		self.viewStok.Hide()
		return self.viewBeranda.Show()
		
	def HandleBtnHapus(self,event):
		if self.stokSelected != None:
			r = wx.MessageDialog(None, 'Apakah Anda Yakin Ingin Menghapus Data Tersebut?', 'Hapus Data Barang', style=wx.ICON_WARNING | wx.YES_NO | wx.NO_DEFAULT).ShowModal()
			if r == wx.ID_YES:
				id_stok = self.viewStok.m_listCtrl4.GetItemText(self.stokSelected,0)
				self.model.deleteByID(id_stok)
				self.viewStok.LimitData.SetMax(len(self.getDataBarang()))
				self.stokSelected = None
				wx.MessageDialog(None, 'Data berhasil dihapus!!', 'Delete Success', style=wx.OK | wx.ICON_INFORMATION).ShowModal()
				return self.set_BodyTableBarang()

	def HandleBtnEdit(self,event):
		if self.stokSelected != None:
			self.viewStok.Hide()
			self.viewEditBarang.Show()
			id_barang = self.viewStok.m_listCtrl4.GetItemText(self.stokSelected,0)
			data = self.model.getBarangByID(id_barang)
			return self.fillFormEdit(data)

	def fillFormEdit(self,data):
		self.viewEditBarang.m_textCtrlJenisBarang.SetValue(data[1])
		self.viewEditBarang.m_textCtrlMerk.SetValue(data[2])
		self.viewEditBarang.m_textCtrlWarna.SetValue(data[3])
		self.viewEditBarang.m_textCtrlUkuran.SetValue(data[4])
		self.viewEditBarang.m_textCtrlJumlahStok.SetValue(f'{data[5]}')

	def HandleBtnTambah(self,event):
		self.viewStok.Hide()
		self.viewTambahBarang.Show()	

	def getDataBarang(self):
		return self.model.getDataBarang()

	def set_HeaderTableBarang(self):
		table = ['ID','Jenis', 'Merk', 'Warna', 'Ukuran', 'Stok']
		for i,j in enumerate(table):
			self.viewStok.m_listCtrl4.InsertColumn(i,j)

	def set_BodyTableBarang(self, data=None):
		data = self.getDataBarang() if data==None else data
		self.viewStok.m_listCtrl4.ClearAll()
		self.set_HeaderTableBarang()
		for index,row in enumerate(data):
			if index < self.valueLimitData():
				self.viewStok.m_listCtrl4.InsertItem(index,row[0])
				for i in range(6):
					self.viewStok.m_listCtrl4.SetItem(index,i, str(row[i]))

###########################################################################
## Transaksi
###########################################################################
	def set_event_transaksi(self):
		self.viewTransaksi.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItemTr )
		self.viewTransaksi.LimitData.Bind( wx.EVT_SPINCTRL, self.limitDataTr )
		self.viewTransaksi.LimitData.Bind( wx.EVT_TEXT, self.limitDataTr )
		self.viewTransaksi.LimitData.Bind( wx.EVT_TEXT_ENTER, self.limitDataTr )
		self.viewTransaksi.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackTr )
		self.viewTransaksi.LimitData.SetMax(len(self.getDataBarangTr()))
		self.viewTransaksi.m_searchCtrl1.Bind( wx.EVT_TEXT, self.onSearchTr )
		self.viewTransaksi.BtnBrgKeluar.Bind( wx.EVT_BUTTON, self.HandleBtnBrgKeluar )
		self.viewTransaksi.BtnDetailTransaksi.Bind( wx.EVT_BUTTON, self.HandleBtnDetail )
		self.viewTransaksi.BtnTambahMasuk.Bind( wx.EVT_BUTTON, self.HandleBtnBrgMasuk )

	def onSearchTr(self, event) :
		keyword = self.viewTransaksi.m_searchCtrl1.GetValue()
		if keyword != '':
			result = self.model.searchByKeyword(keyword)
			return self.set_BodyTableBarangTr(result)
		return self.set_BodyTableBarangTr()

	def HandleBtnBrgMasuk(self, event) :
		if self.stokSelected!= None:
			self.viewTransaksi.Hide()
			self.viewBrgMasuk.Show()
			id_barang = self.viewTransaksi.m_listCtrl4.GetItemText(self.stokSelected,0)
			data = self.model.getBarangByID(id_barang)
			return self.fillFormBrgMasuk(data)
	
	def HandleBtnBrgKeluar(self, event) :
		if self.stokSelected!= None:
			self.viewTransaksi.Hide()
			self.viewBrgKeluar.Show()
			id_barang = self.viewTransaksi.m_listCtrl4.GetItemText(self.stokSelected,0)
			data = self.model.getBarangByID(id_barang)
			return self.fillFormBrgKeluar(data)

	def fillFormBrgMasuk(self,data):
		self.viewBrgMasuk.m_textCtrlJenisBarangM.SetValue(data[1])
		self.viewBrgMasuk.m_textCtrlMerkM.SetValue(data[2])
		self.viewBrgMasuk.m_textCtrlWarnaM.SetValue(data[3])
		self.viewBrgMasuk.m_textCtrlUkuranM.SetValue(data[4])

	def fillFormBrgKeluar(self,data):
		self.viewBrgKeluar.m_textCtrlJenisBarangK.SetValue(data[1])
		self.viewBrgKeluar.m_textCtrlMerkK.SetValue(data[2])
		self.viewBrgKeluar.m_textCtrlWarnaK.SetValue(data[3])
		self.viewBrgKeluar.m_textCtrlUkuranK.SetValue(data[4])

	def HandleBtnBackTr(self, event) :
		self.viewTransaksi.Hide()
		return self.viewBeranda.Show()

	def valueLimitDataTr(self):
		return self.viewTransaksi.LimitData.GetValue()

	def limitDataTr(self,event):
		return self.set_BodyTableBarangTr()

	def HandleSelectItemTr(self,event):
		self.stokSelected = event.GetIndex()

	def getDataBarangTr(self):
		return self.model.getDataBarang()

	def set_HeaderTableBarangTr(self):
		table = ['ID','Jenis', 'Merk', 'Warna', 'Ukuran', 'Stok']
		for i,j in enumerate(table):
			self.viewTransaksi.m_listCtrl4.InsertColumn(i,j)

	def set_BodyTableBarangTr(self, data=None):
		data = self.getDataBarangTr() if data==None else data
		self.viewTransaksi.m_listCtrl4.ClearAll()
		self.set_HeaderTableBarangTr()
		for index,row in enumerate(data):
			if index < self.valueLimitDataTr():
				self.viewTransaksi.m_listCtrl4.InsertItem(index,row[0])
				for i in range(6):
					self.viewTransaksi.m_listCtrl4.SetItem(index,i, str(row[i]))

	def HandleBtnDetail (self, event) :
		self.viewTransaksi.Hide()
		self.viewDetailTransaksi.Show()
		self.set_BodyTableDetailTransaksi()

###########################################################################
## Class BrgMasuk
###########################################################################
	def set_event_Brg_masuk(self):
		self.viewBrgMasuk.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandlBrgMasukBack )
		self.viewBrgMasuk.m_buttonOke.Bind( wx.EVT_BUTTON, self.HandleBrgMasukOke )

	def HandlBrgMasukBack (self, event):
		self.viewBrgMasuk.Hide()
		return self.viewTransaksi.Show()

	def HandleBrgMasukOke(self, event):
		now=datetime.now()
		format_waktu=now.strftime('%Y-%m-%d %H:%M:%S')
		jenis = self.viewBrgMasuk.m_textCtrlJenisBarangM.GetValue()
		merk = self.viewBrgMasuk.m_textCtrlMerkM.GetValue()
		warna = self.viewBrgMasuk.m_textCtrlWarnaM.GetValue()
		ukuran = self.viewBrgMasuk.m_textCtrlUkuranM.GetValue()
		masuk = self.viewBrgMasuk.m_textCtrlJumlahMasuk.GetValue()
		ketMasuk= "masuk"
		if masuk.isnumeric():
			id_barang = self.viewTransaksi.m_listCtrl4.GetItemText(self.stokSelected,0)
			self.model.updateBrgMasuk((id_barang,jenis,merk,warna,ukuran,int(masuk)))
			self.resetFormBrgmasuk()
			self.model.insertBrgMasuk((id_barang,masuk,ketMasuk,format_waktu))
			self.viewBrgMasuk.Hide()
			self.viewTransaksi.LimitData.SetMax(len(self.getDataBarangTr()))
			self.viewTransaksi.Show()
			return self.set_BodyTableBarangTr()

	def resetFormBrgmasuk(self):
		self.viewBrgMasuk.m_textCtrlJenisBarangM.SetValue('')
		self.viewBrgMasuk.m_textCtrlMerkM.SetValue('')
		self.viewBrgMasuk.m_textCtrlWarnaM.SetValue('')
		self.viewBrgMasuk.m_textCtrlUkuranM.SetValue('')
		self.viewBrgMasuk.m_textCtrlJumlahMasuk.SetValue('')
		self.stokSelected = None

###########################################################################
## Class BrgKeluar
###########################################################################
	def set_event_Brg_keluar(self):
		self.viewBrgKeluar.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandlBrgKeluarBack )
		self.viewBrgKeluar.m_buttonOke.Bind( wx.EVT_BUTTON, self.HandleBrgKeluarOke )

	def HandlBrgKeluarBack (self, event):
		self.viewBrgKeluar.Hide()
		return self.viewTransaksi.Show()

	def HandleBrgKeluarOke(self, event):
		now=datetime.now()
		format_waktu=now.strftime('%Y-%m-%d %H:%M:%S')
		jenis = self.viewBrgKeluar.m_textCtrlJenisBarangK.GetValue()
		merk = self.viewBrgKeluar.m_textCtrlMerkK.GetValue()
		warna = self.viewBrgKeluar.m_textCtrlWarnaK.GetValue()
		ukuran = self.viewBrgKeluar.m_textCtrlUkuranK.GetValue()
		keluar = self.viewBrgKeluar.m_textCtrlJumlahKeluar.GetValue()
		ketKeluar= "keluar"
		id_barang = self.viewTransaksi.m_listCtrl4.GetItemText(self.stokSelected,0)
		jumlahStok= self.model.getJumlahStokByID(id_barang)[0]
		if keluar.isnumeric():
			if jumlahStok > int(keluar):
				self.model.updateBrgKeluar((id_barang,jenis,merk,warna,ukuran,int(keluar)))
				self.resetFormBrgKeluar()
				self.model.insertBrgKeluar((id_barang,keluar,ketKeluar,format_waktu))
				self.viewBrgKeluar.Hide()
				self.viewTransaksi.LimitData.SetMax(len(self.getDataBarangTr()))
				self.viewTransaksi.Show()
				return self.set_BodyTableBarangTr()
			else :
				wx.MessageDialog(None, 'MAAF, STOK TIDAK MENCUKUPI', 'INFORMATION', style=wx.OK | wx.ICON_INFORMATION).ShowModal()


	def resetFormBrgKeluar(self):
		self.viewBrgKeluar.m_textCtrlJenisBarangK.SetValue('')
		self.viewBrgKeluar.m_textCtrlMerkK.SetValue('')
		self.viewBrgKeluar.m_textCtrlWarnaK.SetValue('')
		self.viewBrgKeluar.m_textCtrlUkuranK.SetValue('')
		self.viewBrgKeluar.m_textCtrlJumlahKeluar.SetValue('')
		self.stokSelected = None

	
###########################################################################
## DetailTransaksi
###########################################################################
	def set_event_detail_transaksi(self):
		self.viewDetailTransaksi.m_listCtrl6.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItemDt )
		self.viewDetailTransaksi.LimitDataDt.Bind( wx.EVT_SPINCTRL, self.limitDataDtt )
		self.viewDetailTransaksi.LimitDataDt.Bind( wx.EVT_TEXT, self.limitDataDtt )
		self.viewDetailTransaksi.LimitDataDt.Bind( wx.EVT_TEXT_ENTER, self.limitDataDtt )
		self.viewDetailTransaksi.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackDt )
		self.viewDetailTransaksi.m_searchCtrlDt.Bind( wx.EVT_TEXT, self.onSearchDt )

	def onSearchDt(self,event):
		keyword = self.viewDetailTransaksi.m_searchCtrlDt.GetValue()
		if keyword != '':
			result = self.model.searchByKeywordTr(keyword)
			return self.set_BodyTableDetailTransaksi(result)
		return self.set_BodyTableDetailTransaksi()
		
	def HandleSelectItemDt(self,event):
		self.TransaksiSelected = event.GetIndex()

	def HandleBtnBackDt(self, event) :
		self.viewDetailTransaksi.Hide()
		return self.viewTransaksi.Show()

	def valueLimitDataDt(self):
		return self.viewDetailTransaksi.LimitDataDt.GetValue()

	def limitDataDtt(self,event):
		return self.set_BodyTableDetailTransaksi()

	def getDataTransaksi(self):
		return self.model.getDataTransaksi()

	def set_HeaderTableDetailTransaksi(self):
		table = ['id_transaksi','id_barang', 'jumlah', 'masuk/keluar','tanggal']
		for i,j in enumerate(table):
			self.viewDetailTransaksi.m_listCtrl6.InsertColumn(i,j)

	def set_BodyTableDetailTransaksi(self, data=None):
		data = self.getDataTransaksi() if data==None else data
		self.viewDetailTransaksi.m_listCtrl6.ClearAll()
		self.set_HeaderTableDetailTransaksi()
		for index,row in enumerate(data):
			if index < self.valueLimitDataDt():
				self.viewDetailTransaksi.m_listCtrl6.InsertItem(index,row[0])
				for i in range(5):
					self.viewDetailTransaksi.m_listCtrl6.SetItem(index,i, str(row[i]))



###########################################################################
## Akun Setting
###########################################################################
	def set_event_admin(self):
		self.viewAdmin.BtnEditData.Bind( wx.EVT_BUTTON, self.HandleBtnEditAdm )
		self.viewAdmin.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackAdm )
		self.viewAdmin.m_listCtrl5.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectAdmin )

	def HandleSelectAdmin(self,event):
		self.adminSelected = event.GetIndex()

	def HandleBtnEditAdm(self,event):
		self.dialog = Views.UbahUser(None)
		self.dialog.btnSimpan.Bind( wx.EVT_BUTTON, self.onbtnSimpan )
		id_admin = self.viewAdmin.m_listCtrl5.GetItemText(self.adminSelected,0)
		data = self.model.getAdminByID(id_admin)
		self.dialog.username.SetValue(data[2])
		self.dialog.password.SetValue(data[3])
		self.dialog.ShowModal()

	def onbtnSimpan(self,event):
		if self.adminSelected != None:
			usr = self.dialog.username.GetValue()
			passwd = self.dialog.password.GetValue()
			id_admin = self.viewAdmin.m_listCtrl5.GetItemText(self.adminSelected,0)
			if (usr != '') & (passwd != ''):
				self.model.updateAdmin(id_admin,usr,passwd)
			self.set_BodyTableAdmin()
			self.dialog.Destroy()

	def HandleBtnBackAdm(self,event):
		self.viewAdmin.Hide()
		self.viewBeranda.Show()

	def getDataAdmin(self):
		return self.model.getDataAdmin()

	def set_HeaderTableAdmin(self):
		table = ['ID','Nama', 'Username', 'Password']
		for i,j in enumerate(table):
			self.viewAdmin.m_listCtrl5.InsertColumn(i,j)

	def set_BodyTableAdmin(self, data=None):
		data = self.getDataAdmin() if data==None else data
		self.viewAdmin.m_listCtrl5.ClearAll()
		self.set_HeaderTableAdmin()
		for index,row in enumerate(data):
			self.viewAdmin.m_listCtrl5.InsertItem(index,row[0])
			for i in range(4):
				self.viewAdmin.m_listCtrl5.SetItem(index,i, str(row[i]))
	
	


###########################################################################
## Main Program
###########################################################################
	def main(self):
		self.viewLogin.Show()