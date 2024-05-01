# https://www.codewars.com/kata/53b138b3b987275b46000115

def comp(ver): # modified ipv4 address parsing procedure
    return sum([a*100**(5-i) for i, a in enumerate(map(int,ver.split('.')))]) 

def compare_versions(version1,version2):
    return comp(version1) >= comp(version2)

# clever:
from distutils.version import LooseVersion, StrictVersion
return LooseVersion(version1) >= LooseVersion(version2)
