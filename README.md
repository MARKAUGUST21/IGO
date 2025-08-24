# Sistema IGO - Gestão de Produtos

Sistema completo de gestão de produtos desenvolvido em duas versões: Python (orientado a objetos com arquitetura MVC) e C (usando structs e menus interativos).

## 🎯 Funcionalidades

### Autenticação e Controle de Acesso
- **Tela de Login** com diferentes níveis de acesso
- **Níveis de Acesso**: Administrador, Gerente, Vendedor e Cliente
- **Recuperação de Senha** (redefinição simples)

### Cadastros
- **Produtos**: Nome, categoria (roupa/alimento), tamanho, marca, validade (alimentos), quantidade
- **Fornecedores/Doadores**: Informações completas
- **Clientes/Solicitantes**: Dados dos clientes
- **Funcionários**: Cadastro de equipe

### Controle de Estoque
- Visualização de produtos disponíveis
- Atualização de quantidades (entrada e saída)
- Alertas para validade próxima (alimentos)

### Solicitações/Pedidos
- Registro e acompanhamento de pedidos
- Aprovação/rejeição por administrador
- Histórico de pedidos por cliente

### Relatórios
- Entrada e saída de produtos
- Produtos mais solicitados/vendidos
- Relatório de fornecedores/doadores

## 🏗️ Arquitetura

### Versão Python (MVC)
```
python_version/
├── models/          # Modelos de dados
├── views/           # Interfaces de usuário
├── controllers/     # Lógica de negócio
└── main.py         # Arquivo principal
```

### Versão C
```
c_version/
├── main.c          # Arquivo principal
├── models.h        # Definições de structs
├── functions.c     # Implementações das funções
└── Makefile        # Compilação
```

## 🚀 Como Executar

### Versão Python
```bash
cd python_version
python main.py
```

### Versão C
```bash
cd c_version
make
./igo
```

## 👥 Usuários Padrão

| Usuário | Senha | Nível de Acesso |
|---------|-------|------------------|
| admin | admin123 | Administrador |
| gerente | gerente123 | Gerente |
| vendedor | vendedor123 | Vendedor |
| cliente | cliente123 | Cliente |

## 📋 Regras do Sistema

- Interface em terminal (linha de comando)
- Estrutura clara de menus numerados
- Validação de dados (não aceita cadastros vazios)
- Relatórios exibidos diretamente na tela
- Persistência de dados em arquivo JSON (Python) e binário (C)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Orientação a objetos, arquitetura MVC
- **C**: Structs, arrays, funções modulares
- **JSON**: Persistência de dados (Python)
- **Arquivos binários**: Persistência de dados (C)

## 📁 Estrutura do Projeto

```
NP1(SEM2)/
├── README.md
├── python_version/
│   ├── models/
│   │   ├── __init__.py
│   │   └── database.py
│   ├── views/
│   │   └── __init__.py
│   ├── controllers/
│   │   └── __init__.py
│   └── main.py
└── c_version/
    └── (arquivos C serão implementados)
```

## 🔄 Status do Desenvolvimento

- ✅ Estrutura do projeto criada
- ✅ Versão Python iniciada (MVC)
- ✅ Modelo de banco de dados implementado
- 🔄 Controllers e Views em desenvolvimento
- ⏳ Versão C pendente
- ⏳ Testes e validação pendentes

## 👨‍💻 Desenvolvedor

Sistema desenvolvido para a disciplina NP1 (Semestre 2) com foco em programação estruturada e orientada a objetos.
