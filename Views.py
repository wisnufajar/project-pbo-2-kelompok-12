# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class loginFrame
###########################################################################

class loginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"- Selamat datang Di aplikasi Gudang penyimpanan barang -", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		bSizer1.Add( self.m_staticText32, 0, wx.ALL, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"LOGIN" ), wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.text_email = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), 0|wx.BORDER_NONE )
		self.text_email.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_email, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		sbSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.text_password = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,50 ), wx.TE_PASSWORD|wx.BORDER_NONE )
		self.text_password.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		sbSizer3.Add( self.text_password, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText321 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )

		sbSizer3.Add( self.m_staticText321, 0, wx.ALL, 5 )

		self.btn_login = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btn_login.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.btn_login.SetBackgroundColour( wx.Colour( 10, 209, 85 ) )

		sbSizer3.Add( self.btn_login, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_login_onclick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_login_onclick( self, event ):
		event.Skip()


###########################################################################
## Class beranda
###########################################################################

class beranda ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 550,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"BERANDA" ), wx.VERTICAL )

		self.btnCekStok = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"TAMPILKAN STOK DALAM GUDANG", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btnCekStok.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.btnCekStok.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btnCekStok.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		sbSizer4.Add( self.btnCekStok, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnTransaksi = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"TRANSAKSI", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btnTransaksi.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.btnTransaksi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btnTransaksi.SetBackgroundColour( wx.Colour( 142, 219, 179 ) )

		sbSizer4.Add( self.btnTransaksi, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnAkunSetting = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"AKUN SETTING", wx.DefaultPosition, wx.Size( -1,70 ), 0 )
		self.btnAkunSetting.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.btnAkunSetting.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.btnAkunSetting.SetBackgroundColour( wx.Colour( 228, 133, 171 ) )

		sbSizer4.Add( self.btnAkunSetting, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( sbSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnCekStok.Bind( wx.EVT_BUTTON, self.HandleBtnTampilStok )
		self.btnTransaksi.Bind( wx.EVT_BUTTON, self.HandleBtnTransaksi )
		self.btnAkunSetting.Bind( wx.EVT_BUTTON, self.HandleBtnAkunSeting )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandleBtnTampilStok( self, event ):
		event.Skip()

	def HandleBtnTransaksi( self, event ):
		event.Skip()

	def HandleBtnAkunSeting( self, event ):
		event.Skip()


###########################################################################
## Class cekStok
###########################################################################

class cekStok ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"STOK DALAM GUDANG", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer17.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.m_listCtrl4 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.m_listCtrl4.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_listCtrl4.SetMinSize( wx.Size( 750,315 ) )

		fgSizer2.Add( self.m_listCtrl4, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer2, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.LimitData = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 10, 10 )
		self.LimitData.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.LimitData.SetMaxSize( wx.Size( 70,-1 ) )

		bSizer20.Add( self.LimitData, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnBack = wx.Button( self.m_panel1, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnBack.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer20.Add( self.BtnBack, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnHapusData = wx.Button( self.m_panel1, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnHapusData.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnHapusData.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer20.Add( self.BtnHapusData, 1, wx.ALL|wx.EXPAND, 5 )

		self.BtnEditData = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnEditData.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnEditData.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )

		bSizer20.Add( self.BtnEditData, 1, wx.ALL|wx.EXPAND, 5 )

		self.BtnTambahData = wx.Button( self.m_panel1, wx.ID_ANY, u"Tambah Data Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnTambahData.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnTambahData.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer20.Add( self.BtnTambahData, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer17 )
		self.m_panel1.Layout()
		bSizer17.Fit( self.m_panel1 )
		bSizer16.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.onSearch )
		self.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItem )
		self.LimitData.Bind( wx.EVT_SPINCTRL, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT_ENTER, self.limitData )
		self.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBack )
		self.BtnHapusData.Bind( wx.EVT_BUTTON, self.HandleBtnHapus )
		self.BtnEditData.Bind( wx.EVT_BUTTON, self.HandleBtnEdit )
		self.BtnTambahData.Bind( wx.EVT_BUTTON, self.HandleBtnTambah )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSearch( self, event ):
		event.Skip()

	def HandleSelectItem( self, event ):
		event.Skip()

	def limitData( self, event ):
		event.Skip()



	def HandleBtnBack( self, event ):
		event.Skip()

	def HandleBtnHapus( self, event ):
		event.Skip()

	def HandleBtnEdit( self, event ):
		event.Skip()

	def HandleBtnTambah( self, event ):
		event.Skip()


###########################################################################
## Class TambahBarang
###########################################################################

class TambahBarang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TAMBAH JENIS BARANG BARU", pos = wx.DefaultPosition, size = wx.Size( 445,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticJenisBarang = wx.StaticText( self, wx.ID_ANY, u"JENIS BARANG :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticJenisBarang.Wrap( -1 )

		self.m_staticJenisBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticJenisBarang, 0, wx.ALL, 5 )

		self.m_textCtrlJenisBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlJenisBarang, 1, wx.ALL, 5 )

		self.m_staticTextMerk = wx.StaticText( self, wx.ID_ANY, u"MERK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMerk.Wrap( -1 )

		self.m_staticTextMerk.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextMerk, 0, wx.ALL, 5 )

		self.m_textCtrlMerk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlMerk, 0, wx.ALL, 5 )

		self.m_staticTextWarna = wx.StaticText( self, wx.ID_ANY, u"WARNA :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWarna.Wrap( -1 )

		self.m_staticTextWarna.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextWarna, 0, wx.ALL, 5 )

		self.m_textCtrlWarna = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlWarna, 0, wx.ALL, 5 )

		self.m_staticTextUkuran = wx.StaticText( self, wx.ID_ANY, u"UKURAN :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran.Wrap( -1 )

		self.m_staticTextUkuran.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextUkuran, 0, wx.ALL, 5 )

		self.m_textCtrlUkuran = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlUkuran, 0, wx.ALL, 5 )

		self.m_staticTextStok = wx.StaticText( self, wx.ID_ANY, u"JUMLAH STOK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStok.Wrap( -1 )

		self.m_staticTextStok.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextStok, 0, wx.ALL, 5 )

		self.m_textCtrlJumlahStok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlJumlahStok, 1, wx.ALL, 5 )

		self.m_buttonBack = wx.Button( self, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBack.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		gSizer8.Add( self.m_buttonBack, 0, wx.ALL, 5 )

		self.m_buttonTambah = wx.Button( self, wx.ID_ANY, u"TAMBAH", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonTambah.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonTambah.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		gSizer8.Add( self.m_buttonTambah, 1, wx.ALL, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandleTambahBarangBack )
		self.m_buttonTambah.Bind( wx.EVT_BUTTON, self.HandleTambahBarang )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandleTambahBarangBack( self, event ):
		event.Skip()

	def HandleTambahBarang( self, event ):
		event.Skip()


###########################################################################
## Class transaksi
###########################################################################

class transaksi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"TRANSAKSI", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_searchCtrl1 = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer17.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.m_listCtrl4 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.m_listCtrl4.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_listCtrl4.SetMinSize( wx.Size( 750,315 ) )

		fgSizer2.Add( self.m_listCtrl4, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer2, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.LimitData = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 10, 10 )
		self.LimitData.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.LimitData.SetMaxSize( wx.Size( 70,-1 ) )

		bSizer20.Add( self.LimitData, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnBack = wx.Button( self.m_panel1, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnBack.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer20.Add( self.BtnBack, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnBrgKeluar = wx.Button( self.m_panel1, wx.ID_ANY, u"Barang Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnBrgKeluar.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnBrgKeluar.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer20.Add( self.BtnBrgKeluar, 1, wx.ALL|wx.EXPAND, 5 )

		self.BtnDetailTransaksi = wx.Button( self.m_panel1, wx.ID_ANY, u"Detail Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnDetailTransaksi.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnDetailTransaksi.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )

		bSizer20.Add( self.BtnDetailTransaksi, 1, wx.ALL|wx.EXPAND, 5 )

		self.BtnTambahMasuk = wx.Button( self.m_panel1, wx.ID_ANY, u"Barang masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnTambahMasuk.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnTambahMasuk.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer20.Add( self.BtnTambahMasuk, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer17 )
		self.m_panel1.Layout()
		bSizer17.Fit( self.m_panel1 )
		bSizer16.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.onSearchTr )
		self.m_listCtrl4.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItemTr )
		self.LimitData.Bind( wx.EVT_SPINCTRL, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT_ENTER, self.limitData )
		self.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackTr )
		self.BtnBrgKeluar.Bind( wx.EVT_BUTTON, self.HandleBtnBrgKeluar )
		self.BtnDetailTransaksi.Bind( wx.EVT_BUTTON, self.HandleBtnDetail )
		self.BtnTambahMasuk.Bind( wx.EVT_BUTTON, self.HandleBtnBrgMasuk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onSearchTr( self, event ):
		event.Skip()

	def HandleSelectItemTr( self, event ):
		event.Skip()

	def limitData( self, event ):
		event.Skip()



	def HandleBtnBackTr( self, event ):
		event.Skip()

	def HandleBtnBrgKeluar( self, event ):
		event.Skip()

	def HandleBtnDetail( self, event ):
		event.Skip()

	def HandleBtnBrgMasuk( self, event ):
		event.Skip()


###########################################################################
## Class DetailTransaksi
###########################################################################

class DetailTransaksi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DETAIL TRANSAKSI", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.m_listCtrl6 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.m_listCtrl6.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_listCtrl6.SetMinSize( wx.Size( 750,355 ) )

		fgSizer2.Add( self.m_listCtrl6, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer2, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.LimitDataDt = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 10, 10 )
		self.LimitDataDt.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.LimitDataDt.SetMaxSize( wx.Size( 70,-1 ) )

		bSizer20.Add( self.LimitDataDt, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnBack = wx.Button( self.m_panel1, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnBack.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer20.Add( self.BtnBack, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_searchCtrlDt = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrlDt.ShowSearchButton( True )
		self.m_searchCtrlDt.ShowCancelButton( False )
		bSizer20.Add( self.m_searchCtrlDt, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer17 )
		self.m_panel1.Layout()
		bSizer17.Fit( self.m_panel1 )
		bSizer16.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_listCtrl6.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectItemDt )
		self.LimitDataDt.Bind( wx.EVT_SPINCTRL, self.limitDataDt )
		self.LimitDataDt.Bind( wx.EVT_TEXT, self.limitDataDt )
		self.LimitDataDt.Bind( wx.EVT_TEXT_ENTER, self.limitDataDt )
		self.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackDt )
		self.m_searchCtrlDt.Bind( wx.EVT_TEXT, self.onSearchDt )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandleSelectItemDt( self, event ):
		event.Skip()

	def limitDataDt( self, event ):
		event.Skip()



	def HandleBtnBackDt( self, event ):
		event.Skip()

	def onSearchDt( self, event ):
		event.Skip()


###########################################################################
## Class EditBarang
###########################################################################

class EditBarang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"EDIT BARANG", pos = wx.DefaultPosition, size = wx.Size( 445,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticJenisBarang = wx.StaticText( self, wx.ID_ANY, u"JENIS BARANG :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticJenisBarang.Wrap( -1 )

		self.m_staticJenisBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticJenisBarang, 0, wx.ALL, 5 )

		self.m_textCtrlJenisBarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlJenisBarang, 1, wx.ALL, 5 )

		self.m_staticTextMerk = wx.StaticText( self, wx.ID_ANY, u"MERK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMerk.Wrap( -1 )

		self.m_staticTextMerk.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextMerk, 0, wx.ALL, 5 )

		self.m_textCtrlMerk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlMerk, 0, wx.ALL, 5 )

		self.m_staticTextWarna = wx.StaticText( self, wx.ID_ANY, u"WARNA :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWarna.Wrap( -1 )

		self.m_staticTextWarna.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextWarna, 0, wx.ALL, 5 )

		self.m_textCtrlWarna = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlWarna, 0, wx.ALL, 5 )

		self.m_staticTextUkuran = wx.StaticText( self, wx.ID_ANY, u"UKURAN :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran.Wrap( -1 )

		self.m_staticTextUkuran.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextUkuran, 0, wx.ALL, 5 )

		self.m_textCtrlUkuran = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlUkuran, 0, wx.ALL, 5 )

		self.m_staticTextStok = wx.StaticText( self, wx.ID_ANY, u"JUMLAH STOK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStok.Wrap( -1 )

		self.m_staticTextStok.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextStok, 0, wx.ALL, 5 )

		self.m_textCtrlJumlahStok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlJumlahStok, 1, wx.ALL, 5 )

		self.m_buttonBack = wx.Button( self, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBack.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		gSizer8.Add( self.m_buttonBack, 0, wx.ALL, 5 )

		self.m_buttonSimpan = wx.Button( self, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonSimpan.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonSimpan.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		gSizer8.Add( self.m_buttonSimpan, 1, wx.ALL, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandleEditBarangBack )
		self.m_buttonSimpan.Bind( wx.EVT_BUTTON, self.HandleSimpanBarang )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandleEditBarangBack( self, event ):
		event.Skip()

	def HandleSimpanBarang( self, event ):
		event.Skip()


###########################################################################
## Class DataAdmin
###########################################################################

class DataAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DataAdmin", pos = wx.DefaultPosition, size = wx.Size( 596,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 1, 5 )
		fgSizer2.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.m_listCtrl5 = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.m_listCtrl5.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.m_listCtrl5.SetMinSize( wx.Size( 750,350 ) )

		fgSizer2.Add( self.m_listCtrl5, 0, wx.ALL, 5 )


		bSizer17.Add( fgSizer2, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.LimitData = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, 0, 10, 5 )
		self.LimitData.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.LimitData.SetMaxSize( wx.Size( 70,-1 ) )

		bSizer20.Add( self.LimitData, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnBack = wx.Button( self.m_panel1, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnBack.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer20.Add( self.BtnBack, 0, wx.ALL|wx.EXPAND, 5 )

		self.BtnEditData = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BtnEditData.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.BtnEditData.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )

		bSizer20.Add( self.BtnEditData, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer17 )
		self.m_panel1.Layout()
		bSizer17.Fit( self.m_panel1 )
		bSizer16.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_listCtrl5.Bind( wx.EVT_LIST_ITEM_SELECTED, self.HandleSelectAdmin )
		self.LimitData.Bind( wx.EVT_SPINCTRL, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT, self.limitData )
		self.LimitData.Bind( wx.EVT_TEXT_ENTER, self.limitData )
		self.BtnBack.Bind( wx.EVT_BUTTON, self.HandleBtnBackAdm )
		self.BtnEditData.Bind( wx.EVT_BUTTON, self.HandleBtnEditAdm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandleSelectAdmin( self, event ):
		event.Skip()

	def limitData( self, event ):
		event.Skip()



	def HandleBtnBackAdm( self, event ):
		event.Skip()

	def HandleBtnEditAdm( self, event ):
		event.Skip()


###########################################################################
## Class UbahUser
###########################################################################

class UbahUser ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ubah Data Admin", pos = wx.DefaultPosition, size = wx.Size( 176,215 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		bSizer17.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.username, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		bSizer17.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.password, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSimpan.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.btnSimpan.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		bSizer17.Add( self.btnSimpan, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpan.Bind( wx.EVT_BUTTON, self.onbtnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onbtnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class BrgMasuk
###########################################################################

class BrgMasuk ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BARANG MASUK", pos = wx.DefaultPosition, size = wx.Size( 445,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticJenisBarang = wx.StaticText( self, wx.ID_ANY, u"JENIS BARANG :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticJenisBarang.Wrap( -1 )

		self.m_staticJenisBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticJenisBarang, 0, wx.ALL, 5 )

		self.m_textCtrlJenisBarangM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlJenisBarangM, 1, wx.ALL, 5 )

		self.m_staticTextMerk = wx.StaticText( self, wx.ID_ANY, u"MERK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMerk.Wrap( -1 )

		self.m_staticTextMerk.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextMerk, 0, wx.ALL, 5 )

		self.m_textCtrlMerkM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlMerkM, 0, wx.ALL, 5 )

		self.m_staticTextWarna = wx.StaticText( self, wx.ID_ANY, u"WARNA :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWarna.Wrap( -1 )

		self.m_staticTextWarna.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextWarna, 0, wx.ALL, 5 )

		self.m_textCtrlWarnaM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlWarnaM, 0, wx.ALL, 5 )

		self.m_staticTextUkuran = wx.StaticText( self, wx.ID_ANY, u"UKURAN :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran.Wrap( -1 )

		self.m_staticTextUkuran.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextUkuran, 0, wx.ALL, 5 )

		self.m_textCtrlUkuranM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlUkuranM, 0, wx.ALL, 5 )

		self.m_staticTextStok = wx.StaticText( self, wx.ID_ANY, u"JUMLAH MASUK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStok.Wrap( -1 )

		self.m_staticTextStok.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextStok, 0, wx.ALL, 5 )

		self.m_textCtrlJumlahMasuk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlJumlahMasuk, 1, wx.ALL, 5 )

		self.m_buttonBack = wx.Button( self, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBack.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		gSizer8.Add( self.m_buttonBack, 0, wx.ALL, 5 )

		self.m_buttonOke = wx.Button( self, wx.ID_ANY, u"OKE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonOke.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonOke.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		gSizer8.Add( self.m_buttonOke, 1, wx.ALL, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandlBrgMasukBack )
		self.m_buttonOke.Bind( wx.EVT_BUTTON, self.HandleBrgMasukOke )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandlBrgMasukBack( self, event ):
		event.Skip()

	def HandleBrgMasukOke( self, event ):
		event.Skip()


###########################################################################
## Class BrgKeluar
###########################################################################

class BrgKeluar ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BARANG KELUAR", pos = wx.DefaultPosition, size = wx.Size( 445,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticJenisBarang = wx.StaticText( self, wx.ID_ANY, u"JENIS BARANG :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticJenisBarang.Wrap( -1 )

		self.m_staticJenisBarang.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticJenisBarang, 0, wx.ALL, 5 )

		self.m_textCtrlJenisBarangK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlJenisBarangK, 1, wx.ALL, 5 )

		self.m_staticTextMerk = wx.StaticText( self, wx.ID_ANY, u"MERK :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextMerk.Wrap( -1 )

		self.m_staticTextMerk.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextMerk, 0, wx.ALL, 5 )

		self.m_textCtrlMerkK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlMerkK, 0, wx.ALL, 5 )

		self.m_staticTextWarna = wx.StaticText( self, wx.ID_ANY, u"WARNA :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextWarna.Wrap( -1 )

		self.m_staticTextWarna.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextWarna, 0, wx.ALL, 5 )

		self.m_textCtrlWarnaK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlWarnaK, 0, wx.ALL, 5 )

		self.m_staticTextUkuran = wx.StaticText( self, wx.ID_ANY, u"UKURAN :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextUkuran.Wrap( -1 )

		self.m_staticTextUkuran.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextUkuran, 0, wx.ALL, 5 )

		self.m_textCtrlUkuranK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		gSizer8.Add( self.m_textCtrlUkuranK, 0, wx.ALL, 5 )

		self.m_staticTextStok = wx.StaticText( self, wx.ID_ANY, u"JUMLAH KELUAR :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextStok.Wrap( -1 )

		self.m_staticTextStok.SetFont( wx.Font( 9, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )

		gSizer8.Add( self.m_staticTextStok, 0, wx.ALL, 5 )

		self.m_textCtrlJumlahKeluar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrlJumlahKeluar, 1, wx.ALL, 5 )

		self.m_buttonBack = wx.Button( self, wx.ID_ANY, u"BACK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonBack.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonBack.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		gSizer8.Add( self.m_buttonBack, 0, wx.ALL, 5 )

		self.m_buttonOke = wx.Button( self, wx.ID_ANY, u"OKE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonOke.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Cooper Black" ) )
		self.m_buttonOke.SetBackgroundColour( wx.Colour( 0, 255, 128 ) )

		gSizer8.Add( self.m_buttonOke, 1, wx.ALL, 5 )


		self.SetSizer( gSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_buttonBack.Bind( wx.EVT_BUTTON, self.HandlBrgKeluarBack )
		self.m_buttonOke.Bind( wx.EVT_BUTTON, self.HandleBrgKeluarOke )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def HandlBrgKeluarBack( self, event ):
		event.Skip()

	def HandleBrgKeluarOke( self, event ):
		event.Skip()


