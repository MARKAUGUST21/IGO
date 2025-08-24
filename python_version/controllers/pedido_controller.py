#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Pedidos - Sistema IGO
"""

from datetime import datetime

class PedidoController:
    """Controlador responsável pela gestão de pedidos"""
    
    def __init__(self, database):
        self.db = database
    
    def criar_pedido(self):
        """Cria um novo pedido"""
        print("\n" + "=" * 40)
        print("         CRIAR PEDIDO")
        print("=" * 40)
        
        # Selecionar cliente
        cliente_id = input("ID do cliente: ").strip()
        if not cliente_id or not cliente_id.isdigit():
            print("❌ ID do cliente inválido!")
            return
        
        cliente = self.db.get_item("clientes", int(cliente_id))
        if not cliente:
            print("❌ Cliente não encontrado!")
            return
        
        print(f"Cliente: {cliente['nome']}")
        
        # Listar produtos disponíveis
        produtos = self.db.get_items("produtos")
        if not produtos:
            print("❌ Nenhum produto disponível!")
            return
        
        print("\nProdutos disponíveis:")
        print(f"{'ID':<4} {'Nome':<25} {'Qtd':<4} {'Preço':<8}")
        print("-" * 50)
        
        for produto in produtos:
            if produto['quantidade'] > 0:
                preco = f"R$ {produto.get('preco', 0):.2f}"
                print(f"{produto['id']:<4} {produto['nome']:<25} {produto['quantidade']:<4} {preco:<8}")
        
        # Itens do pedido
        itens = []
        total = 0.0
        
        while True:
            produto_id = input("\nID do produto (0 para finalizar): ").strip()
            if produto_id == "0":
                break
            
            if not produto_id or not produto_id.isdigit():
                print("❌ ID inválido!")
                continue
            
            produto = self.db.get_item("produtos", int(produto_id))
            if not produto:
                print("❌ Produto não encontrado!")
                continue
            
            if produto['quantidade'] <= 0:
                print("❌ Produto sem estoque!")
                continue
            
            while True:
                try:
                    quantidade = int(input(f"Quantidade (máx: {produto['quantidade']}): ").strip())
                    if quantidade <= 0:
                        print("❌ Quantidade deve ser maior que zero!")
                        continue
                    if quantidade > produto['quantidade']:
                        print("❌ Quantidade insuficiente em estoque!")
                        continue
                    break
                except ValueError:
                    print("❌ Quantidade deve ser um número!")
                    continue
            
            preco_unitario = produto.get('preco', 0)
            subtotal = preco_unitario * quantidade
            total += subtotal
            
            item = {
                "produto_id": produto['id'],
                "nome_produto": produto['nome'],
                "quantidade": quantidade,
                "preco_unitario": preco_unitario,
                "subtotal": subtotal
            }
            
            itens.append(item)
            print(f"✅ {produto['nome']} x{quantidade} = R$ {subtotal:.2f}")
        
        if not itens:
            print("❌ Pedido sem itens!")
            return
        
        # Criar pedido
        pedido = {
            "cliente_id": cliente['id'],
            "cliente_nome": cliente['nome'],
            "itens": itens,
            "total": total,
            "status": "pendente",
            "data_pedido": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data_aprovacao": None,
            "observacoes": input("Observações (opcional): ").strip()
        }
        
        novo_pedido = self.db.add_item("pedidos", pedido)
        print(f"\n✅ Pedido criado com sucesso!")
        print(f"ID do Pedido: {novo_pedido['id']}")
        print(f"Total: R$ {total:.2f}")
        print(f"Status: {novo_pedido['status']}")
    
    def listar_pedidos(self):
        """Lista todos os pedidos"""
        pedidos = self.db.get_items("pedidos")
        
        if not pedidos:
            print("\n📭 Nenhum pedido encontrado!")
            return
        
        print("\n" + "=" * 80)
        print("                              LISTA DE PEDIDOS")
        print("=" * 80)
        print(f"{'ID':<4} {'Cliente':<25} {'Total':<10} {'Status':<12} {'Data':<20}")
        print("-" * 80)
        
        for pedido in pedidos:
            data = pedido['data_pedido'][:10]  # Apenas a data
            total = f"R$ {pedido['total']:.2f}"
            print(f"{pedido['id']:<4} {pedido['cliente_nome']:<25} {total:<10} {pedido['status']:<12} {data:<20}")
        
        print("=" * 80)
        print(f"Total de pedidos: {len(pedidos)}")
    
    def listar_meus_pedidos(self):
        """Lista pedidos do cliente logado"""
        print("\n" + "=" * 40)
        print("         MEUS PEDIDOS")
        print("=" * 40)
        
        cliente_id = input("Digite seu ID de cliente: ").strip()
        if not cliente_id or not cliente_id.isdigit():
            print("❌ ID inválido!")
            return
        
        pedidos = self.db.get_items("pedidos", {"cliente_id": int(cliente_id)})
        
        if not pedidos:
            print("📭 Nenhum pedido encontrado!")
            return
        
        print(f"\nSeus pedidos:")
        for pedido in pedidos:
            self.exibir_pedido_detalhado(pedido)
    
    def exibir_pedido_detalhado(self, pedido):
        """Exibe detalhes de um pedido"""
        print("\n" + "=" * 60)
        print(f"Pedido #{pedido['id']}")
        print(f"Cliente: {pedido['cliente_nome']}")
        print(f"Data: {pedido['data_pedido']}")
        print(f"Status: {pedido['status']}")
        print(f"Total: R$ {pedido['total']:.2f}")
        
        if pedido.get('observacoes'):
            print(f"Observações: {pedido['observacoes']}")
        
        print("\nItens:")
        print(f"{'Produto':<25} {'Qtd':<4} {'Preço':<8} {'Subtotal':<10}")
        print("-" * 50)
        
        for item in pedido['itens']:
            preco = f"R$ {item['preco_unitario']:.2f}"
            subtotal = f"R$ {item['subtotal']:.2f}"
            print(f"{item['nome_produto']:<25} {item['quantidade']:<4} {preco:<8} {subtotal:<10}")
        
        print("=" * 60)
    
    def aprovar_pedidos(self):
        """Aprova ou rejeita pedidos pendentes"""
        pedidos = self.db.get_items("pedidos", {"status": "pendente"})
        
        if not pedidos:
            print("\n✅ Nenhum pedido pendente para aprovação!")
            return
        
        print("\n" + "=" * 40)
        print("      APROVAR/REJEITAR PEDIDOS")
        print("=" * 40)
        
        for pedido in pedidos:
            print(f"\nPedido #{pedido['id']} - {pedido['cliente_nome']}")
            print(f"Total: R$ {pedido['total']:.2f}")
            
            acao = input("Aprovar (a) ou Rejeitar (r)? ").strip().lower()
            
            if acao == 'a':
                # Aprovar pedido
                self.db.update_item("pedidos", pedido['id'], {
                    "status": "aprovado",
                    "data_aprovacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                # Atualizar estoque
                for item in pedido['itens']:
                    produto = self.db.get_item("produtos", item['produto_id'])
                    if produto:
                        nova_quantidade = produto['quantidade'] - item['quantidade']
                        self.db.update_item("produtos", produto['id'], {"quantidade": nova_quantidade})
                
                print("✅ Pedido aprovado e estoque atualizado!")
                
            elif acao == 'r':
                # Rejeitar pedido
                motivo = input("Motivo da rejeição: ").strip()
                self.db.update_item("pedidos", pedido['id'], {
                    "status": "rejeitado",
                    "observacoes": f"Rejeitado: {motivo}"
                })
                print("❌ Pedido rejeitado!")
            
            else:
                print("⚠️  Ação ignorada!")
    
    def historico_pedidos(self):
        """Exibe histórico de pedidos"""
        print("\n" + "=" * 40)
        print("       HISTÓRICO DE PEDIDOS")
        print("=" * 40)
        
        # Filtros
        print("Filtros:")
        print("1 - Todos")
        print("2 - Aprovados")
        print("3 - Rejeitados")
        print("4 - Pendentes")
        
        filtro = input("Escolha o filtro (1-4): ").strip()
        
        if filtro == "1":
            pedidos = self.db.get_items("pedidos")
        elif filtro == "2":
            pedidos = self.db.get_items("pedidos", {"status": "aprovado"})
        elif filtro == "3":
            pedidos = self.db.get_items("pedidos", {"status": "rejeitado"})
        elif filtro == "4":
            pedidos = self.db.get_items("pedidos", {"status": "pendente"})
        else:
            print("❌ Filtro inválido!")
            return
        
        if not pedidos:
            print("📭 Nenhum pedido encontrado!")
            return
        
        print(f"\nEncontrados {len(pedidos)} pedido(s):")
        for pedido in pedidos:
            self.exibir_pedido_detalhado(pedido)
