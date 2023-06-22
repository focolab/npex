import setuptools
import platform

if platform.system() == 'Darwin':
    setuptools.setup(
        name="npex",
        version="0.0.1",
        author="Greg Bubnis",
        author_email="gregory.bubnis@ucsf.edu",
        description="NeuroPAL extractor",
        long_description_content_type=open('readme.md').read(),
        packages=['npex'],
        install_requires=[
            'numpy>=1.22.4',
            'tifffile>=2022.5.4', 
            'pandas>=1.4.2',
            'matplotlib>=3.5.2',
            'pyqtgraph>=0.12.4',
            'pyqt6',
            'napari[pyqt6_experimental]',
            'foco-improc',
            'xmltodict'
        ],
        python_requires='<3.11',
    )

else:

    setuptools.setup(
        name="npex",
        version="0.0.1",
        author="Greg Bubnis",
        author_email="gregory.bubnis@ucsf.edu",
        description="NeuroPAL extractor",
        long_description_content_type=open('readme.md').read(),
        packages=['npex'],
        install_requires=[
            'numpy>=1.22.4',
            'tifffile>=2022.5.4', 
            'pandas>=1.4.2',
            'matplotlib>=3.5.2',
            'pyqtgraph>=0.12.4',
            'pyqt5',
            'napari>=0.4.16',
            'foco-improc',
            'xmltodict'
        ],
        python_requires='>=3.8',
    )
