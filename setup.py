# coding: utf-8

"""
    Core Operations

    The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API.  The Sparkfly documentation site is under development. If the documentation you're after isn't available here, please contact support@sparkfly.com and we will get you what you need.

    The version of the OpenAPI document: 1.0
    Contact: support@sparkfly.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "sparkfly"
VERSION = "1.1.10"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "aiohttp >= 3.8.4",
    "aiohttp-retry >= 2.8.3",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Core Operations",
    author="Sparkfly Support Team",
    author_email="support@sparkfly.com",
    url="https://github.com/growth-operations/sparkfly-api-client",
    keywords=["OpenAPI", "OpenAPI-Generator", "Core Operations"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description="""\
    The Sparkfly Platform provides a full lifecycle for promotions and rewards from creation to distribution to settlement. The platform integrates in real-time at the point-of-sale and provides item level discounting and tracking. The capabilities of the Sparkfly Platform are available through the use of the Sparkfly Platform API.  The Sparkfly documentation site is under development. If the documentation you&#39;re after isn&#39;t available here, please contact support@sparkfly.com and we will get you what you need.
    """,  # noqa: E501
    package_data={"sparkfly": ["py.typed"]},
)