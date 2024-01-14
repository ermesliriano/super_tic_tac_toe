from setuptools import setup

setup(
    name='super-tic-tac-toe',
    version='0.1.0',
    packages=['super_tic_tac_toe'],
    install_requires=["pygame","importlib"],
    entry_points={
        'console_scripts': [
            'super-tic-tac-toe = super_tic_tac_toe.__main__:main'
        ]
    },
)