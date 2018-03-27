from setuptools import setup

setup(
    name='app_led',
    packages=['app_led'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-socketio',
        'io_blueprint',
        'git+http://github.com/m-housh/io-blueprint.git'
        'serial',
    ],
)
