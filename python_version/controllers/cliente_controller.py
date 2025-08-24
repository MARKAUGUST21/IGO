#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Clientes - Sistema IGO
"""

from datetime import datetime

class ClienteController:
    """Controlador responsável pela gestão de clientes"""
    
    def __init__(self, database):
        self.db = database
    
    def menu_clientes(self):
        """Menu de gestão de clientes"""
        while True:
            print("\n" + "=" * 40)
            print("        GESTÃO DE CLIENTES")
            print("=" * 40)
            print("1 - Cadastrar Cliente")
            print("2 - Listar Clientes")
            print("3 - Buscar Cliente")
            print("4 - Editar Cliente")
            print("5 - Excluir Cliente")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_cliente()
            elif opcao == "2":
                self.listar_clientes()
            elif opcao == "3":
                self.buscar_cliente()
            elif opcao == "4":
                self.editar_cliente()
            elif opcao == "5":
                self.excluir_cliente()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def cadastrar_cliente(self):
        """Cadastra um novo cliente"""
        print("\n" + "=" * 40)
        print("       CADASTRO DE CLIENTE")
        print("=" * 40)
        
        nome = input("Nome completo: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        cpf = input("CPF: ").strip()
        if not cpf:
            print("❌ CPF não pode estar vazio!")
            return
        
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        endereco = input("Endereço: ").strip()
        
        cliente = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone,
            "email": email,
            "endereco": endereco,
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        novo_cliente = self.db.add_item("clientes", cliente)
        print(f"\n✅ Cliente '{novo_cliente['nome']}' cadastrado com sucesso!")
    
    def listar_clientes(self):
        """Lista todos os clientes"""
        clientes = self.db.get_items("clientes")
        
        if not clientes:
            print("\n📭 Nenhum cliente cadastrado!")
            return
        
        print("\n" + "=" * 70)
        print("                            LISTA DE CLIENTES")
        print("=" * 70)
        print(f"{'ID':<4} {'Nome':<25} {'CPF':<15} {'Telefone':<15} {'Email':<20}")
        print("-" * 70)
        
        for cliente in clientes:
            print(f"{cliente['id']:<4} {cliente['nome']:<25} {cliente['cpf']:<15} {cliente['telefone']:<15} {cliente['email']:<20}")
        
        print("=" * 70)
        print(f"Total de clientes: {len(clientes)}")
    
    def buscar_cliente(self):
        """Busca cliente por nome ou CPF"""
        termo = input("Digite o nome ou CPF do cliente: ").strip()
        if not termo:
            print("❌ Termo de busca não pode estar vazio!")
            return
        
        clientes = self.db.get_items("clientes")
        encontrados = []
        
        for cliente in clientes:
            if (termo.lower() in cliente['nome'].lower() or 
                termo in cliente['cpf']):
                encontrados.append(cliente)
        
        if not encontrados:
            print("❌ Nenhum cliente encontrado!")
            return
        
        print(f"\n🔍 Encontrados {len(encontrados)} cliente(s):")
        for cliente in encontrados:
            self.exibir_cliente_detalhado(cliente)
    
    def exibir_cliente_detalhado(self, cliente):
        """Exibe detalhes de um cliente"""
        print("\n" + "-" * 50)
        print(f"ID: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Telefone: {cliente['telefone']}")
        print(f"Email: {cliente['email']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"Data de Cadastro: {cliente['data_cadastro']}")
        print("-" * 50)
    
    def editar_cliente(self):
        """Edita um cliente existente"""
        cliente_id = input("Digite o ID do cliente: ").strip()
        if not cliente_id or not cliente_id.isdigit():
            print("❌ ID inválido!")
            return
        
        cliente = self.db.get_item("clientes", int(cliente_id))
        if not cliente:
            print("❌ Cliente não encontrado!")
            return
        
        print(f"\nEditando cliente: {cliente['nome']}")
        self.exibir_cliente_detalhado(cliente)
        
        print("\nDeixe em branco para manter o valor atual:")
        
        nome = input(f"Nome [{cliente['nome']}]: ").strip()
        if nome:
            cliente['nome'] = nome
        
        telefone = input(f"Telefone [{cliente['telefone']}]: ").strip()
        if telefone:
            cliente['telefone'] = telefone
        
        email = input(f"Email [{cliente['email']}]: ").strip()
        if email:
            cliente['email'] = email
        
        endereco = input(f"Endereço [{cliente['endereco']}]: ").strip()
        if endereco:
            cliente['endereco'] = endereco
        
        self.db.update_item("clientes", cliente['id'], cliente)
        print("✅ Cliente atualizado com sucesso!")
    
    def excluir_cliente(self):
        """Exclui um cliente"""
        cliente_id = input("Digite o ID do cliente: ").strip()
        if not cliente_id or not cliente_id.isdigit():
            print("❌ ID inválido!")
            return
        
        cliente = self.db.get_item("clientes", int(cliente_id))
        if not cliente:
            print("❌ Cliente não encontrado!")
            return
        
        print(f"\nCliente a ser excluído:")
        self.exibir_cliente_detalhado(cliente)
        
        confirmacao = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()
        if confirmacao == 's':
            self.db.delete_item("clientes", cliente['id'])
            print("✅ Cliente excluído com sucesso!")
        else:
            print("❌ Operação cancelada!")
