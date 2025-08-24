#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
View do Menu - Sistema IGO
"""

class MenuView:
    """Classe responsável pela interface de usuário dos menus"""
    
    def __init__(self):
        pass
    
    def mostrar_cabecalho(self, titulo):
        """Exibe cabeçalho padronizado"""
        print("\n" + "=" * 60)
        print(f"                    {titulo}")
        print("=" * 60)
    
    def mostrar_rodape(self):
        """Exibe rodapé padronizado"""
        print("=" * 60)
        print("Pressione ENTER para continuar...")
        input()
    
    def mostrar_erro(self, mensagem):
        """Exibe mensagem de erro padronizada"""
        print(f"\n❌ ERRO: {mensagem}")
    
    def mostrar_sucesso(self, mensagem):
        """Exibe mensagem de sucesso padronizada"""
        print(f"\n✅ {mensagem}")
    
    def mostrar_aviso(self, mensagem):
        """Exibe mensagem de aviso padronizada"""
        print(f"\n⚠️  {mensagem}")
    
    def mostrar_info(self, mensagem):
        """Exibe mensagem informativa padronizada"""
        print(f"\nℹ️  {mensagem}")
    
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_progresso(self, mensagem, valor_atual, valor_total):
        """Exibe barra de progresso"""
        percentual = int((valor_atual / valor_total) * 100)
        barra = "█" * (percentual // 5) + "░" * (20 - (percentual // 5))
        print(f"\r{mensagem}: [{barra}] {percentual}%", end="", flush=True)
        
        if valor_atual == valor_total:
            print()  # Nova linha quando completar
    
    def confirmar_acao(self, mensagem):
        """Solicita confirmação do usuário"""
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        return resposta in ['s', 'sim', 'y', 'yes']
    
    def selecionar_opcao(self, opcoes, mensagem="Escolha uma opção"):
        """Permite seleção de opção com validação"""
        while True:
            print(f"\n{mensagem}:")
            for i, opcao in enumerate(opcoes, 1):
                print(f"{i} - {opcao}")
            print("0 - Cancelar")
            
            try:
                escolha = int(input("\nOpção: ").strip())
                if escolha == 0:
                    return None
                if 1 <= escolha <= len(opcoes):
                    return escolha - 1
                else:
                    self.mostrar_erro("Opção inválida!")
            except ValueError:
                self.mostrar_erro("Digite um número válido!")
    
    def mostrar_tabela(self, dados, colunas, titulo="TABELA"):
        """Exibe dados em formato de tabela"""
        if not dados:
            print(f"\n📭 Nenhum {titulo.lower()} encontrado!")
            return
        
        # Calcular larguras das colunas
        larguras = []
        for i, coluna in enumerate(colunas):
            largura = len(coluna)
            for dado in dados:
                if isinstance(dado, dict) and coluna in dado:
                    largura = max(largura, len(str(dado[coluna])))
            larguras.append(largura)
        
        # Cabeçalho
        linha_cabecalho = " | ".join(f"{coluna:<{larguras[i]}}" for i, coluna in enumerate(colunas))
        largura_total = len(linha_cabecalho)
        
        print(f"\n{titulo}")
        print("=" * largura_total)
        print(linha_cabecalho)
        print("-" * largura_total)
        
        # Dados
        for dado in dados:
            linha = " | ".join(f"{str(dado.get(coluna, '')):<{larguras[i]}}" for i, coluna in enumerate(colunas))
            print(linha)
        
        print("=" * largura_total)
        print(f"Total: {len(dados)} registro(s)")
    
    def mostrar_menu_principal(self, nivel_acesso):
        """Exibe menu principal baseado no nível de acesso"""
        self.mostrar_cabecalho("MENU PRINCIPAL - SISTEMA IGO")
        
        print(f"Nível de Acesso: {nivel_acesso.upper()}")
        print(f"Data/Hora: {self.obter_data_hora_atual()}")
        
        if nivel_acesso == "administrador":
            self.mostrar_menu_admin()
        elif nivel_acesso == "gerente":
            self.mostrar_menu_gerente()
        elif nivel_acesso == "vendedor":
            self.mostrar_menu_vendedor()
        elif nivel_acesso == "cliente":
            self.mostrar_menu_cliente()
        else:
            self.mostrar_erro("Nível de acesso inválido!")
    
    def mostrar_menu_admin(self):
        """Exibe menu para administradores"""
        print("\n1 - Cadastros")
        print("2 - Controle de Estoque")
        print("3 - Pedidos")
        print("4 - Relatórios")
        print("5 - Configurações do Sistema")
        print("6 - Relatório Geral")
        print("0 - Sair")
    
    def mostrar_menu_gerente(self):
        """Exibe menu para gerentes"""
        print("\n1 - Cadastros")
        print("2 - Controle de Estoque")
        print("3 - Pedidos")
        print("4 - Relatórios")
        print("5 - Relatório Geral")
        print("0 - Sair")
    
    def mostrar_menu_vendedor(self):
        """Exibe menu para vendedores"""
        print("\n1 - Visualizar Produtos")
        print("2 - Atualizar Estoque")
        print("3 - Criar Pedidos")
        print("4 - Visualizar Pedidos")
        print("0 - Sair")
    
    def mostrar_menu_cliente(self):
        """Exibe menu para clientes"""
        print("\n1 - Visualizar Produtos")
        print("2 - Criar Pedido")
        print("3 - Meus Pedidos")
        print("0 - Sair")
    
    def obter_data_hora_atual(self):
        """Retorna data e hora atual formatada"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    
    def mostrar_ajuda(self):
        """Exibe tela de ajuda"""
        self.mostrar_cabecalho("AJUDA - SISTEMA IGO")
        
        print("📖 COMO USAR O SISTEMA:")
        print("\n1. LOGIN:")
        print("   • Digite seu usuário e senha")
        print("   • Use as credenciais fornecidas pelo administrador")
        
        print("\n2. NAVEGAÇÃO:")
        print("   • Digite o número da opção desejada")
        print("   • Use '0' para voltar ou sair")
        print("   • Pressione Ctrl+C para sair em emergência")
        
        print("\n3. FUNCIONALIDADES:")
        print("   • Cadastros: Gerenciar produtos, fornecedores, clientes e funcionários")
        print("   • Estoque: Controlar entrada/saída de produtos")
        print("   • Pedidos: Criar e gerenciar solicitações")
        print("   • Relatórios: Visualizar estatísticas do sistema")
        
        print("\n4. DICAS:")
        print("   • Sempre confirme antes de excluir registros")
        print("   • Use a busca para encontrar itens rapidamente")
        print("   • Verifique o estoque antes de criar pedidos")
        
        self.mostrar_rodape()
    
    def mostrar_sobre(self):
        """Exibe informações sobre o sistema"""
        self.mostrar_cabecalho("SOBRE - SISTEMA IGO")
        
        print("🏢 SISTEMA IGO - GESTÃO DE PRODUTOS")
        print("\n📋 DESCRIÇÃO:")
        print("   Sistema completo para gestão de produtos, incluindo")
        print("   roupas, alimentos, controle de estoque e pedidos.")
        
        print("\n🎯 FUNCIONALIDADES:")
        print("   • Gestão de produtos (roupas e alimentos)")
        print("   • Controle de estoque com alertas")
        print("   • Sistema de pedidos e aprovações")
        print("   • Relatórios detalhados")
        print("   • Controle de acesso por níveis")
        
        print("\n🛠️  TECNOLOGIAS:")
        print("   • Python 3.x com arquitetura MVC")
        print("   • Persistência em arquivo JSON")
        print("   • Interface em terminal")
        
        print("\n👨‍💻 DESENVOLVIMENTO:")
        print("   • Disciplina: NP1 (Semestre 2)")
        print("   • Foco: Programação estruturada e OO")
        print("   • Arquitetura: Model-View-Controller")
        
        print("\n📅 VERSÃO: 1.0.0")
        print("📅 DATA: 2025")
        
        self.mostrar_rodape()
