import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    version = '1.0.0',
    name='Huanghw4',
    author='MinHuang',
    author_email='minhuang15@outlook.com',
    description='BMI500 HW4',
    keywords='example, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/warming151/Huang-bmi-hw4',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['numpy',
		'matplotlib',
		'pandas',
		'scipy',
        'scanpy',
        'seaborn',
        'h5py'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },

)
