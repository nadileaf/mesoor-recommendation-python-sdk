import setuptools

REQUIRES = [
    'betterproto[compiler]==1.2.5',
    'grpcio-tools==1.31.0'
]
setuptools.setup(
    name='mesoor-recommendation-sdk',
    version='0.0.1',
    author='Mesoor',
    author_email='',
    description='Python SDK for Mesoor recommendation system',
    url="https://github.com/nadileaf/mesoor-recommendation-sdk",
    license='MIT License',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7, <4',
    install_requires=REQUIRES
)
