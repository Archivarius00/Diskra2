from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='minTREEalgorythmes',
  version='0.0.1',
  author='Archivarius & co',
  author_email='rewiwer00@mail.com',
  description='Алгоритмы минимального остовного дерева.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Archivarius00/Diskra2',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
  ],
  keywords='оставное-дерево',
  project_urls={
    'none'
  },
  python_requires='>=3.7'
)