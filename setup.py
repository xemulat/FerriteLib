from distutils.core import setup
setup(
  name = 'FerriteLib',
  packages = ['FerriteLib'],
  version = '0.1',
  license='mit',
  description = "Load JSON at the speed of light!",
  long_description="Usage: \n`text = getvalue('file.json', 'text')`\n`file = getfile('file.json')`",
  author = 'Xemulated',
  author_email = 'xemulated@tuta.io',
  url = 'https://github.com/xemulat',
  download_url = 'https://github.com/xemulat/FerriteLib/archive/refs/tags/0.1.tar.gz',
  keywords = ['QOL', 'xemulated', 'json'],
  install_requires=[''],
  classifiers=[
    'Development Status :: 4 - Beta',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.10',
  ],
)