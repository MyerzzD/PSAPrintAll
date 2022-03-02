
import subprocess

p = subprocess("Notepad")
# Waits for the window for 10 seconds
w = p.WaitWindow("*", "Open*", -1, 10000)
if w.Exists:
  w.Activate
  print("Open dialog picture")
else:
  print("Incorrect window")