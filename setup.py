from setuptools import setup, find_packages

setup(
    name='gifify',
    version='0.1.0',
    packages=find_packages(),
    description='PythonからFFmpegをコールして動画をGIFアニメーション化',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Toshihiko ARai',
    author_email='i.officearai@gmail.com',
    url='https://github.com/aragig/gifify',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)