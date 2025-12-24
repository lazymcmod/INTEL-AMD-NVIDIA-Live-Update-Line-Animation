import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.animation as animation




amd_df = pd.read_csv('amd.csv')
nvidia_df = pd.read_csv('nvidia.csv')
intel_df = pd.read_csv('intel.csv')

amd_df['Date'] = pd.to_datetime(amd_df['Date'])
amd_df['Close'] = amd_df['Close/Last'].str.replace('$', '').astype(float)
amd_df = amd_df.sort_values('Date').reset_index(drop=True)

nvidia_df['Date'] = pd.to_datetime(nvidia_df['Date'])
nvidia_df['Close'] = nvidia_df['Close/Last'].str.replace('$', '').astype(float)
nvidia_df = nvidia_df.sort_values('Date').reset_index(drop=True)


intel_df['Date'] = pd.to_datetime(intel_df['Date'])
intel_df['Close'] = intel_df['Close/Last'].str.replace('$', '').astype(float)
intel_df = intel_df.sort_values('Date').reset_index(drop=True)

fig, ax = plt.subplots(figsize=(12, 6))

all_dates = pd.concat([amd_df['Date'], nvidia_df['Date'], intel_df['Date']])
all_closes = pd.concat([amd_df['Close'], nvidia_df['Close'], intel_df['Close']])

ax.set_xlim(all_dates.min(), all_dates.max())
ax.set_ylim(all_closes.min() - 5, all_closes.max() + 5)
ax.set_xlabel('Date')
ax.set_ylabel('Close Price ($)')
ax.set_title('Stock Price Animation - AMD, NVIDIA, Intel')

line_amd, = ax.plot([], [], lw=2, color='steelblue', label='AMD')
line_nvidia, = ax.plot([], [], lw=2, color='green', label='NVIDIA')
line_intel, = ax.plot([], [], lw=2, color='red', label='Intel')

ax.legend(loc='upper right')

text_amd = ax.text(0, 0, '', fontsize=9, color='steelblue', weight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
text_nvidia = ax.text(0, 0, '', fontsize=9, color='green', weight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
text_intel = ax.text(0, 0, '', fontsize=9, color='red', weight='bold', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))


def animate(frame):
   
    line_amd.set_data(amd_df['Date'][:frame], amd_df['Close'][:frame])
    
    line_nvidia.set_data(nvidia_df['Date'][:frame], nvidia_df['Close'][:frame])
    
    line_intel.set_data(intel_df['Date'][:frame], intel_df['Close'][:frame])
    
    if frame > 0:
        amd_price = amd_df['Close'].iloc[frame-1]
        amd_date = amd_df['Date'].iloc[frame-1]
        text_amd.set_position((amd_date, amd_price))
        text_amd.set_text(f'${amd_price:.2f}')
    
    if frame > 0:
        nvidia_price = nvidia_df['Close'].iloc[frame-1]
        nvidia_date = nvidia_df['Date'].iloc[frame-1]
        text_nvidia.set_position((nvidia_date, nvidia_price))
        text_nvidia.set_text(f'${nvidia_price:.2f}')
    
    if frame > 0:
        intel_price = intel_df['Close'].iloc[frame-1]
        intel_date = intel_df['Date'].iloc[frame-1]
        text_intel.set_position((intel_date, intel_price))
        text_intel.set_text(f'${intel_price:.2f}')
    
    return line_amd, line_nvidia, line_intel, text_amd, text_nvidia, text_intel



max_frames = max(len(amd_df), len(nvidia_df), len(intel_df))

anim = animation.FuncAnimation(fig, animate, frames=max_frames, interval=6, blit=True, repeat=True)



plt.tight_layout()


plt.show()