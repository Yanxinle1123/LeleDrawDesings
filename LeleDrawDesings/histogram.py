import matplotlib.pyplot as plt

from LeleDrawDesigns.dice_analysis import dice_analysis

poss_results, list_frequencies = dice_analysis()


class Histogram:
    def __init__(self, input_values=None, frequencies=None, label_size=None, figsize=None, skin=None, color=None,
                 edgecolor=None, title=None, title_fontsize=None, x_label=None, x_label_fontsize=None, y_label=None,
                 y_label_fontsize=None, x_ticks=None, x_ticks_fontsize=None, y_ticks=None, y_ticks_fontsize=None,
                 save_name=None):
        self._input_values = input_values
        self._frequencies = frequencies
        self._label_size = label_size
        self._skin = skin
        self._color = color
        self._edgecolor = edgecolor
        self._title = title
        self._title_fontsize = title_fontsize
        self._x_label = x_label
        self._x_label_fontsize = x_label_fontsize
        self._y_label = y_label
        self._y_label_fontsize = y_label_fontsize
        self._x_ticks = x_ticks
        self._figsize = figsize
        self._x_ticks_fontsize = x_ticks_fontsize
        self._y_ticks = y_ticks
        self._y_ticks_fontsize = y_ticks_fontsize
        self._save_name = save_name

        if self._input_values is None:
            self._input_values = poss_results
        if self._frequencies is None:
            self._frequencies = list_frequencies
        if self._skin is None:
            self._skin = 'seaborn-v0_8'
        if self._color is None:
            self._color = 'blue'
        if self._edgecolor is None:
            self._edgecolor = 'black'
        if self._figsize is None:
            self._figsize = (10, 6)
        if self._x_ticks_fontsize is None:
            self._x_ticks_fontsize = 14
        if self._y_ticks_fontsize is None:
            self._y_ticks_fontsize = 14
        if self._label_size is None:
            self._label_size = 14

        self.draw()

    def draw(self):
        plt.style.use(self._skin)
        plt.figure(figsize=self._figsize)
        plt.bar(self._input_values, self._frequencies, color=self._color, edgecolor=self._edgecolor)
        plt.title(self._title, fontsize=self._title_fontsize)
        plt.xlabel(self._x_label, fontsize=self._x_label_fontsize)
        plt.ylabel(self._y_label, fontsize=self._y_label_fontsize)
        if self._x_ticks is not None:
            plt.xticks(self._input_values, self._x_ticks)
            plt.tick_params(axis='x', labelsize=self._x_ticks_fontsize)
        if self._y_ticks is not None:
            plt.xticks(self._input_values, self._y_ticks)
            plt.tick_params(axis='y', labelsize=self._y_ticks_fontsize)
            plt.tick_params(labelsize=self._label_size)
        if self._save_name is not None:
            plt.savefig(self._save_name)
        plt.show()
