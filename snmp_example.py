from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('192.168.56.111',161)),
    ContextData(),
    ObjectType(ObjectIdentity('iso.3.6.1.2.1.25.3.2.1.3.196608')),
    #ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
    #ObjectType(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
        )

errorIndication,errorStatus,errorIndex,varBinds = next(iterator)

if errorIndication:
    print(errorIndication)

elif errorStatus:
    print(errorStatus.prettyPrint())

else:
    for varBind in varBinds:
        print(' ='.join([x.prettyPrint() for x in varBind]))
