{
  "targets": [{
    "target_name": "leveldb",
    "type": "static_library",
    "standalone_static_library": 1,
    "dependencies": [
      "../snappy/snappy.gyp:snappy",
      "../zlib/zlib.gyp:zlib"
    ],
    "direct_dependent_settings": {
      "include_dirs": [
        "leveldb/include/",
        "leveldb/port/",
        "leveldb/util",
        "leveldb/"
      ]
    },
    "defines": [
      "SNAPPY=0",
      "DLLX="
    ],
    "include_dirs": [
      "leveldb/",
      "leveldb/include/"
    ],
    "conditions": [
      ["OS == 'win'", {
        "conditions": [
          ["MSVS_VERSION != '2015' and MSVS_VERSION != '2013'", {
            "include_dirs": [ "leveldb/port/win" ]
          }]
        ],
        "include_dirs": [
          "port-libuv/"
        ],
        "defines": [
          "LEVELDB_PLATFORM_UV=1",
          "NOMINMAX=1",
          "_HAS_EXCEPTIONS=0"
        ],
        "sources": [
          "port-libuv/port_uv.cc",
          "port-libuv/env_win.cc",
          "port-libuv/win_logger.cc"
        ],
        "msvs_settings": {
          "VCCLCompilerTool": {
            "RuntimeTypeInfo": "false",
            "EnableFunctionLevelLinking": "true",
            "ExceptionHandling": "2",
            "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244" ]
          }
        }
      }, {
        "sources": [
          "leveldb/port/port_posix.cc",
          "leveldb/port/port_posix.h",
          "leveldb/util/env_posix.cc",
          "leveldb/port/port_win.cc",
          "leveldb/port/port_win.h",
          "leveldb/util/env_win.cc",
          "leveldb/util/Filepath.h",
          "leveldb/util/win_logger.cc",
          "leveldb/util/win_logger.h"
        ],
        "defines": [
          "LEVELDB_PLATFORM_POSIX=1"
        ],
        "ccflags": [
          "-fno-builtin-memcmp",
          "-fPIC"
        ],
        "cflags": [ "-std=c++0x" ],
        "cflags!": [ "-fno-tree-vrp" ]
      }],
      ["OS != 'win'" and "OS != 'freebsd'", {
        "cflags": [
          "-Wno-sign-compare",
          "-Wno-unused-but-set-variable"
        ]
      }],
      ["OS == 'linux'", {
        "defines": [
          "OS_LINUX=1"
        ],
        "libraries": [
          "-lpthread"
        ],
        "ccflags": [
          "-pthread"
        ]
      }],
      ["OS == 'freebsd'", {
        "defines": [
          "OS_FREEBSD=1",
          "_REENTRANT=1"
        ],
        "libraries": [
          "-lpthread"
        ],
        "ccflags": [
          "-pthread"
        ],
        "cflags": [
          "-Wno-sign-compare"
        ]
      }],
      ["OS == 'openbsd'", {
        "defines": [
          "OS_OPENBSD=1",
          "_REENTRANT=1"
        ],
        "libraries": [
          "-lpthread"
        ],
        "ccflags": [
          "-pthread"
        ],
        "cflags": [
          "-Wno-sign-compare"
        ]
      }],
      ["OS == 'solaris'", {
        "defines": [
          "OS_SOLARIS=1",
          "_REENTRANT=1"
        ],
        "libraries": [
          "-lrt",
          "-lpthread"
        ],
        "ccflags": [
          "-pthread"
        ]
      }],
      ["OS == 'ios'", {
        "defines": [
          "OS_IOS=1"
        ],
        "libraries": [],
        "ccflags": [],
        "xcode_settings": {
          "WARNING_CFLAGS": [
            "-Wno-sign-compare",
            "-Wno-unused-variable",
            "-Wno-unused-function"
          ]
        }
      }],
      ["OS == 'mac'", {
        "defines": [
          "OS_MACOSX=1"
        ],
        "libraries": [],
        "ccflags": [],
        "xcode_settings": {
          "WARNING_CFLAGS": [
            "-Wno-sign-compare",
            "-Wno-unused-variable",
            "-Wno-unused-function"
          ]
        }
      }],
      ["OS == 'android'", {
        "defines": [
          "OS_ANDROID=1",
          "_REENTRANT=1"
        ],
        "libraries": [
          "-lpthread"
        ],
        "ccflags": [
          "-pthread",
          "-fno-builtin-memcmp"
        ],
        "cflags": [
          "-fPIC"
        ],
        "cflags!": [
          "-fPIE",
          "-mfloat-abi=hard",
          "-Wno-unused-but-set-variable"
        ]
      }],
      ["target_arch == 'arm'", {
        "cflags": [
          "-mfloat-abi=hard"
        ]
      }]
    ],
    "sources": [
      "leveldb/db/builder.cc",
      "leveldb/db/builder.h",
      "leveldb/db/db_impl.cc",
      "leveldb/db/db_impl.h",
      "leveldb/db/db_iter.cc",
      "leveldb/db/db_iter.h",
      "leveldb/db/filename.cc",
      "leveldb/db/filename.h",
      "leveldb/db/dbformat.cc",
      "leveldb/db/dbformat.h",
      "leveldb/db/log_format.h",
      "leveldb/db/log_reader.cc",
      "leveldb/db/log_reader.h",
      "leveldb/db/log_writer.cc",
      "leveldb/db/log_writer.h",
      "leveldb/db/memtable.cc",
      "leveldb/db/memtable.h",
      "leveldb/db/repair.cc",
      "leveldb/db/skiplist.h",
      "leveldb/db/snapshot.h",
      "leveldb/db/table_cache.cc",
      "leveldb/db/table_cache.h",
      "leveldb/db/version_edit.cc",
      "leveldb/db/version_edit.h",
      "leveldb/db/version_set.cc",
      "leveldb/db/version_set.h",
      "leveldb/db/write_batch.cc",
      "leveldb/db/write_batch_internal.h",
      "leveldb/helpers/memenv/memenv.cc",
      "leveldb/helpers/memenv/memenv.h",
      "leveldb/include/leveldb/cache.h",
      "leveldb/include/leveldb/comparator.h",
      "leveldb/include/leveldb/db.h",
      "leveldb/include/leveldb/dumpfile.h",
      "leveldb/include/leveldb/env.h",
      "leveldb/include/leveldb/filter_policy.h",
      "leveldb/include/leveldb/iterator.h",
      "leveldb/include/leveldb/options.h",
      "leveldb/include/leveldb/slice.h",
      "leveldb/include/leveldb/status.h",
      "leveldb/include/leveldb/table.h",
      "leveldb/include/leveldb/table_builder.h",
      "leveldb/include/leveldb/write_batch.h",
      "leveldb/port/port.h",
      "leveldb/port/port_posix_sse.cc",
      "leveldb/table/block.cc",
      "leveldb/table/block.h",
      "leveldb/table/block_builder.cc",
      "leveldb/table/block_builder.h",
      "leveldb/table/filter_block.cc",
      "leveldb/table/filter_block.h",
      "leveldb/table/format.cc",
      "leveldb/table/format.h",
      "leveldb/table/iterator.cc",
      "leveldb/table/iterator_wrapper.h",
      "leveldb/table/merger.cc",
      "leveldb/table/merger.h",
      "leveldb/table/table.cc",
      "leveldb/table/table_builder.cc",
      "leveldb/table/two_level_iterator.cc",
      "leveldb/table/two_level_iterator.h",
      "leveldb/util/arena.cc",
      "leveldb/util/arena.h",
      "leveldb/util/bloom.cc",
      "leveldb/util/cache.cc",
      "leveldb/util/coding.cc",
      "leveldb/util/coding.h",
      "leveldb/util/comparator.cc",
      "leveldb/util/crc32c.cc",
      "leveldb/util/crc32c.h",
      "leveldb/util/env.cc",
      "leveldb/util/filter_policy.cc",
      "leveldb/util/hash.cc",
      "leveldb/util/hash.h",
      "leveldb/util/logging.cc",
      "leveldb/util/logging.h",
      "leveldb/util/mutexlock.h",
      "leveldb/util/options.cc",
      "leveldb/util/random.h",
      "leveldb/util/status.cc",
      "leveldb/db/zlib_compressor.cc",
      "leveldb/db/zopfli_compressor.cc",
      "leveldb/db/zstd_compressor.cc",
      "leveldb/include/leveldb/compressor.h",
      "leveldb/include/leveldb/decompress_allocator.h",
      "leveldb/include/leveldb/zlib_compressor.h",
      "leveldb/include/leveldb/zopfli_compressor.h",
      "leveldb/include/leveldb/zstd_compressor.h",
      "leveldb/include/leveldb/iterator.h",
      "leveldb/util/env_boost.cc"
    ]
  }]
}
