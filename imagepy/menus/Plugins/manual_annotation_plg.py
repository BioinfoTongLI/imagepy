from imagepy import IPy
from imagepy.core.engine import Free
import pandas as pd
from imagepy.IPy import curapp
import os


def generate_empty_annotation(n_cell, n_t):
    idx = []
    for i in range(n_cell):
        for j in range(n_t):
            idx.append((i, j))
    pd_idx = pd.MultiIndex.from_tuples(idx, names=['Cell', 'Timepoint'])
    return pd.DataFrame(index=pd_idx, columns=["Class"])


class Plugin(Free):
    title = "Manual Annotation"

    def run(self, para=None):
        path = "/Volumes/Macintosh/curioData/screening/20181022_wt_mad1/FLUO_80_1_FluoAnalysis/mad1/croppedImgs"
        # TODO this getDir and wx.DirDialog will both crash
        # tmp_dir = IPy.getdir("Choose a directory", "", "")
        list_file = os.listdir(path)
        data = generate_empty_annotation(len(list_file), 70)
        IPy.show_table(data, 'Annotations[%s,%s]' % data.shape)
