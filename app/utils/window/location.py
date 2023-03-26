import subprocess

def location(x, y):
    cmd_x = 'xrandr | grep "current" | cut -d "," -f2 | cut -d " " -f3'
    cmd_y = 'xrandr | grep "current" | cut -d "," -f2 | cut -d " " -f5'
    window_x = subprocess.run(cmd_x, shell=True, stdout=subprocess.PIPE, text=True)
    window_y = subprocess.run(cmd_y, shell=True, stdout=subprocess.PIPE, text=True)
    window_x = int(window_x.stdout.strip())
    window_y = int(window_y.stdout.strip())
    size_x = (window_x - x) // 2
    size_y = (window_y - y) // 2

    return size_x, size_y

### Get Window Size

# window_menuApp.get_screen_size()
# window_menuApp.current_size_accurate()
# window_menuApp.size
# window_menuApp.current_location()