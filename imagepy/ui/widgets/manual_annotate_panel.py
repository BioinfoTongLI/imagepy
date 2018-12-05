import wx, sys, os
import numpy as np
from imagepy import IPy
import skimage.external.tifffile as tifffile

from imagepy.core import TablePlus
from imagepy.core.manager.windowmanager import ImageManager
import pandas as pd


if sys.version_info[0] == 2: memoryview = np.getbuffer


def generate_empty_annotation(n_t):
    pd_idx = pd.Index([i for i in range(n_t)], names=['TimePoint'])
    return pd.DataFrame(np.zeros(len(pd_idx)), index=pd_idx, columns=["Class"], dtype=int)


class manual_annotate_panel(wx.Panel):
    """ HistCanvas: diverid from wx.core.Panel """

    def __init__(self, parent, list_file):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY,
                          pos=wx.DefaultPosition,
                          style=wx.TAB_TRAVERSAL)

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.HORIZONTAL)
        self.parent = parent

        self.current_selection = ""

        self.data = generate_empty_annotation(70)

        self.tps = TablePlus(self.data, 'Annotations[%s,%s]' % self.data.shape)

        self.annotations = {}

        self.lst_box = wx.ListBox(self, size=(-1, 120), choices=list_file, style=wx.LB_SINGLE)

        box.Add(self.lst_box)

        panel.SetSizer(box)
        panel.Fit()

        self.Centre()
        self.Show(True)
        self.update = False
        self.lst_box.Bind(wx.EVT_LISTBOX, self.on_list_box)

    def on_list_box(self, event):
        selected_path = self.parent.root + os.sep + event.GetEventObject().GetStringSelection()
        selected_id = selected_path.split(os.sep)[-5:]
        try:
            img = tifffile.imread(selected_path)
        except Exception:
            return
        cur_ips = ImageManager.get()
        tmp_id = "_".join(selected_id)
        try:
            cur_ips.set_imgs(img)
            cur_ips.update = 'pix'
        except Exception:
            IPy.show_img(img, tmp_id)
        self.current_selection = tmp_id
        if self.current_selection not in self.annotations.keys():
            empty_d = generate_empty_annotation(70)
            self.annotations[self.current_selection] = empty_d
            self.tps.set_data(empty_d)
        else:
            self.tps.set_data(self.annotations[self.current_selection])
        self.tps.update = True

    def update_list(self, list):
        self.lst_box.Set(list)
        self.current_selection = "_".join(list[0].split(os.sep)[-5:])
        self.tps.update = True

    def export_all(self, path):
        pd.concat(self.annotations).to_csv(path + os.sep + "annots.csv")