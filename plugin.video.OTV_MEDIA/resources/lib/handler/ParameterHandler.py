# -*- coding: utf-8 -*-
import sys
try:
    from urlparse import parse_qsl, urlsplit
    from urllib import unquote_plus, urlencode
except ImportError:
    from urllib.parse import parse_qsl, urlsplit, unquote_plus, urlencode

from resources.lib.util import urlEncode, Unquote
class ParameterHandler:
    def __init__(self):
        params = dict()
        if len(sys.argv) >= 3 and len(sys.argv[2]) > 0:
            params = dict(parse_qsl(urlsplit(sys.argv[2]).query))
        self.__params = params

    def getAllParameters(self):
        # returns all parameters as dictionary
        return self.__params

    def getValue(self, sParamName):
        if (self.exist(sParamName)):
            sParamValue = self.__params[sParamName]
            return Unquote(sParamValue)

        return False


    def exist(self, paramName):
        # checks if paramter with the name "paramName" exists
        return paramName in self.__params

    def setParam(self, paramName, paramValue):
        # set the value of the parameter with the name "paramName" to "paramValue"
        # if there is no such parameter, the parameter is created
        # if no value is given "paramValue" is set "None"
        paramValue = str(paramValue)
        self.__params.update({paramName: paramValue})

    def addParams(self, paramDict):
        # adds a whole dictionary {key1:value1,...,keyN:valueN} of parameters to the ParameterHandler
        # existing parameters are updated
        for key, value in paramDict.items():
            self.__params.update({key: str(value)})

    def getParameterAsUri(self):
        outParams = dict()
        if 'params' in self.__params:
            del self.__params['params']
        if 'function' in self.__params:
            del self.__params['function']
        if 'title' in self.__params:
            del self.__params['title']
        if 'site' in self.__params:
            del self.__params['site']

        if len(self.__params) > 0:
            for param in self.__params:
                if len(self.__params[param]) < 1:
                    continue
                outParams[param] = unquote_plus(self.__params[param])
            return urlencode(outParams)
        return 'params=0'
