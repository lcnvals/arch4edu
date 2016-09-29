#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'arch4edu-x86_64'

def pre_build():
  aur_pre_build('python-tensorflow-git')

  import os
  os.environ['https_proxy']='127.0.0.1:8123'

  for line in edit_file('PKGBUILD'):
    if 'pkgname=' in line:
        print('pkgname=python-tensorflow-nogpu-git')
    elif 'pkgdesc' in line:
        print(line.replace('."','.(no GPU support)"'))
    elif 'pkgver()' in line:
        print('optdepends=()')
        print(line)
    elif 'conflicts' in line:
        print(line.replace(')',' "python-tensorflow-git" "python-tensorflow-gpu5.2-git" "python-tensorflow-gpu6.1-git")'))
    elif './configure' in line:
        print('  export TF_NEED_GCP=0')
        print('  export CC=gcc-5')
        print('  export CXX=g++-5')
        print('  echo -e "/usr/lib/python3.5/site-packages"|'+line)
    else:
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
