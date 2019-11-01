from tenda11n import tenda11n_api
import time

# Tenda11N API init
# This API uses 192.168.0.1 as default router ip, you can change it by Tenda11N("192.168.X.X")
api = tenda11n_api.Tenda11N() 

# Login to router
if not api.login("admin", "pass1234"): # Enter your own login credentials
  print("Failed to login to router page")
  exit()

# Do Anything
def printDict(_dict, key):
    if key in _dict:
        print("[{0}]{1}".format(key, _dict[key]))

def printNetworkStats():
    networkStats = api.networkUsageStats()    # Returns dict with all active connections
    printDict(networkStats, "192.168.0.200")  # Print network stats for 192.168.0.200
    printDict(networkStats, "192.168.0.100")  # ..

while 1:
    printNetworkStats()
    time.sleep(1)