print(__name__+": Entered boot")
print(__name__+": Importing settings")
import settings
print(__name__+": Imported settings")
print(__name__+": Started boot settings")
settings.on_boot()
print(__name__+": Leaving boot")