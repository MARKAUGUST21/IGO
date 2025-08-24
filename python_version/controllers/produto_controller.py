#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Produtos - Sistema IGO
"""

from datetime import datetime, timedelta

class ProdutoController:
    """Controlador responsável pela gestão de produtos"""
    
    def __init__(self, database):
        self.db = database
    
    def menu_produtos(self):
        """Menu de gestão de produtos"""
        while True:
            print("\n" + "=" * 40)
            print("        GESTÃO DE PRODUTOS")
            print("=" * 40)
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("3 - Buscar Produto")
            print("4 - Editar Produto")
            print("5 - Excluir Produto")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_produto()
            elif opcao == "2":
                self.listar_produtos()
            elif opcao == "3":
                self.buscar_produto()
            elif opcao == "4":
                self.editar_produto()
            elif opcao == "5":
                self.excluir_produto()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def cadastrar_produto(self):
        """Cadastra um novo produto"""
        print("\n" + "=" * 40)
        print("        CADASTRO DE PRODUTO")
        print("=" * 40)
        
        # Validação de dados
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        # Categoria
        print("\nCategorias disponíveis:")
        print("1 - Roupa")
        print("2 - Alimento")
        
        categoria_opcao = input("Escolha a categoria (1-2): ").strip()
        if categoria_opcao == "1":
            categoria = "roupa"
        elif categoria_opcao == "2":
            categoria = "alimento"
        else:
            print("❌ Categoria inválida!")
            return
        
        # Tamanho (apenas para roupas)
        tamanho = ""
        if categoria == "roupa":
            print("\nTamanhos disponíveis:")
            print("PP, P, M, G, GG, XG")
            tamanho = input("Tamanho: ").strip().upper()
            if not tamanho:
                print("❌ Tamanho não pode estar vazio!")
                return
        
        # Marca
        marca = input("Marca: ").strip()
        if not marca:
            print("❌ Marca não pode estar vazia!")
            return
        
        # Validade (apenas para alimentos)
        validade = ""
        if categoria == "alimento":
            while True:
                try:
                    data_str = input("Data de validade (DD/MM/AAAA): ").strip()
                    if not data_str:
                        print("❌ Data de validade não pode estar vazia!")
                        continue
                    
                    # Converter para formato YYYY-MM-DD
                    data_parts = data_str.split('/')
                    if len(data_parts) == 3:
                        validade = f"{data_parts[2]}-{data_parts[1]}-{data_parts[0]}"
                        break
                    else:
                        print("❌ Formato de data inválido! Use DD/MM/AAAA")
                except:
                    print("❌ Data inválida!")
                    continue
        
        # Quantidade
        while True:
            try:
                quantidade = int(input("Quantidade inicial: ").strip())
                if quantidade < 0:
                    print("❌ Quantidade não pode ser negativa!")
                    continue
                break
            except ValueError:
                print("❌ Quantidade deve ser um número!")
                continue
        
        # Preço
        while True:
            try:
                preco = float(input("Preço unitário: R$ ").strip())
                if preco < 0:
                    print("❌ Preço não pode ser negativo!")
                    continue
                break
            except ValueError:
                print("❌ Preço deve ser um número!")
                continue
        
        # Criar produto
        produto = {
            "nome": nome,
            "categoria": categoria,
            "tamanho": tamanho,
            "marca": marca,
            "validade": validade,
            "quantidade": quantidade,
            "preco": preco,
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Adicionar ao banco
        novo_produto = self.db.add_item("produtos", produto)
        
        print(f"\n✅ Produto '{novo_produto['nome']}' cadastrado com sucesso!")
        print(f"ID: {novo_produto['id']}")
        
        # Registrar movimentação
        self.registrar_movimentacao("entrada", novo_produto['id'], quantidade, "Cadastro inicial")
    
    def listar_produtos(self):
        """Lista todos os produtos"""
        produtos = self.db.get_items("produtos")
        
        if not produtos:
            print("\n📭 Nenhum produto cadastrado!")
            return
        
        print("\n" + "=" * 80)
        print("                              LISTA DE PRODUTOS")
        print("=" * 80)
        print(f"{'ID':<4} {'Nome':<25} {'Categoria':<10} {'Tamanho':<8} {'Marca':<15} {'Qtd':<4} {'Preço':<8}")
        print("-" * 80)
        
        for produto in produtos:
            tamanho = produto.get('tamanho', 'N/A')
            preco = f"R$ {produto.get('preco', 0):.2f}"
            print(f"{produto['id']:<4} {produto['nome']:<25} {produto['categoria']:<10} {tamanho:<8} {produto['marca']:<15} {produto['quantidade']:<4} {preco:<8}")
        
        print("=" * 80)
        print(f"Total de produtos: {len(produtos)}")
    
    def buscar_produto(self):
        """Busca produto por nome ou ID"""
        print("\n" + "=" * 40)
        print("         BUSCAR PRODUTO")
        print("=" * 40)
        
        termo = input("Digite o nome ou ID do produto: ").strip()
        if not termo:
            print("❌ Termo de busca não pode estar vazio!")
            return
        
        produtos = self.db.get_items("produtos")
        encontrados = []
        
        for produto in produtos:
            # Buscar por ID
            if termo.isdigit() and produto['id'] == int(termo):
                encontrados.append(produto)
            # Buscar por nome
            elif termo.lower() in produto['nome'].lower():
                encontrados.append(produto)
            # Buscar por marca
            elif termo.lower() in produto['marca'].lower():
                encontrados.append(produto)
        
        if not encontrados:
            print("❌ Nenhum produto encontrado!")
            return
        
        print(f"\n🔍 Encontrados {len(encontrados)} produto(s):")
        for produto in encontrados:
            self.exibir_produto_detalhado(produto)
    
    def exibir_produto_detalhado(self, produto):
        """Exibe detalhes de um produto específico"""
        print("\n" + "-" * 50)
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        if produto['categoria'] == 'roupa':
            print(f"Tamanho: {produto.get('tamanho', 'N/A')}")
        print(f"Marca: {produto['marca']}")
        if produto['categoria'] == 'alimento':
            print(f"Validade: {produto.get('validade', 'N/A')}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto.get('preco', 0):.2f}")
        print(f"Data de Cadastro: {produto.get('data_cadastro', 'N/A')}")
        print("-" * 50)
    
    def editar_produto(self):
        """Edita um produto existente"""
        print("\n" + "=" * 40)
        print("         EDITAR PRODUTO")
        print("=" * 40)
        
        produto_id = input("Digite o ID do produto: ").strip()
        if not produto_id or not produto_id.isdigit():
            print("❌ ID inválido!")
            return
        
        produto = self.db.get_item("produtos", int(produto_id))
        if not produto:
            print("❌ Produto não encontrado!")
            return
        
        print(f"\nEditando produto: {produto['nome']}")
        self.exibir_produto_detalhado(produto)
        
        # Campos editáveis
        print("\nDeixe em branco para manter o valor atual:")
        
        nome = input(f"Nome [{produto['nome']}]: ").strip()
        if nome:
            produto['nome'] = nome
        
        marca = input(f"Marca [{produto['marca']}]: ").strip()
        if marca:
            produto['marca'] = marca
        
        if produto['categoria'] == 'roupa':
            tamanho = input(f"Tamanho [{produto.get('tamanho', 'N/A')}]: ").strip()
            if tamanho:
                produto['tamanho'] = tamanho.upper()
        
        if produto['categoria'] == 'alimento':
            validade = input(f"Validade [{produto.get('validade', 'N/A')}]: ").strip()
            if validade:
                produto['validade'] = validade
        
        # Atualizar no banco
        self.db.update_item("produtos", produto['id'], produto)
        print("✅ Produto atualizado com sucesso!")
    
    def excluir_produto(self):
        """Exclui um produto"""
        print("\n" + "=" * 40)
        print("         EXCLUIR PRODUTO")
        print("=" * 40)
        
        produto_id = input("Digite o ID do produto: ").strip()
        if not produto_id or not produto_id.isdigit():
            print("❌ ID inválido!")
            return
        
        produto = self.db.get_item("produtos", int(produto_id))
        if not produto:
            print("❌ Produto não encontrado!")
            return
        
        print(f"\nProduto a ser excluído:")
        self.exibir_produto_detalhado(produto)
        
        confirmacao = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()
        if confirmacao == 's':
            self.db.delete_item("produtos", produto['id'])
            print("✅ Produto excluído com sucesso!")
        else:
            print("❌ Operação cancelada!")
    
    def atualizar_estoque(self):
        """Atualiza a quantidade de um produto"""
        print("\n" + "=" * 40)
        print("      ATUALIZAR ESTOQUE")
        print("=" * 40)
        
        produto_id = input("Digite o ID do produto: ").strip()
        if not produto_id or not produto_id.isdigit():
            print("❌ ID inválido!")
            return
        
        produto = self.db.get_item("produtos", int(produto_id))
        if not produto:
            print("❌ Produto não encontrado!")
            return
        
        print(f"\nProduto: {produto['nome']}")
        print(f"Quantidade atual: {produto['quantidade']}")
        
        print("\nTipo de movimentação:")
        print("1 - Entrada (adicionar)")
        print("2 - Saída (remover)")
        
        tipo = input("Escolha o tipo (1-2): ").strip()
        if tipo not in ['1', '2']:
            print("❌ Tipo inválido!")
            return
        
        while True:
            try:
                quantidade = int(input("Quantidade: ").strip())
                if quantidade <= 0:
                    print("❌ Quantidade deve ser maior que zero!")
                    continue
                break
            except ValueError:
                print("❌ Quantidade deve ser um número!")
                continue
        
        # Calcular nova quantidade
        if tipo == '1':  # Entrada
            nova_quantidade = produto['quantidade'] + quantidade
            tipo_mov = "entrada"
            descricao = f"Entrada de {quantidade} unidades"
        else:  # Saída
            if produto['quantidade'] < quantidade:
                print("❌ Quantidade insuficiente em estoque!")
                return
            nova_quantidade = produto['quantidade'] - quantidade
            tipo_mov = "saida"
            descricao = f"Saída de {quantidade} unidades"
        
        # Atualizar quantidade
        self.db.update_item("produtos", produto['id'], {"quantidade": nova_quantidade})
        
        # Registrar movimentação
        self.registrar_movimentacao(tipo_mov, produto['id'], quantidade, descricao)
        
        print(f"✅ Estoque atualizado! Nova quantidade: {nova_quantidade}")
    
    def produtos_baixo_estoque(self, limite=10):
        """Lista produtos com estoque baixo"""
        produtos = self.db.get_produtos_baixo_estoque(limite)
        
        if not produtos:
            print(f"\n✅ Todos os produtos estão com estoque acima de {limite} unidades!")
            return
        
        print(f"\n⚠️  PRODUTOS COM ESTOQUE BAIXO (≤ {limite} unidades):")
        print("=" * 60)
        
        for produto in produtos:
            print(f"ID: {produto['id']} | {produto['nome']} | Qtd: {produto['quantidade']} | Categoria: {produto['categoria']}")
    
    def produtos_vencendo(self, dias=30):
        """Lista produtos próximos do vencimento"""
        produtos = self.db.get_produtos_vencendo(dias)
        
        if not produtos:
            print(f"\n✅ Nenhum produto vencendo nos próximos {dias} dias!")
            return
        
        print(f"\n⚠️  PRODUTOS VENCENDO NOS PRÓXIMOS {dias} DIAS:")
        print("=" * 60)
        
        for produto in produtos:
            print(f"ID: {produto['id']} | {produto['nome']} | Validade: {produto['validade']} | Qtd: {produto['quantidade']}")
    
    def registrar_movimentacao(self, tipo, produto_id, quantidade, descricao):
        """Registra uma movimentação de estoque"""
        movimentacao = {
            "tipo": tipo,
            "produto_id": produto_id,
            "quantidade": quantidade,
            "descricao": descricao,
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.db.add_item("movimentacoes", movimentacao)
