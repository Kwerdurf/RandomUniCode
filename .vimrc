set nocompatible              " be iMproved, required
set shell=/bin/bash
syn on
filetype off                  " required
set number                    " turn on numbering
set gdefault                  " search is global by default

packadd termdebug             "add a package to enable gdb usage in vim
"set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'flazz/vim-colorschemes'
Plugin 'scrooloose/nerdtree'
Plugin 'Valloric/YouCompleteMe'
Plugin 'rdnetto/YCM-Generator'
Plugin 'tpope/vim-surround'
Plugin 'jiangmiao/auto-pairs'
Plugin 'oplatek/Conque-Shell'
Plugin 'scrooloose/syntastic'
Plugin 'vim-scripts/taglist.vim'
Plugin 'bling/vim-bufferline'
Plugin 'powerline/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'tpope/vim-fugitive'
call vundle#end()            " required
filetype plugin indent on    " required
"set colorscheme
colorscheme badwolf 
"colorscheme gruvbox
"colorscheme fahrenheit
"colorscheme desertink

"NERDTree config
autocmd vimenter * NERDTree
map <F4> :NERDTreeToggle <CR>
"mapping for tab switching
map <C-Tab> <C-w>w
map <C-S-Tab> <C-w>W
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

"gdb shortcut for c related files
autocmd filetype cpp nnoremap <F6> :Termdebug %:r<CR><c-w>2j<c-w>L
autocmd filetype h  nnoremap <F6> :Termdebug %:r<CR><c-w>2j<c-w>L
autocmd filetype c nnoremap <F6> :Termdebug %:r<CR><c-w>2j<c-w>L

"open a small terminal window at the bottom of the current buffer
nnoremap <F5> :ConqueTermSplit bash<CR><ESC><c-w>13-i<


"YCM Config
let g:ycm_global_ycm_extra_conf = "~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py"
let g:ycm_autoclose_preview_window_after_insertion = 1
let g:ycm_autoclose_preview_window_after_completion = 1

"ConqueTerm Config
let g:ConqueTerm_Color = 2         " 1: strip color after 200 lines, 2: always with color
let g:ConqueTerm_CloseOnEnd = 1    " close conque when program ends running
let g:ConqueTerm_StartMessages = 0 " display warning messages if conqueTerm is configured incorrectly"

"tabs are a bitch
"Use actual tab chars in Makefiles.
"if has("autocmd")
"    autocmd FileType make set tabstop=8 shiftwidth=8 softtabstop=0 noexpandtab
"endif

" For everything else, use a tab width of 4 space chars.
set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
                    " Vim will interpret it to be having
                    " a width of 4.
set shiftwidth=4    " Indents will have a width of 4.
set softtabstop=4   " Sets the number of columns for a TAB.

"python convention is 4 spaces
autocmd filetype python set expandtab

