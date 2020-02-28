import btac

# May instantiate the Btac class to use REST utilitiy functions directly.
bt = btac.Btac()
# May instantiate subclasses for methods that have direct match with API methods.
cp = btac.ControlPanel()

# Some dummy variables to use as test parameters.
oid = "s0m30rg4n1z4t10nid"
did = "s0m3d3v1c31d"        

# TODO: Add couple examples.
device_info = bt.detailed(oid, did)
print(device_info)

id = "s0m31d3nt1ty1d"
identity = bt.identity_detailed(oid, id)
print(identity)