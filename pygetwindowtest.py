from modulefinder import EXTENDED_ARG
from pywinauto import Application, win32defines
from pywinauto.win32functions import SetFocus, ShowWindow
import sys
import win32gui as wgui
import win32process as wproc
import win32api as wapi
import autoit
import pywinauto
import subprocess 
import selenium

# wins = subprocess.run('wmctrl -l', shell=True, stdout=subprocess.PIPE)
# title = next(ln for ln in wins.stdout.decode('utf-8').splitlines() if 'Edge' in ln)
# print (title)


# desktop = pywinauto.Desktop(backend="uia")
# window = desktop.windows(title="Microsoft Edge", control_type="Window")[0]
# wrapper_list = window.descendants(control_type="Window")
# for wrapper in wrapper_list:
#     print(wrapper.window_text())


# autoit.win_activate("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")





















# app = Application().connect(path="C:\Program Files (x86)\Microsoft\Edge\Application")
# w = app.top_window()

# #bring window into foreground
# if w.HasStyle(win32defines.WS_MINIMIZE): # if minimized
#     ShowWindow(w.wrapper_object(), 9) # restore window state
# else:
#     SetFocus(w.wrapper_object()) #bring to front





# def main(*argv):
#     if not argv:
#         window_name = input("Untitled - Notepad")
#     else:
#         window_name = argv[0]

#     handle = wgui.FindWindow(None, window_name)
#     print("Window `{0:s}` handle: 0x{1:016X}".format(window_name, handle))
#     if not handle:
#         print("Invalid window handle")
#         return
#     remote_thread, _ = wproc.GetWindowThreadProcessId(handle)
#     wproc.AttachThreadInput(wapi.GetCurrentThreadId(), remote_thread, True)
#     prev_handle = wgui.SetFocus(handle)


# if __name__ == "__main__":
#     print("Python {0:s} {1:d}bit on {2:s}\n".format(" ".join(item.strip() for item in sys.version.split("\n")), 64 if sys.maxsize > 0x100000000 else 32, sys.platform))
#     main(*sys.argv[1:])
#     print("\nDone.")
