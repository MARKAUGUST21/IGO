# 🚀 INSTRUÇÕES DE EXECUÇÃO - SISTEMA IGO

## 📋 Pré-requisitos

- **Python 3.7 ou superior**
- **Sistema operacional**: Windows, macOS ou Linux
- **Terminal/Prompt de comando**

## 🐍 Instalação do Python

### Windows
1. Baixe o Python do site oficial: https://www.python.org/downloads/
2. Durante a instalação, **marque a opção "Add Python to PATH"**
3. Verifique a instalação: `python --version`

### macOS
```bash
# Usando Homebrew
brew install python3

# Verificar instalação
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip

# Verificar instalação
python3 --version
```

## 🎯 Como Executar o Sistema

### 1. Navegar para o diretório
```bash
cd python_version
```

### 2. Executar o sistema principal
```bash
# Windows
python main.py

# macOS/Linux
python3 main.py
```

### 3. Executar teste do sistema (opcional)
```bash
# Windows
python test_sistema.py

# macOS/Linux
python3 test_sistema.py
```

## 🔐 Credenciais de Acesso

O sistema vem com usuários padrão configurados:

| Usuário | Senha | Nível de Acesso |
|---------|-------|-----------------|
| `admin` | `admin123` | Administrador |
| `gerente` | `gerente123` | Gerente |
| `vendedor` | `vendedor123` | Vendedor |
| `cliente` | `cliente123` | Cliente |

## 🎮 Funcionalidades por Nível de Acesso

### 👑 Administrador
- **Acesso total** ao sistema
- Cadastros completos
- Controle de estoque
- Gestão de pedidos
- Relatórios completos
- Configurações do sistema

### 👔 Gerente
- Cadastros
- Controle de estoque
- Gestão de pedidos
- Relatórios
- **NÃO pode** alterar configurações do sistema

### 👨‍💼 Vendedor
- Visualizar produtos
- Atualizar estoque
- Criar pedidos
- Visualizar pedidos

### 👤 Cliente
- Visualizar produtos
- Criar pedidos
- Visualizar seus próprios pedidos

## 🛠️ Estrutura do Projeto

```
python_version/
├── main.py                 # Arquivo principal
├── test_sistema.py         # Arquivo de teste
├── models/
│   ├── __init__.py
│   └── database.py         # Modelo de dados
├── controllers/
│   ├── __init__.py
│   ├── auth_controller.py  # Autenticação
│   ├── main_controller.py  # Controlador principal
│   ├── produto_controller.py # Gestão de produtos
│   ├── fornecedor_controller.py # Gestão de fornecedores
│   ├── cliente_controller.py # Gestão de clientes
│   ├── funcionario_controller.py # Gestão de funcionários
│   ├── pedido_controller.py # Gestão de pedidos
│   └── relatorio_controller.py # Relatórios
├── views/
│   ├── __init__.py
│   └── menu_view.py        # Interface do usuário
└── igo_data.json          # Arquivo de dados (criado automaticamente)
```

## 🔧 Solução de Problemas

### Erro: "Python não foi encontrado"
- **Windows**: Reinstale o Python marcando "Add Python to PATH"
- **macOS/Linux**: Use `python3` em vez de `python`

### Erro de importação
- Certifique-se de estar no diretório `python_version`
- Verifique se todos os arquivos estão presentes

### Erro de permissão
- **Windows**: Execute o terminal como administrador
- **macOS/Linux**: Use `sudo` se necessário

## 📱 Primeiros Passos

1. **Execute o sistema**: `python main.py`
2. **Faça login** com as credenciais padrão
3. **Explore os menus** baseados no seu nível de acesso
4. **Cadastre produtos** para testar o sistema
5. **Crie pedidos** para ver o fluxo completo

## 🎯 Funcionalidades Principais

### 📦 Gestão de Produtos
- Cadastro de produtos (roupas e alimentos)
- Controle de estoque
- Alertas de estoque baixo
- Alertas de produtos vencendo (alimentos)

### 👥 Gestão de Pessoas
- Fornecedores
- Clientes
- Funcionários
- Usuários do sistema

### 📋 Gestão de Pedidos
- Criação de pedidos
- Aprovação/rejeição
- Histórico completo
- Atualização automática de estoque

### 📊 Relatórios
- Estoque atual
- Movimentações
- Produtos mais solicitados
- Estatísticas gerais

## 🚨 Dicas Importantes

- **Sempre confirme** antes de excluir registros
- **Use a busca** para encontrar itens rapidamente
- **Verifique o estoque** antes de criar pedidos
- **Faça backup** do arquivo `igo_data.json` regularmente
- **Use Ctrl+C** para sair em emergência

## 📞 Suporte

Se encontrar problemas:
1. Execute `python test_sistema.py` para diagnóstico
2. Verifique se está no diretório correto
3. Confirme se o Python está instalado e no PATH
4. Verifique se todos os arquivos estão presentes

## 🎉 Parabéns!

Você agora tem um sistema completo de gestão de produtos funcionando com arquitetura MVC! 

**Próximos passos sugeridos:**
- Teste todas as funcionalidades
- Cadastre produtos de exemplo
- Crie pedidos de teste
- Explore os relatórios
- Personalize conforme suas necessidades

---

**Sistema IGO - Versão 1.0.0**  
**Desenvolvido para NP1 (Semestre 2)**  
**Arquitetura: Model-View-Controller (MVC)**
