from distutils.core import setup, Extension

setup(name='info',
      ext_modules=[
          Extension('info',
                    ['info.c'],
                    include_dirs=['/usr/src/linux-headers-4.9.61-sched.8.0+/include/uapi', '/usr/src/linux-headers-4.9.61-sched.8.0+/include', '/usr/include/python3.5m'],
                    define_macros=[('NUM_SUBFLOWS', '2'), ('SOL_TCP', '6')]
                    )
      ])
