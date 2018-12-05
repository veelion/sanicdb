from setuptools import setup
import sanicdb

setup(
    name="sanicdb",
    version=sanicdb.version,
    description=sanicdb.__doc__,
    author="veelion",
    author_email="veelion@gmail.com",
    url='https://github.com/veelion/sanicdb',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: BSD',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'pymysql',
        'aiomysql',
    ],
    license='BSD',
    py_modules=['sanicdb'],
    include_package_data=True,
    zip_safe=False
)
