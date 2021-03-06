import pyopencl as cl
import utils
from ocl_platform import Platform

class PlatformList():

    def enter(self):
        utils.cls()
        print("=" * 85)

    def list(self):
        idx = 1
        for platform in cl.get_platforms():
            print("%2d platform NAME   : %10s" % (idx, platform.name))
            print("            VERSION: %10s" % (platform.version))
            print("            PROFILE: %10s" % (platform.profile))
            print("            VENDOR : %10s" % (platform.vendor))
            idx = idx + 1
            print("-" * 85)
        return idx - 1

    def choose(self, index):
        return Platform(cl.get_platforms()[index])

    def prompt(self):
        return "Please choose which platform you want to see"
