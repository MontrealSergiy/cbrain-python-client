# coding: utf-8

"""
    CBRAIN API

    API for interacting with the CBRAIN Platform  # noqa: E501

    OpenAPI spec version: 6.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cbrain_api
from cbrain_api.api.data_providers_api import DataProvidersApi  # noqa: E501
from cbrain_api.rest import ApiException


class TestDataProvidersApi(unittest.TestCase):
    """DataProvidersApi unit test stubs"""

    def setUp(self):
        self.api = cbrain_api.api.data_providers_api.DataProvidersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_providers_get(self):
        """Test case for data_providers_get

        Get a list of the Data Providers available to the current user.  # noqa: E501
        """
        pass

    def test_data_providers_id_browse_get(self):
        """Test case for data_providers_id_browse_get

        List the files on a Data Provider.  # noqa: E501
        """
        pass

    def test_data_providers_id_delete_post(self):
        """Test case for data_providers_id_delete_post

        Deletes unregistered files from a CBRAIN Data provider.  # noqa: E501
        """
        pass

    def test_data_providers_id_get(self):
        """Test case for data_providers_id_get

        Get information on a particular Data Provider.  # noqa: E501
        """
        pass

    def test_data_providers_id_is_alive_get(self):
        """Test case for data_providers_id_is_alive_get

        Pings a Data Provider to check if it is running.  # noqa: E501
        """
        pass

    def test_data_providers_id_register_post(self):
        """Test case for data_providers_id_register_post

        Registers a file as a Userfile in CBRAIN.  # noqa: E501
        """
        pass

    def test_data_providers_id_unregister_post(self):
        """Test case for data_providers_id_unregister_post

        Unregisters files as Userfile in CBRAIN.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()