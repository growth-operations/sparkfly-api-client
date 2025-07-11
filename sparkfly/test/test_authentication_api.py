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

from sparkfly.api.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.IsolatedAsyncioTestCase):
    """AuthenticationApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = AuthenticationApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_post_auth(self) -> None:
        """Test case for post_auth

        Request an Authentication Token
        """
        pass


if __name__ == '__main__':
    unittest.main()
