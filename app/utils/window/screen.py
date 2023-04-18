import platform
import subprocess

def screen(x, y):
    system = platform.system()
    if system == "Linux":
        cmd_x = 'xrandr | grep "current" | cut -d "," -f2 | cut -d " " -f3'
        cmd_y = 'xrandr | grep "current" | cut -d "," -f2 | cut -d " " -f5'
        window_x = subprocess.run(cmd_x, shell=True, stdout=subprocess.PIPE, text=True)
        window_y = subprocess.run(cmd_y, shell=True, stdout=subprocess.PIPE, text=True)
        window_x = int(window_x.stdout.strip())
        window_y = int(window_y.stdout.strip())
        size_x = int(window_x * x)
        size_y = int(window_y * y)
        loc_x = (window_x - size_x) // 2
        loc_y = (window_y - size_y) // 2
    if system == "Windows":
        cmd_x = 'wmic path Win32_VideoController get CurrentHorizontalResolution'
        cmd_y = 'wmic path Win32_VideoController get CurrentVerticalResolution'
        window_x = subprocess.run(cmd_x, shell=True, stdout=subprocess.PIPE, text=True)
        window_y = subprocess.run(cmd_y, shell=True, stdout=subprocess.PIPE, text=True)
        window_x = int(window_x.stdout.strip().split()[1])
        window_y = int(window_y.stdout.strip().split()[1])
        size_x = int(window_x * x)
        size_y = int(window_y * y)
        loc_x = (window_x - size_x) // 2
        loc_y = (window_y - size_y) // 2

    return size_x, size_y, loc_x, loc_y

### Get Window Size

# window_menuApp.get_screen_size()
# window_menuApp.current_size_accurate()
# window_menuApp.size
# window_menuApp.current_location()