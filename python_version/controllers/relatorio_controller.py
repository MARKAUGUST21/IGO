#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Relatórios - Sistema IGO
"""

from datetime import datetime

class RelatorioController:
    """Controlador responsável pela geração de relatórios"""
    
    def __init__(self, database):
        self.db = database
    
    def relatorio_estoque(self):
        """Gera relatório de estoque"""
        print("\n" + "=" * 60)
        print("                    RELATÓRIO DE ESTOQUE")
        print("=" * 60)
        
        produtos = self.db.get_items("produtos")
        if not produtos:
            print("📭 Nenhum produto cadastrado!")
            return
        
        # Estatísticas
        total_produtos = len(produtos)
        total_valor = sum(p.get('preco', 0) * p['quantidade'] for p in produtos)
        produtos_roupa = len([p for p in produtos if p['categoria'] == 'roupa'])
        produtos_alimento = len([p for p in produtos if p['categoria'] == 'alimento'])
        
        print(f"Total de Produtos: {total_produtos}")
        print(f"Valor Total em Estoque: R$ {total_valor:.2f}")
        print(f"Produtos de Roupa: {produtos_roupa}")
        print(f"Produtos Alimentícios: {produtos_alimento}")
        
        # Produtos por categoria
        print("\n" + "-" * 60)
        print("PRODUTOS POR CATEGORIA:")
        print("-" * 60)
        
        categorias = {}
        for produto in produtos:
            cat = produto['categoria']
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(produto)
        
        for categoria, prods in categorias.items():
            print(f"\n{categoria.upper()}:")
            print(f"{'ID':<4} {'Nome':<25} {'Qtd':<4} {'Preço':<8} {'Valor Total':<12}")
            print("-" * 60)
            
            for produto in prods:
                preco = f"R$ {produto.get('preco', 0):.2f}"
                valor_total = f"R$ {(produto.get('preco', 0) * produto['quantidade']):.2f}"
                print(f"{produto['id']:<4} {produto['nome']:<25} {produto['quantidade']:<4} {preco:<8} {valor_total:<12}")
        
        print("\n" + "=" * 60)
    
    def relatorio_movimentacoes(self):
        """Gera relatório de movimentações"""
        print("\n" + "=" * 60)
        print("                RELATÓRIO DE MOVIMENTAÇÕES")
        print("=" * 60)
        
        movimentacoes = self.db.get_items("movimentacoes")
        if not movimentacoes:
            print("📭 Nenhuma movimentação registrada!")
            return
        
        # Estatísticas
        entradas = [m for m in movimentacoes if m['tipo'] == 'entrada']
        saidas = [m for m in movimentacoes if m['tipo'] == 'saida']
        
        print(f"Total de Movimentações: {len(movimentacoes)}")
        print(f"Entradas: {len(entradas)}")
        print(f"Saídas: {len(saidas)}")
        
        # Últimas movimentações
        print("\n" + "-" * 60)
        print("ÚLTIMAS MOVIMENTAÇÕES:")
        print("-" * 60)
        print(f"{'Data/Hora':<20} {'Tipo':<8} {'Produto ID':<12} {'Qtd':<4} {'Descrição':<30}")
        print("-" * 60)
        
        # Ordenar por data (mais recentes primeiro)
        movimentacoes_ordenadas = sorted(movimentacoes, key=lambda x: x['data_hora'], reverse=True)
        
        for mov in movimentacoes_ordenadas[:20]:  # Últimas 20
            data = mov['data_hora'][:19]  # Formato mais legível
            print(f"{data:<20} {mov['tipo']:<8} {mov['produto_id']:<12} {mov['quantidade']:<4} {mov['descricao']:<30}")
        
        print("\n" + "=" * 60)
    
    def relatorio_produtos_solicitados(self):
        """Gera relatório dos produtos mais solicitados"""
        print("\n" + "=" * 60)
        print("              PRODUTOS MAIS SOLICITADOS")
        print("=" * 60)
        
        pedidos = self.db.get_items("pedidos", {"status": "aprovado"})
        if not pedidos:
            print("📭 Nenhum pedido aprovado encontrado!")
            return
        
        # Contar produtos solicitados
        contagem_produtos = {}
        for pedido in pedidos:
            for item in pedido['itens']:
                produto_id = item['produto_id']
                if produto_id not in contagem_produtos:
                    contagem_produtos[produto_id] = {
                        'nome': item['nome_produto'],
                        'quantidade_total': 0,
                        'pedidos': 0
                    }
                contagem_produtos[produto_id]['quantidade_total'] += item['quantidade']
                contagem_produtos[produto_id]['pedidos'] += 1
        
        # Ordenar por quantidade
        produtos_ordenados = sorted(contagem_produtos.items(), 
                                  key=lambda x: x[1]['quantidade_total'], 
                                  reverse=True)
        
        print(f"{'Rank':<4} {'Produto':<25} {'Qtd Total':<12} {'Pedidos':<8}")
        print("-" * 60)
        
        for i, (produto_id, dados) in enumerate(produtos_ordenados[:10], 1):  # Top 10
            print(f"{i:<4} {dados['nome']:<25} {dados['quantidade_total']:<12} {dados['pedidos']:<8}")
        
        print("\n" + "=" * 60)
    
    def relatorio_fornecedores(self):
        """Gera relatório de fornecedores"""
        print("\n" + "=" * 60)
        print("                 RELATÓRIO DE FORNECEDORES")
        print("=" * 60)
        
        fornecedores = self.db.get_items("fornecedores")
        if not fornecedores:
            print("📭 Nenhum fornecedor cadastrado!")
            return
        
        print(f"Total de Fornecedores: {len(fornecedores)}")
        
        # Fornecedores por região (baseado no endereço)
        regioes = {}
        for fornecedor in fornecedores:
            endereco = fornecedor['endereco']
            if endereco:
                # Extrair cidade/estado do endereço
                partes = endereco.split(',')
                if len(partes) >= 2:
                    regiao = partes[-1].strip()
                else:
                    regiao = "Não informado"
            else:
                regiao = "Não informado"
            
            if regiao not in regioes:
                regioes[regiao] = []
            regioes[regiao].append(fornecedor)
        
        print("\n" + "-" * 60)
        print("FORNECEDORES POR REGIÃO:")
        print("-" * 60)
        
        for regiao, fornecedores_regiao in regioes.items():
            print(f"\n{regiao.upper()}: {len(fornecedores_regiao)} fornecedor(es)")
            print(f"{'ID':<4} {'Nome':<30} {'CNPJ':<18} {'Telefone':<15}")
            print("-" * 60)
            
            for fornecedor in fornecedores_regiao:
                print(f"{fornecedor['id']:<4} {fornecedor['nome']:<30} {fornecedor['cnpj']:<18} {fornecedor['telefone']:<15}")
        
        print("\n" + "=" * 60)
    
    def relatorio_geral(self):
        """Gera relatório geral do sistema"""
        print("\n" + "=" * 60)
        print("                    RELATÓRIO GERAL - IGO")
        print("=" * 60)
        
        # Contadores
        produtos = self.db.get_items("produtos")
        fornecedores = self.db.get_items("fornecedores")
        clientes = self.db.get_items("clientes")
        funcionarios = self.db.get_items("funcionarios")
        pedidos = self.db.get_items("pedidos")
        usuarios = self.db.get_items("usuarios")
        
        print(f"📊 ESTATÍSTICAS GERAIS:")
        print(f"   • Produtos: {len(produtos)}")
        print(f"   • Fornecedores: {len(fornecedores)}")
        print(f"   • Clientes: {len(clientes)}")
        print(f"   • Funcionários: {len(funcionarios)}")
        print(f"   • Pedidos: {len(pedidos)}")
        print(f"   • Usuários: {len(usuarios)}")
        
        # Status dos pedidos
        if pedidos:
            pedidos_pendentes = len([p for p in pedidos if p['status'] == 'pendente'])
            pedidos_aprovados = len([p for p in pedidos if p['status'] == 'aprovado'])
            pedidos_rejeitados = len([p for p in pedidos if p['status'] == 'rejeitado'])
            
            print(f"\n📋 STATUS DOS PEDIDOS:")
            print(f"   • Pendentes: {pedidos_pendentes}")
            print(f"   • Aprovados: {pedidos_aprovados}")
            print(f"   • Rejeitados: {pedidos_rejeitados}")
        
        # Produtos por categoria
        if produtos:
            categorias = {}
            for produto in produtos:
                cat = produto['categoria']
                if cat not in categorias:
                    categorias[cat] = 0
                categorias[cat] += 1
            
            print(f"\n🏷️  PRODUTOS POR CATEGORIA:")
            for categoria, quantidade in categorias.items():
                print(f"   • {categoria.title()}: {quantidade}")
        
        # Valor total em estoque
        if produtos:
            valor_total = sum(p.get('preco', 0) * p['quantidade'] for p in produtos)
            print(f"\n💰 VALOR TOTAL EM ESTOQUE: R$ {valor_total:.2f}")
        
        print("\n" + "=" * 60)
        print(f"Relatório gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}")
        print("=" * 60)
