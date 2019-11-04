# from ...ui.widgets.folder_viewer_panel import folder_viewer_panel
# import wx, os


# class Plugin(wx.Panel):
    # title = 'Folder viewer'

    # def __init__(self, parent):
        # wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(255, 0),
                          # style=wx.TAB_TRAVERSAL)

        # bSizer1 = wx.BoxSizer(wx.VERTICAL)

        # path = "/Volumes/Macintosh/curioData/screening/20181022_wt_mad1/FLUO_80_1_FluoAnalysis/mad1/croppedImgs"
        # # TODO this getDir and wx.DirDialog will both crash
        # # tmp_dir = IPy.getdir("Choose a directory", "", "")
        # list_file = os.listdir(path)

        # self.curvepan = folder_viewer_panel(self, [path + os.sep + f for f in list_file])
        # bSizer1.Add(self.curvepan, 0, wx.ALL | wx.EXPAND, 0)

        # bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        # self.btn_load = wx.Button(self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.Size(-1, -1), wx.BU_EXACTFIT)
        # self.btn_load.SetMaxSize(wx.Size(-1, 40))

        # bSizer2.Add(self.btn_load, 0, wx.ALIGN_CENTER | wx.ALL, 0)


        # bSizer2.AddStretchSpacer(prop=1)

        # self.txt = wx.TextCtrl(self, -1, size=(140, -1))

        # bSizer2.Add(self.txt)


        # bSizer1.Add(bSizer2, 0, wx.EXPAND | wx.ALL, 5)

        # self.SetSizer(bSizer1)
        # self.Layout()

        # # self.curvepan.Bind(None, self.handle)
        # self.btn_load.Bind(wx.EVT_BUTTON, self.on_load)

    # # def handle(self, event):
    # #     ips = IPy.get_ips()
    # #     if ips is None: return
    # #     lut = CurvePanel.lookup(self.curvepan.pts)
    # #     lut = np.vstack((lut, lut, lut)).T
    # #     ips.lut = lut
    # #     ips.update = 'pix'

    # def on_load(self, event):
        # print(self.txt.GetLineText(0))
