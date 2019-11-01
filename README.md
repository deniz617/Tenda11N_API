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
#### Note: Do not forget to add tenda11n_api. or as whatever you named the module in front of the functions before you call them.

| Function(args)                                     | Function Description                                                           | Return value                                                     |
|----------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| login(user,pw)                                     | Logins to router, you have to call this function after first init.             | returns False on fail otherwise True                             |
| networkUsageStats()                                | Gets network usage stats about every connected device.                         | returns a dict with every ip as key. Returns empty dict on fail. |
| getBandwithCtrl_List()                             | Gets bandwith control rules/list.                                              | Returns a array of rules.                                        |
| setBandwithCtrl_List(bandwithCtrl_flag, ctrl_list) | Sets Bandwith control rules/list. (Get the list first and use it as reference) | Returns a array of new rules.                                    |
| reboot()                                           | Reboots the router.                                                            | Returns nothing.                                                 |
