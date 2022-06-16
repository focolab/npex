import setuptools
setuptools.setup(
    name="npex",
    version="0.0.1",
    author="Greg Bubnis",
    author_email="gregory.bubnis@ucsf.edu",
    description="NeuroPAL extractor",
    long_description_content_type=open('readme.md').read(),
    packages=['npex'],
    install_requires=[
#          'numpy>=1.22.4',
#          'tifffile>=2022.5.4',
    ],
    python_requires='>=3.7',
)