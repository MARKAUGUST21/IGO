#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador Principal - Sistema IGO
"""

from datetime import datetime
from controllers.produto_controller import ProdutoController
from controllers.fornecedor_controller import FornecedorController
from controllers.cliente_controller import ClienteController
from controllers.funcionario_controller import FuncionarioController
from controllers.pedido_controller import PedidoController
from controllers.relatorio_controller import RelatorioController

class MainController:
    """Controlador principal que gerencia todos os menus e funcionalidades"""
    
    def __init__(self, database):
        self.db = database
        self.produto_controller = ProdutoController(database)
        self.fornecedor_controller = FornecedorController(database)
        self.cliente_controller = ClienteController(database)
        self.funcionario_controller = FuncionarioController(database)
        self.pedido_controller = PedidoController(database)
        self.relatorio_controller = RelatorioController(database)
    
    def show_main_menu(self, nivel_acesso):
        """Exibe o menu principal baseado no nível de acesso"""
        while True:
            try:
                print("\n" + "=" * 50)
                print("           MENU PRINCIPAL - IGO")
                print("=" * 50)
                
                # Menu baseado no nível de acesso
                if nivel_acesso == "administrador":
                    self.show_admin_menu()
                elif nivel_acesso == "gerente":
                    self.show_gerente_menu()
                elif nivel_acesso == "vendedor":
                    self.show_vendedor_menu()
                elif nivel_acesso == "cliente":
                    self.show_cliente_menu()
                else:
                    print("❌ Nível de acesso inválido!")
                    break
                    
            except KeyboardInterrupt:
                print("\n\nSaindo do sistema...")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")
                continue
    
    def show_admin_menu(self):
        """Menu para administradores"""
        print("1 - Cadastros")
        print("2 - Controle de Estoque")
        print("3 - Pedidos")
        print("4 - Relatórios")
        print("5 - Configurações do Sistema")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.show_cadastros_menu()
        elif opcao == "2":
            self.show_estoque_menu()
        elif opcao == "3":
            self.show_pedidos_menu()
        elif opcao == "4":
            self.show_relatorios_menu()
        elif opcao == "5":
            self.show_configuracoes_menu()
        elif opcao == "0":
            raise KeyboardInterrupt
        else:
            print("❌ Opção inválida!")
    
    def show_gerente_menu(self):
        """Menu para gerentes"""
        print("1 - Cadastros")
        print("2 - Controle de Estoque")
        print("3 - Pedidos")
        print("4 - Relatórios")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.show_cadastros_menu()
        elif opcao == "2":
            self.show_estoque_menu()
        elif opcao == "3":
            self.show_pedidos_menu()
        elif opcao == "4":
            self.show_relatorios_menu()
        elif opcao == "0":
            raise KeyboardInterrupt
        else:
            print("❌ Opção inválida!")
    
    def show_vendedor_menu(self):
        """Menu para vendedores"""
        print("1 - Visualizar Produtos")
        print("2 - Atualizar Estoque")
        print("3 - Criar Pedidos")
        print("4 - Visualizar Pedidos")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.produto_controller.listar_produtos()
        elif opcao == "2":
            self.produto_controller.atualizar_estoque()
        elif opcao == "3":
            self.pedido_controller.criar_pedido()
        elif opcao == "4":
            self.pedido_controller.listar_pedidos()
        elif opcao == "0":
            raise KeyboardInterrupt
        else:
            print("❌ Opção inválida!")
    
    def show_cliente_menu(self):
        """Menu para clientes"""
        print("1 - Visualizar Produtos")
        print("2 - Criar Pedido")
        print("3 - Meus Pedidos")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            self.produto_controller.listar_produtos()
        elif opcao == "2":
            self.pedido_controller.criar_pedido()
        elif opcao == "3":
            self.pedido_controller.listar_meus_pedidos()
        elif opcao == "0":
            raise KeyboardInterrupt
        else:
            print("❌ Opção inválida!")
    
    def show_cadastros_menu(self):
        """Menu de cadastros"""
        while True:
            print("\n" + "=" * 40)
            print("           MENU CADASTROS")
            print("=" * 40)
            print("1 - Produtos")
            print("2 - Fornecedores")
            print("3 - Clientes")
            print("4 - Funcionários")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.produto_controller.menu_produtos()
            elif opcao == "2":
                self.fornecedor_controller.menu_fornecedores()
            elif opcao == "3":
                self.cliente_controller.menu_clientes()
            elif opcao == "4":
                self.funcionario_controller.menu_funcionarios()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def show_estoque_menu(self):
        """Menu de controle de estoque"""
        while True:
            print("\n" + "=" * 40)
            print("        CONTROLE DE ESTOQUE")
            print("=" * 40)
            print("1 - Visualizar Produtos")
            print("2 - Adicionar Produto")
            print("3 - Atualizar Quantidade")
            print("4 - Produtos com Baixo Estoque")
            print("5 - Produtos Vencendo")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.produto_controller.listar_produtos()
            elif opcao == "2":
                self.produto_controller.cadastrar_produto()
            elif opcao == "3":
                self.produto_controller.atualizar_estoque()
            elif opcao == "4":
                self.produto_controller.produtos_baixo_estoque()
            elif opcao == "5":
                self.produto_controller.produtos_vencendo()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def show_pedidos_menu(self):
        """Menu de pedidos"""
        while True:
            print("\n" + "=" * 40)
            print("           MENU PEDIDOS")
            print("=" * 40)
            print("1 - Criar Pedido")
            print("2 - Listar Pedidos")
            print("3 - Aprovar/Rejeitar Pedidos")
            print("4 - Histórico de Pedidos")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.pedido_controller.criar_pedido()
            elif opcao == "2":
                self.pedido_controller.listar_pedidos()
            elif opcao == "3":
                self.pedido_controller.aprovar_pedidos()
            elif opcao == "4":
                self.pedido_controller.historico_pedidos()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def show_relatorios_menu(self):
        """Menu de relatórios"""
        while True:
            print("\n" + "=" * 40)
            print("          MENU RELATÓRIOS")
            print("=" * 40)
            print("1 - Relatório de Estoque")
            print("2 - Relatório de Movimentações")
            print("3 - Produtos Mais Solicitados")
            print("4 - Relatório de Fornecedores")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.relatorio_controller.relatorio_estoque()
            elif opcao == "2":
                self.relatorio_controller.relatorio_movimentacoes()
            elif opcao == "3":
                self.relatorio_controller.relatorio_produtos_solicitados()
            elif opcao == "4":
                self.relatorio_controller.relatorio_fornecedores()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def show_configuracoes_menu(self):
        """Menu de configurações do sistema"""
        print("\n" + "=" * 40)
        print("      CONFIGURAÇÕES DO SISTEMA")
        print("=" * 40)
        print("1 - Alterar Senha")
        print("2 - Backup do Sistema")
        print("3 - Restaurar Sistema")
        print("0 - Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            # Implementar alteração de senha
            print("🔧 Funcionalidade em desenvolvimento...")
        elif opcao == "2":
            print("🔧 Funcionalidade em desenvolvimento...")
        elif opcao == "3":
            print("🔧 Funcionalidade em desenvolvimento...")
        elif opcao == "0":
            return
        else:
            print("❌ Opção inválida!")
