from LeleDrawDesigns.dice_analysis import dice_analysis
from LeleDrawDesigns.histogram import Histogram
from LeleDrawDesigns.line_chart import LineChart
from LeleDrawDesigns.obtain_all_skin import obtain_all_skin

"""
演示如何使用LeleDrawDesigns库
用一个简单的骰子事例来生成数据
"""

poss_results, frequencies = dice_analysis()

input_values = []
for i in range(len(frequencies)):
    input_values.append(i + 1)

xlabel = 'Result'
ylabel = 'Frequency of Result'
x_labels = ["one", "two", "three", "four", "five", "six"]

Histogram(poss_results, frequencies, x_ticks=x_labels, x_ticks_fontsize=20, y_ticks_fontsize=50,
          skin='Solarize_Light2', title='Results of Rolling One D6 1,000 Times(Histogram)',
          title_fontsize=20, x_label=xlabel, y_label=ylabel, x_label_fontsize=20, y_label_fontsize=20,
          color='green', edgecolor='black', figsize=(10, 7),
          save_name='Results of Rolling One D6 1,000 Times(Histogram)')

LineChart(input_values=input_values, squares=frequencies, x_ticks=x_labels, style='straight',
          line_color='green', skin='Solarize_Light2',
          set_title='Results of Rolling One D6 1,000 Times(StraightLineChart)',
          set_title_fontsize=20, set_x_label=xlabel, set_x_label_fontsize=20, set_y_label=ylabel,
          set_y_label_fontsize=20, line_width=3, figsize=(10, 7), x_ticks_fontsize=20,
          save_name='Results of Rolling One D6 1,000 Times(StraightLineChart)')

LineChart(input_values=input_values, squares=frequencies, x_ticks=x_labels, style='curved',
          line_color='green', skin='Solarize_Light2',
          set_title='Results of Rolling One D6 1,000 Times(CurvedLineChart)', set_title_fontsize=20,
          set_x_label=xlabel, set_x_label_fontsize=20, set_y_label=ylabel, set_y_label_fontsize=20,
          line_width=3, figsize=(10, 7), x_ticks_fontsize=20,
          save_name='Results of Rolling One D6 1,000 Times(CurvedLineChart)')

obtain_all_skin()
