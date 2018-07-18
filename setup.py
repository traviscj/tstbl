from setuptools import setup

setup(
    name='tstbl',
    version='0.1',
    py_modules=['tstbl'],
    install_requires=[
        'click',
        'click_completion',
        'tablib',
    ],
    entry_points='''
        [console_scripts]
        tstbl=tstbl:main
    ''',
    exclude_package_data={'': ['.gitignore'],},
)
