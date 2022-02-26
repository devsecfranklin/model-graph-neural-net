dnl Process this file with autoconf
AC_PREREQ([2.69])
AC_INIT(model-graph-neural-net, 0.1, franklin@bitsmasher.net, https://github.com/devsecfranklin/model-graph-neural-net)
AC_CONFIG_MACRO_DIR(config/m4)
AC_CONFIG_AUX_DIR(config)
AM_INIT_AUTOMAKE

LT_INIT

AC_CONFIG_COMMANDS([franklin-build],
 [echo "(⊃｡•́‿•̀｡)⊃━⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿ Configuring for $mypkgname ☽༓･*˚⁺‧͙"],
 [mypkgname=$PACKAGE_NAME])
AC_CONFIG_FILES([cluster/Makefile
                 paper/Makefile 
                 presentation/Makefile]) # Makefiles to generate, one per line

AM_PATH_PYTHON(3.8) # minimum version of Python
PY39="python$PYTHON_VERSION" # define the python interpreter
dnl LDFLAGS="$LDFLAGS -l$PY39"
AC_SUBST(PY39, python$PYTHON_VERSION)

AC_LATEX_CLASS_ARTICLE
AC_LATEX_CLASS_BOOK
AC_LATEX_CLASS_REPORT
AC_LATEX_PACKAGE_AMSMATH
AC_LATEX_PACKAGE_FONTENC
AC_PROG_DVIPDF
AC_PROG_DVIPS
AC_PROG_FIG2DEV
AC_PROG_GNUPLOT
AC_PROG_MF
AC_PROG_LATEX
AC_PROG_BIBTEX
AC_PROG_PDFLATEX
AC_PROG_PS2PDF
dnl AC_PROG_LATEX2HTML
dnl AC_PROG_LATEX2MAN
AC_PROG_MAKEINDEX
dnl AC_PROG_JPEG2PS
AC_PROG_MKTEXPK
AC_PROG_TEXHASH
AC_PROG_KPSEWHICH
dnl AC_TEXMF_PATH
AC_PROG_PNGTOPNM
AC_PROG_PNMTOPS
AC_PROG_JPEGTOPNM
dnl AC_PROG_LATEX2PNG
dnl AC_PROG_LATEX2RTF
AC_PROG_PSBOOK
AC_PROG_PSNUP
AC_PROG_PSSELECT
AC_PROG_PSRESIZE
AC_PROG_DVIBOOK

AC_OUTPUT
