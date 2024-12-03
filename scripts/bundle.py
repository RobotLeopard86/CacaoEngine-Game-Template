#!/usr/bin/env python

import pathlib
import shutil
import sys
import os

buildroot = pathlib.Path(os.environ['MESON_BUILD_ROOT'])

if not buildroot.exists():
	raise FileNotFoundError('Build directory does not exist.')

bundleroot = (buildroot / 'bundle')
if bundleroot.exists():
	shutil.rmtree(bundleroot)

bundleroot.mkdir()

exe_suffix = '.exe' if os.name == 'nt' else ''
so_prefix = '' if os.name == 'nt' else 'lib'
so_suffix = '.dll' if os.name == 'nt' else '.dylib' if sys.platform.startswith('darwin') else '.so'

srcroot = pathlib.Path(os.environ['MESON_SOURCE_ROOT'])

shutil.copy2(buildroot / 'subprojects' / 'cacaoengine' / 'cacao' / ('cacao-template' + exe_suffix), bundleroot)
shutil.copy2(srcroot / 'launchconfig.cacao.yml', bundleroot)
shutil.copy2(buildroot / ('launch' + so_suffix), bundleroot)

def get_engine_path():
	return (bundleroot / ('cacao-template' + exe_suffix))
