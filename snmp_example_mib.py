#sudo apt-get install snmp-mibs-downloader
from pysnmp.hlapi import *

iterator = nextCmd(
    SnmpEngine(),
    CommunityData('public',mpModel=0),
    UdpTransportTarget(('192.168.56.111',161)),
    ContextData(),
    ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
    ObjectType(ObjectIdentity('IF-MIB','ifMtu')),
    ObjectType(ObjectIdentity('IF-MIB','ifSpeed')),
    ObjectType(ObjectIdentity('IF-MIB','ifPhysAddress')),
    ObjectType(ObjectIdentity('IF-MIB','ifType')),
    lexicographicMode=False
        )

for errorIndication, errorStatus, errorIndex, varBinds in iterator:
    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print(errorStatus.prettyPrint())
        break
    else:
        for varBind in varBinds:
            print(' ='.join([x.prettyPrint() for x in varBind]))

        
