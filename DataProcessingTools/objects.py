import numpy as np
from . import levels


class DPObject():
    def __init__(self, *args, **kwargs):
        self.data = np.ndarray((0, 0))
        self.dirs = []
        self.setidx = []

    def plot(self, i, fig):
        pass

    def __add__(self, obj):
        pass

    def level(self):
        pass

    def update_idx(self, index):
        """
        Return `index` if it is valid for the current object
        """
        return max(0, min(index, self.data.shape[0]-1))

    def getindex(self, level):
        """
        Return an index into this object for the requested level.
        """
        level_names = []
        for d in self.dirs:
            q = levels.get_level_path(level, d)
            level_names.append(q)

        unique_names = []
        for l in level_names:
            if l not in unique_names:
                unique_names.append(l)

        idx = np.zeros((len(self.setidx), ), dtype=np.int)
        for i in range(len(self.setidx)):
            idx[i] = unique_names.index(level_names[self.setidx[i]])
        return idx

    def append(self, obj):
        """
        Appends the data of `obj` to this object.
        """
        mx = self.setidx[-1]+1
        for s in obj.setidx:
            self.setidx.append(s+mx)
        for d in obj.dirs:
            self.dirs.append(d)


class DPObjects():
    def __init__(self, objects):
        self.objects = objects

    def __getitem__(self, key):
        return self.objects[key]

    def update_idx(self, index):
        return max(0, min(index, len(self.objects)-1))

    def append(self, item):
        self.objects.append(item)

    def plot(self, i, *args, **kwargs):
        j = self.update_idx(i)
        return self.objects[j].plot(*args, **kwargs)
