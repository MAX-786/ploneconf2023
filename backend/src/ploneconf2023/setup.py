"""Installer for the ploneconf2023 package."""
from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="ploneconf2023",
    version="1.0.0a1",
    description="Plone Conference Training configuration package.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Plone Foundation",
    author_email="collective@plone.org",
    url="https://github.com/MAX-786/ploneconf2023",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/ploneconf2023",
        "Source": "https://github.com/MAX-786/ploneconf2023",
        "Tracker": "https://github.com/MAX-786/ploneconf2023/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Plone",
        "prettyconf",
        "plone.api",
    ],
    extras_require={
        "test": [
            "pytest-plone>=0.5.0",
            "pytest-cov",
            "pytest",
            "zope.pytestlayer",
            "zest.releaser[recommended]",
            "plone.app.testing[robot]",
            "plone.restapi[test]",
            "collective.MockMailHost",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = ploneconf2023.locales.update:update_locale
    """,
)
