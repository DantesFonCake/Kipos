print(__name__+": Entered main")
print(__name__ + ": Importing main_mode")
import main_mode
print(__name__ + ": Imported main_mode")
print(__name__ + ": Entering main_mode")
main_mode.enter()
print(__name__ + ": Left main_mode")
import machine
print(__name__+": Rebooting")
machine.reset()
