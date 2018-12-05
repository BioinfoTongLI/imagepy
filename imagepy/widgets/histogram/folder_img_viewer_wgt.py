from imagepy.ui.tableframe import TablePanel
from imagepy.ui.widgets.manual_annotate_panel import manual_annotate_panel
import wx, os


class Plugin(wx.Panel):
    title = 'Manual annotater'

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition,
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.list_file = ["Your files will be here"]

        self.root = ""

        self.viewerpan = manual_annotate_panel(self, self.list_file)

        bSizer1.Add(self.viewerpan, 0, wx.ALL | wx.EXPAND, 0)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn_load = wx.Button(self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        self.btn_load.SetMaxSize(wx.Size(-1, 40))

        bSizer2.Add(self.btn_load, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.txt = wx.TextCtrl(self, -1, size=(300, -1))

        bSizer2.Add(self.txt, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.tablep = TablePanel(self, wx.Size(200, 500))
        self.tablep.set_tps(self.viewerpan.tps)

        bSizer3.Add(self.tablep, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        # self.btn_save_current = wx.Button(self, wx.ID_ANY, u"Save Current", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        # self.btn_save_current.SetMaxSize(wx.Size(-1, 40))

        self.btn_export_all = wx.Button(self, wx.ID_ANY, u"Export All", wx.DefaultPosition, wx.Size(-1, -1),
                                          wx.BU_EXACTFIT)
        self.btn_export_all.SetMaxSize(wx.Size(-1, 40))

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        # bSizer4.Add(self.btn_save_current, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        bSizer4.Add(self.btn_export_all, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        bSizer1.Add(bSizer2, 0, wx.EXPAND | wx.ALL, 5)
        bSizer1.Add(bSizer3, 0, wx.EXPAND | wx.ALL, 5)
        bSizer1.Add(bSizer4, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.btn_load.Bind(wx.EVT_BUTTON, self.on_load)
        # self.btn_save_current.Bind(wx.EVT_BUTTON, self.on_save_cur)
        self.btn_export_all.Bind(wx.EVT_BUTTON, self.on_export_all)

    def on_load(self, event):
        self.root = self.txt.GetLineText(0)

        file_list = [f for f in os.listdir(self.root) if f.endswith("tif")]
        self.viewerpan.update_list(file_list)

    # def on_save_cur(self, event):
    #     self.viewerpan.save_current()

    def on_export_all(self, event):
        self.viewerpan.export_all(self.root)


