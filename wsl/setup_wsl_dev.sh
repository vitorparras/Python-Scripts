#!/bin/bash

# Atualização e Limpeza do Sistema
echo "Atualizando e limpando o sistema..."
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y && sudo apt autoclean

# Instalar Pacotes Essenciais
echo "Instalando pacotes essenciais..."
sudo apt install -y build-essential curl wget git unzip zip software-properties-common vim

# Verificar e Instalar Gerenciadores de Pacotes Adicionais
echo "Adicionando repositórios e atualizando lista de pacotes..."
sudo add-apt-repository universe -y
sudo apt update

# Configuração de Sudo sem Senha
echo "Configurando sudo sem senha (opcional)..."
echo "$USER ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/$USER

# Ferramentas Essenciais para Desenvolvimento
echo "Instalando Docker..."
sudo apt install -y docker.io
sudo usermod -aG docker $USER
echo "Reinicie o WSL após este script para ativar permissões Docker sem sudo."

echo "Instalando Python e pip..."
sudo apt install -y python3 python3-pip
pip install virtualenv

echo "Instalando Node.js e npm..."
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
echo "Instalando NVM..."
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

echo "Instalando Git..."
sudo apt install -y git
git config --global user.name "Vitor Parras"
git config --global user.email "vitorhugoparras@hotmail.com"
git config --global core.editor "code --wait" # Configura VS Code como editor padrão do Git

# Instalação de Ferramentas Adicionais
echo "Instalando Jupyter Notebook..."
pip install notebook

echo "Instalando preload para melhorar o desempenho..."
sudo apt install -y preload

# Melhorias no Terminal
echo "Instalando Zsh..."
sudo apt install -y zsh
chsh -s $(which zsh)

echo "Instalando Oh My Zsh..."
RUNZSH=no sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "Instalando plugins do Zsh..."
ZSH_CUSTOM=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting

# Configurando plugins no .zshrc
echo "Configurando plugins no .zshrc..."
sed -i 's/plugins=(git)/plugins=(git docker zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc

echo "Adicionando alias ao .zshrc..."
cat <<EOL >>~/.zshrc

# Alias personalizados
alias ll='ls -la'
alias gs='git status'
alias gd='git diff'
alias docker-clean='docker system prune -af'
alias update='sudo apt update && sudo apt upgrade -y'
EOL
source ~/.zshrc

# Ferramentas de Monitoramento
echo "Instalando ferramentas de monitoramento..."
sudo apt install -y htop ncdu

# Configuração de Notificações de Atualizações Pendentes
echo "Configurando notificações para atualizações pendentes..."
sudo apt install -y update-notifier

# Produtividade no WSL
echo "Configurando WSL para versão 2..."
wsl --set-version Ubuntu-22.04 2

echo "Habilitando systemd no WSL..."
sudo tee /etc/wsl.conf > /dev/null <<EOL
[boot]
systemd=true
EOL
echo "Reinicie o WSL para ativar systemd."

# Extras para Produtividade
echo "Instalando fzf (busca inteligente no terminal)..."
sudo apt install -y fzf

echo "Instalando bat (visualização de arquivos com sintaxe destacada)..."
sudo apt install -y bat
echo "Adicionando alias para bat..."
echo "alias cat='bat'" >>~/.zshrc

echo "Instalando tmux (multiplexador de terminais)..."
sudo apt install -y tmux

# Finalização
echo "Configuração concluída! Reinicie o WSL para ativar todas as alterações."
