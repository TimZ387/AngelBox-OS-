from setuptools import setup, find_packages

setup(
    name="AngelBox",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'colorama>=0.4.6',
        'requests>=2.31.0',
        'psutil>=5.9.5',
        'pygments>=2.16.1'
    ],
    entry_points={
        'console_scripts': [
            'angelbox = main:main',
        ],
    },
    author="Your Name",
    description="AngelBox OS in Python",
    license="MIT",
    keywords="os python shell",
    url="https://github.com/yourname/angelbox"
)