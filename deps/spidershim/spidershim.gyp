{
  'targets': [
    {
      'target_name': 'spidershim',
      'type': '<(library)',

      'include_dirs': [
        'include',
        '<(SHARED_INTERMEDIATE_DIR)'
      ],
      'conditions': [
        [ 'target_arch=="ia32"', { 'defines': [ '__i386__=1' ] } ],
        [ 'target_arch=="x64"', { 'defines': [ '__x86_64__=1' ] } ],
        [ 'target_arch=="arm"', { 'defines': [ '__arm__=1' ] } ],
        ['node_engine=="spidermonkey"', {
          'dependencies': [
            'spidermonkey.gyp:spidermonkey#host',
          ],
          'export_dependent_settings': [
            'spidermonkey.gyp:spidermonkey#host',
          ],
        }],
      ],

      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
        'conditions': [
          [ 'target_arch=="arm"', {
            'defines': [ '__arm__=1' ]
          }],
        ],
      },

      'sources': [
        'include/libplatform/libplatform.h',
        'include/v8.h',
        'include/v8config.h',
        'include/v8-debug.h',
        'include/v8-platform.h',
        'include/v8-profiler.h',
        'include/v8-version.h',
        'src/v8array.cc',
      ],
    },
  ],
}
