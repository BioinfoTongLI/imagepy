from imagepy import IPy
from imagepy.core.engine import Free
import pandas as pd
from imagepy.IPy import curapp
import skimage.external.tifffile as tifffile
import wx
import os


def generate_empty_annotation(n_cell, n_t):
    idx = []
    for i in range(n_cell):
        for j in range(n_t):
            idx.append((i, j))
    pd_idx = pd.MultiIndex.from_tuples(idx, names=['Cell', 'Timepoint'])
    return pd.DataFrame(index=pd_idx, columns=["Class"])


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(350, 300))

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        dialog = wx.DirDialog(parent, "Open")
        if dialog.ShowModal() == wx.ID_OK:
                tmp_dir=dialog.GetPath()
        print(123)
        files = os.listdir(tmp_dir)
        lst = wx.ListBox(panel, size=(100, -1), choices=files, style=wx.LB_SINGLE)

        box.Add(lst, 0, wx.EXPAND)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)
        self.Show(True)

    def onListBox(self, event):
        img = tifffile.imread(event.GetEventObject().GetStringSelection())
        IPy.show_img(img, event.GetEventObject().GetStringSelection())
        print("Current selection:"+event.GetEventObject().GetStringSelection()+"\n")


class Plugin(Free):
    title = "Manual Annotation"

    def run(self, para=None):
        Mywin(curapp, 'Current selection')
        data = generate_empty_annotation(3, 5)
        IPy.show_table(data, 'Annotations[%s,%s]' % data.shape)
