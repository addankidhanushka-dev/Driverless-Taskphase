from setuptools import find_packages, setup

package_name = 'tasktwo_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhanushka',
    maintainer_email='addankidhanushka@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'node1 = tasktwo_nodes.node1:main',
            'node2 = tasktwo_nodes.node2:main',
            'node3 = tasktwo_nodes.node3:main',
        ],
    },
)
