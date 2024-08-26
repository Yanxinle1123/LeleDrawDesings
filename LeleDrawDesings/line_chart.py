import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


class LineChart:
    def __init__(self, squares=None, input_values=None, save_name=None, x_ticks=None, x_ticks_fontsize=None,
                 y_ticks=None,
                 y_ticks_fontsize=None, skin=None, style=None, line_width=None, label_size=None, set_title=None,
                 set_title_fontsize=None, set_x_label=None, set_x_label_fontsize=None, set_y_label=None,
                 set_y_label_fontsize=None, drop_color=None, line_color=None, figsize=None):
        self._line_width = line_width
        self._label_size = label_size
        self._save_name = save_name
        self._squares = squares
        self._input_values = input_values
        self._x_ticks = x_ticks
        self._x_ticks_fontsize = x_ticks_fontsize
        self._y_ticks = y_ticks
        self._y_ticks_fontsize = y_ticks_fontsize
        self._set_title = set_title
        self._set_title_fontsize = set_title_fontsize
        self._set_x_label = set_x_label
        self._set_x_label_fontsize = set_x_label_fontsize
        self._set_y_label = set_y_label
        self._set_y_label_fontsize = set_y_label_fontsize
        self._skin = skin
        self._style = style
        self._drop_color = drop_color
        self._line_color = line_color
        self._figsize = figsize

        if self._squares is None:
            self._squares = [1, 4, 9, 16, 25]
        if self._skin is None:
            self._skin = 'seaborn-v0_8'
        if self._style is None:
            self._style = 'straight'
        if self._x_ticks_fontsize is None:
            self._x_ticks_fontsize = 14
        if self._y_ticks_fontsize is None:
            self._y_ticks_fontsize = 14
        if self._line_width is None:
            self._line_width = 3
        if self._label_size is None:
            self._label_size = 10
        if self._input_values is None:
            self._input_values = [0, 1, 2, 3, 4]
        if self._drop_color is None:
            self._drop_color = 'red'
        if self._figsize is None:
            self._figsize = (10, 6)

        self.draw()

    def draw(self):
        input_values = self._input_values
        squares = self._squares
        line_color = self._line_color
        drop_color = self._drop_color
        if self._style == 'straight':

            plt.style.use(self._skin)

            _, ax = plt.subplots(figsize=self._figsize)
            if input_values is None:
                ax.plot(squares, linewidth=self._line_width, color=line_color)
            else:
                ax.plot(input_values, squares, linewidth=self._line_width, color=line_color)

            # 绘制散点图
            ax.scatter(input_values, squares, color=drop_color, marker='o', zorder=3)

            ax.set_title(self._set_title, fontsize=self._set_title_fontsize)
            ax.set_xlabel(self._set_x_label, fontsize=self._set_x_label_fontsize)
            ax.set_ylabel(self._set_y_label, fontsize=self._set_y_label_fontsize)

            ax.tick_params(labelsize=self._label_size)

            if self._x_ticks is not None:
                plt.xticks(self._input_values, self._x_ticks)
                plt.tick_params(axis='x', labelsize=self._x_ticks_fontsize)
            if self._y_ticks is not None:
                plt.xticks(self._input_values, self._y_ticks)
                plt.tick_params(axis='y', labelsize=self._y_ticks_fontsize)
            if self._save_name is not None:
                plt.savefig(self._save_name)

            plt.show()
        elif self._style == 'curved':
            # 三次样条插值
            cs = CubicSpline(input_values, squares)

            # 生成插值数据点
            x = np.linspace(min(input_values), max(input_values), num=100)
            y = cs(x)

            # 设置图的样式
            plt.style.use(self._skin)

            _, ax = plt.subplots(figsize=self._figsize)

            # 绘制折线图
            ax.plot(x, y, linewidth=self._line_width, color=line_color)

            # 绘制散点图
            ax.scatter(input_values, squares, color=drop_color, marker='o', zorder=3)

            # 设置图题并给坐标轴加上标签
            ax.set_title(self._set_title, fontsize=self._set_title_fontsize)
            ax.set_xlabel(self._set_x_label, fontsize=self._set_x_label_fontsize)
            ax.set_ylabel(self._set_y_label, fontsize=self._set_y_label_fontsize)

            # 设置刻度标记的样式
            ax.tick_params(labelsize=self._label_size)

            if self._x_ticks is not None:
                plt.xticks(self._input_values, self._x_ticks)
                plt.tick_params(axis='x', labelsize=self._x_ticks_fontsize)
            if self._y_ticks is not None:
                plt.xticks(self._input_values, self._y_ticks)
                plt.tick_params(axis='y', labelsize=self._y_ticks_fontsize)
            if self._save_name is not None:
                plt.savefig(self._save_name)

            plt.show()
