# Author: Luan Santos @santluan
# 2023-09-28
# source: https://www.youtube.com/watch?v=5faHSJKlS_g&ab_channel=JieJenn

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation, FFMpegWriter

os.chdir("D:\\Desktop\\DataScience\\Python\\Projects")

def update_animation(year):
    top10_bars = data_pivot[year].sort_values(ascending=False).head(10)

    ax.clear()

    ax.invert_yaxis()

    colors = ['#FFA500', '#FFC100', '#FFD700']

    upper_limit_xaxis = top10_bars.max() + 100_000_000
    ax.set_xlim(0, upper_limit_xaxis)
    ax.set_xlabel('Population (milions)')

    if upper_limit_xaxis > 1_000_000:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, pos: f'{v/1000000:.0f}M'))
    else:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, pos: f'{v/1000:.1f}K'))

    ax.barh(top10_bars.index[:3], top10_bars[:3], color=colors, height=0.7)
    ax.barh(top10_bars.index[3:], top10_bars[3:], color='#314960', height=0.7)

    ax.set_title(f'Top 10 Countries By Population in {year}')

    
data_url = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv'
data = pd.read_csv(data_url, usecols=['Country Name', 'Year', 'Value'])

data_pivot = data.pivot(index='Country Name', columns='Year', values='Value')

fig, ax = plt.subplots(figsize=(10, 6))

years = data_pivot.columns


anim = FuncAnimation(fig, update_animation, frames=years, repeat=True, interval=100)
fig.subplots_adjust(left=0.25)

anim.save('bar_chart_race.gif', fps=10)


# writer = FFMpegWriter(fps=10)

# with writer.saving(fig, 'bar_chart_race.mp4', dpi=300):
#     for year in years:
#         update_animation(year)
#         writer.grab_frame()

# plt.show()
# plt.close(fig)
