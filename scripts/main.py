print(__name__+": Entered main")
print(__name__+": Importing settings")
import settings
print(__name__+": Imported settings")
if settings.initialized:
    print(__name__ + ": Importing main_mode")
    import main_mode
    print(__name__ + ": Imported main_mode")
    print(__name__ + ": Entering main_mode")
    main_mode.enter()
    print(__name__ + ": Left main_mode")
else:
    print(__name__ + ": Importing initialization_mode")
    import initialization_mode
    print(__name__ + ": Imported initialization_mode")
    print(__name__ + ": Entering initialization_mode")
    initialization_mode.enter()
    print(__name__ + ": Left initialization_mode")

import machine
print(__name__+": Rebooting")
machine.reset()
