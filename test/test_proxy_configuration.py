# coding: utf-8

"""
    Multilogin v2 Local API

    This API is intended to be used from version 5 of Multilogin for managing cloud saved browser profiles.   To start/stop browser profiles please use the [Multilogin v1 Local API](https://app.swaggerhub.com/apis/Multilogin/MultiloginLocalRestAPI/1.0). # Creating profiles To create a profile send a POST request to the /profile endpoint. The mandatory parameters are the name of the profile, operating system and type of browser. The rest of the fingerprint will be generated automatically, unless you specify more details.  Here is an example request to create a Mimic profile for windows with a proxy: <pre>{ <br>\"name\": \"testProfile\", <br>\"browser\": \"mimic\", <br>\"os\": \"win\", <br>\"network\": { <br>    \"proxy\": { <br>        \"type\": \"HTTP\", <br>        \"host\": \"192.168.1.1\", <br>        \"port\": \"1080\", <br>        \"username\": \"username\", <br>        \"password\": \"password\" <br>        } <br>    } <br>} </pre> # Groups Each group has an unique ID that can be assigned either during the creating of a profile or by updating a profile.  The default group ID is 00000000-0000-0000-0000-000000000000 for Unassigned  # noqa: E501

    OpenAPI spec version: v2-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.proxy_configuration import ProxyConfiguration  # noqa: E501
from swagger_client.rest import ApiException


class TestProxyConfiguration(unittest.TestCase):
    """ProxyConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProxyConfiguration(self):
        """Test ProxyConfiguration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.proxy_configuration.ProxyConfiguration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
