import wx, sys
import numpy as np
import skimage.external.tifffile as tifffile
from imagepy import IPy
import os

if sys.version_info[0] == 2: memoryview = np.getbuffer


class folder_viewer_panel(wx.Panel):
    """ HistCanvas: diverid from wx.core.Panel """

    def __init__(self, parent, list_file):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY,
                          pos=wx.DefaultPosition,
                          style=wx.TAB_TRAVERSAL)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)

        lst = wx.ListBox(panel, size=(500, -1), choices=list_file, style=wx.LB_SINGLE)

        box.Add(lst)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)
        self.idx = -1
        self.update = False

    def onListBox(self, event):
        selected_path = event.GetEventObject().GetStringSelection()
        selected_id = selected_path.split(os.sep)[-5:]
        img = tifffile.imread(selected_path)
        IPy.show_img(img, "_".join(selected_id))