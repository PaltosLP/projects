set number
set shiftwidth=4

call plug#begin('~/AppData/Local/nvim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'morhetz/gruvbox'
Plug 'joshdick/onedark.vim'

call plug#end()

inoremap jk <ESC>

colorscheme gruvbox
