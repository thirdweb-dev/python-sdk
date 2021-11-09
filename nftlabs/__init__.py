import sys

# make sure bar is in sys.modules
import thirdweb
# link this module to bar
sys.modules[__name__] = sys.modules['thirdweb']

# Or simply
sys.modules[__name__] = __import__('thirdweb')
