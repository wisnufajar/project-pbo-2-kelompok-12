from Controller import *

class App(wx.App):
	"""docstring for App"""
	def OnInit(self):
		self.frame = Gudang()
		self.frame.main()
		return True


Run = App()
Run.MainLoop()
