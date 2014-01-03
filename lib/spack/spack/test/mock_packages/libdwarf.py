from spack import *
import os

# Only build certain parts of dwarf because the other ones break.
dwarf_dirs = ['libdwarf', 'dwarfdump2']

class Libdwarf(Package):
    homepage = "http://www.prevanders.net/dwarf.html"
    url      = "http://www.prevanders.net/libdwarf-20130729.tar.gz"
    list_url = homepage

    versions = { 20130729 : "64b42692e947d5180e162e46c689dfbf",
                 20130207 : 'foobarbaz',
                 20111030 : 'foobarbaz',
                 20070703 : 'foobarbaz' }

    depends_on("libelf")

    def clean(self):
        for dir in dwarf_dirs:
            with working_dir(dir):
                if os.path.exists('Makefile'):
                    make('clean')


    def install(self, spec, prefix):
        # dwarf build does not set arguments for ar properly
        make.add_default_arg('ARFLAGS=rcs')

        # Dwarf doesn't provide an install, so we have to do it.
        mkdirp(prefix.bin, prefix.include, prefix.lib, prefix.man1)

        with working_dir('libdwarf'):
            configure("--prefix=%s" % prefix, '--enable-shared')
            make()

            install('libdwarf.a',  prefix.lib)
            install('libdwarf.so', prefix.lib)
            install('libdwarf.h',  prefix.include)
            install('dwarf.h',     prefix.include)

        with working_dir('dwarfdump2'):
            configure("--prefix=%s" % prefix)

            # This makefile has strings of copy commands that
            # cause a race in parallel
            make(parallel=False)

            install('dwarfdump',      prefix.bin)
            install('dwarfdump.conf', prefix.lib)
            install('dwarfdump.1',    prefix.man1)