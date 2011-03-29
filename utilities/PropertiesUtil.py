#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# (C) Copyright 2011 Jose Blanco <jose.blanco[a]vikuit.com>
# 
# This file is part of "vikuit".
# 
# "vikuit" is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# "vikuit" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with "vikuit".  If not, see <http://www.gnu.org/licenses/>.
##
def loadProperties(fileName):
    propFile = file(fileName, "rU" )
    propDict = dict()
    for propLine in propFile:
        propDef = propLine.strip()
        if len(propDef) == 0:
            continue
        if propDef[0] in ( '!', '#' ):
            continue
        punctuation = [ propDef.find(c) for c in ':= ' ] + [ len(propDef) ]
        found = min( [ pos for pos in punctuation if pos != -1 ] )
        name = propDef[:found].rstrip()
        value = propDef[found:].lstrip(":= ").rstrip()
        propDict[name] = value
    propFile.close()
    return propDict