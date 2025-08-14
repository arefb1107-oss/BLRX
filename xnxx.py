# launcher.py
import platform

arch = platform.architecture()[0]

if arch == '64bit':
    import ROM1 as ROM
else:
    import ROM as ROM