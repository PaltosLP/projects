# hello-world
First Repository


WSL Notes:

Windows Terminal
https://github.com/ohmyzsh/ohmyzsh
p10k --> git clone --depth=1 https://github.com/romkatv/powerlevel10k.git 
${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k

Updating Neovim:
  https://ecalzo.is-a.dev/Nvim-on-WSL2/

Vim Plug:
  sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
       
sudo apt install nodejs 

sudo apt install npm

Transparency: CRTL + SHIFT + Scroll Up/Down

packer:
  git clone --depth 1 https://github.com/wbthomason/packer.nvim\
 ~/.local/share/nvim/site/pack/packer/start/packer.nvim

Color Mixer:
  http://spectrumcolors.de/cor_rgb_demo.php

MatPlotLib in WSL:
  https://stackoverflow.com/questions/43397162/show-matplotlib-plots-and-other-gui-in-ubuntu-wsl1-wsl2
