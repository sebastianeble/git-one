import tkinter as tk
from tkinter import filedialog
import mdfreader

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

yop=mdfreader.Mdf(file_path)
info=mdfreader.MdfInfo()
print(info.list_channels(file_path))
# yop.plot("MecActtn_[0].p_CluVlvReq")
print(yop.get_channel("$CalibrationLog"))
