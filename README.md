# Tenda11N API
Unofficial Tenda11N Router API for Python.

## Features
- Tracking of Network bandwith usage
- Get/Set of bandwith rules
- Reboot router

### Example
```python
from tenda11n import tenda11n_api

# Tenda11N API init
# This API uses 192.168.0.1 as default router ip, you can change it by Tenda11N("192.168.X.X")
api = tenda11n_api.Tenda11N("192.168.1.1") 

if not api.login("admin", "pass1234"):
  print("Failed to login to router page")
  exit()

# Get current network stats
networkStats = api.networkUsageStats()

# Print 
for connection in networkStats:
  print("[{0}]{1}".format(connection, networkStats[connection]))
```

## Existing Functions
