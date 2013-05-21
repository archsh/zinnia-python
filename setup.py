#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string
import os,platform

__version__ = '0.06'

ARCH,OS = platform.architecture()
if OS.startswith('Windows'):
#CFLAGS =  /O2 /GA /GL /Gy /Oi /Ob2 /nologo /W3 /EHsc /MT /wd4244
#LDFLAGS = /link /OPT:REF /OPT:ICF /LTCG /NXCOMPAT /DYNAMICBASE ADVAPI32.LIB 
#DEFS =  -D_CRT_SECURE_NO_DEPRECATE -DDLL_EXPORT -DHAVE_WINDOWS_H -DVERSION="\"@VERSION@\"" -DPACKAGE="\"@PACKAGE@\""
#INC = -I. -I..
#svm.obj libzinnia.obj character.obj feature.obj recognizer.obj trainer.obj param.obj sexp.obj
    def_macros  =[('WIN32',1),('_WIN32',1),('_CRT_SECURE_NO_DEPRECATE',1),
                  ('DLL_EXPORT',1),('HAVE_WINDOWS_H',1),('VERSION','\\"%s\\"'%__version__),('PACKAGE','\\"_zinnia\\"')]
    extra_compile_args = ['/O2', '/GA', '/GL', '/Gy', '/Oi', '/Ob2', '/nologo', '/W3', '/EHsc', '/MT', '/wd4244']
    extra_link_args =['/link', '/OPT:REF', '/OPT:ICF', '/LTCG', '/NXCOMPAT', '/DYNAMICBASE', 'ADVAPI32.LIB']
    #ET199_LIB.append('ET199_S.lib')
elif OS.startswith('ELF'):
    def_macros  =[('LINUX',1)]
    extra_compile_args = []
    extra_link_args =[]
    #ET199_LIB.append('libET199.a')

setup(name = "zinnia-python",
      version=__version__,
      description="DR Licensing.",
      license="DR License",
      py_modules=["zinnia"],
      ext_modules = [Extension("_zinnia",
                               ["zinnia_wrap.cxx",
							    "recognizer.cpp",
								"trainer.cpp",
								"param.cpp",
								"sexp.cpp",
								#"zinnia_convert.cpp",
								"zinnia.cpp",
								"svm.cpp",
								"feature.cpp",
								"character.cpp",
								"libzinnia.cpp",
								#"zinnia_learn.cpp",
                                ],
                                #include_dirs=[],
                                #library_dirs=library_dirs,
                                #libraries=libraries,
                                extra_link_args=extra_link_args,
                                extra_compile_args=extra_compile_args,
                                define_macros=def_macros
                               )
                     ])
