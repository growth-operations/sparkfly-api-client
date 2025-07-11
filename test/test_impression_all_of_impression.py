# coding: utf-8

"""
    Core Operations

    The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API.  The Sparkfly documentation site is under development. If the documentation you're after isn't available here, please contact support@sparkfly.com and we will get you what you need.

    The version of the OpenAPI document: 1.0
    Contact: support@sparkfly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sparkfly_api_client.models.impression_all_of_impression import ImpressionAllOfImpression

class TestImpressionAllOfImpression(unittest.TestCase):
    """ImpressionAllOfImpression unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImpressionAllOfImpression:
        """Test ImpressionAllOfImpression
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImpressionAllOfImpression`
        """
        model = ImpressionAllOfImpression()
        if include_optional:
            return ImpressionAllOfImpression(
                cookie_id = '',
                offer_xid = '',
                annotations = sparkfly_api_client.models.impression_request_impression_annotations.impression_request_impression_annotations(
                    str1 = 56, 
                    str2 = 56, 
                    str3 = '', 
                    str4 = True, 
                    str5 = '', ),
                created_at = '',
                updated_at = '',
                channel_id = '',
                channel_name = '',
                creative_name = '',
                errors = sparkfly_api_client.models.errors.errors(
                    errors = sparkfly_api_client.models.response_body_errors.ResponseBodyErrors(), )
            )
        else:
            return ImpressionAllOfImpression(
        )
        """

    def testImpressionAllOfImpression(self):
        """Test ImpressionAllOfImpression"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
