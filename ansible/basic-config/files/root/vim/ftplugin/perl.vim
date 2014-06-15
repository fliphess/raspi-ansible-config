"vim config for perl files
map bb _i#<ESC>j_
map BB _<DEL><ESC>j_

"abbreviations in Insert mode

" use Getopt::Long and usage() with some default options
iab GETOPT <ESC>:read $HOME/.vim/templates/perl_getopt.pl<cr>

"for doxy comment tak the first sub name and paste after @cmethod
iab DOXY <ESC>/^sub<cr>w"xyiwk:read $HOME/.vim/templates/perl_doxy.pl<cr>/FUNCTION<cr>dw"xpa(\%arg)

iab BYTELOG <ESC>:read $HOME/.vim/templates/perl_bytelog.pl<cr>

iab CLASS <ESC>:read $HOME/.vim/templates/perl_class.pl<cr>

"script header with use strict etc
iab HEADER <ESC>:read $HOME/.vim/templates/perl_header.pl<cr>


