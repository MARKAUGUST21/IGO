#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Fornecedores - Sistema IGO
"""

from datetime import datetime

class FornecedorController:
    """Controlador responsável pela gestão de fornecedores"""
    
    def __init__(self, database):
        self.db = database
    
    def menu_fornecedores(self):
        """Menu de gestão de fornecedores"""
        while True:
            print("\n" + "=" * 40)
            print("      GESTÃO DE FORNECEDORES")
            print("=" * 40)
            print("1 - Cadastrar Fornecedor")
            print("2 - Listar Fornecedores")
            print("3 - Buscar Fornecedor")
            print("4 - Editar Fornecedor")
            print("5 - Excluir Fornecedor")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_fornecedor()
            elif opcao == "2":
                self.listar_fornecedores()
            elif opcao == "3":
                self.buscar_fornecedor()
            elif opcao == "4":
                self.editar_fornecedor()
            elif opcao == "5":
                self.excluir_fornecedor()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def cadastrar_fornecedor(self):
        """Cadastra um novo fornecedor"""
        print("\n" + "=" * 40)
        print("     CADASTRO DE FORNECEDOR")
        print("=" * 40)
        
        nome = input("Nome/Razão Social: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        cnpj = input("CNPJ: ").strip()
        if not cnpj:
            print("❌ CNPJ não pode estar vazio!")
            return
        
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        endereco = input("Endereço: ").strip()
        
        fornecedor = {
            "nome": nome,
            "cnpj": cnpj,
            "telefone": telefone,
            "email": email,
            "endereco": endereco,
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        novo_fornecedor = self.db.add_item("fornecedores", fornecedor)
        print(f"\n✅ Fornecedor '{novo_fornecedor['nome']}' cadastrado com sucesso!")
    
    def listar_fornecedores(self):
        """Lista todos os fornecedores"""
        fornecedores = self.db.get_items("fornecedores")
        
        if not fornecedores:
            print("\n📭 Nenhum fornecedor cadastrado!")
            return
        
        print("\n" + "=" * 70)
        print("                           LISTA DE FORNECEDORES")
        print("=" * 70)
        print(f"{'ID':<4} {'Nome':<25} {'CNPJ':<18} {'Telefone':<15} {'Email':<20}")
        print("-" * 70)
        
        for fornecedor in fornecedores:
            print(f"{fornecedor['id']:<4} {fornecedor['nome']:<25} {fornecedor['cnpj']:<18} {fornecedor['telefone']:<15} {fornecedor['email']:<20}")
        
        print("=" * 70)
        print(f"Total de fornecedores: {len(fornecedores)}")
    
    def buscar_fornecedor(self):
        """Busca fornecedor por nome ou CNPJ"""
        termo = input("Digite o nome ou CNPJ do fornecedor: ").strip()
        if not termo:
            print("❌ Termo de busca não pode estar vazio!")
            return
        
        fornecedores = self.db.get_items("fornecedores")
        encontrados = []
        
        for fornecedor in fornecedores:
            if (termo.lower() in fornecedor['nome'].lower() or 
                termo in fornecedor['cnpj']):
                encontrados.append(fornecedor)
        
        if not encontrados:
            print("❌ Nenhum fornecedor encontrado!")
            return
        
        print(f"\n🔍 Encontrados {len(encontrados)} fornecedor(es):")
        for fornecedor in encontrados:
            self.exibir_fornecedor_detalhado(fornecedor)
    
    def exibir_fornecedor_detalhado(self, fornecedor):
        """Exibe detalhes de um fornecedor"""
        print("\n" + "-" * 50)
        print(f"ID: {fornecedor['id']}")
        print(f"Nome: {fornecedor['nome']}")
        print(f"CNPJ: {fornecedor['cnpj']}")
        print(f"Telefone: {fornecedor['telefone']}")
        print(f"Email: {fornecedor['email']}")
        print(f"Endereço: {fornecedor['endereco']}")
        print(f"Data de Cadastro: {fornecedor['data_cadastro']}")
        print("-" * 50)
    
    def editar_fornecedor(self):
        """Edita um fornecedor existente"""
        fornecedor_id = input("Digite o ID do fornecedor: ").strip()
        if not fornecedor_id or not fornecedor_id.isdigit():
            print("❌ ID inválido!")
            return
        
        fornecedor = self.db.get_item("fornecedores", int(fornecedor_id))
        if not fornecedor:
            print("❌ Fornecedor não encontrado!")
            return
        
        print(f"\nEditando fornecedor: {fornecedor['nome']}")
        self.exibir_fornecedor_detalhado(fornecedor)
        
        print("\nDeixe em branco para manter o valor atual:")
        
        nome = input(f"Nome [{fornecedor['nome']}]: ").strip()
        if nome:
            fornecedor['nome'] = nome
        
        telefone = input(f"Telefone [{fornecedor['telefone']}]: ").strip()
        if telefone:
            fornecedor['telefone'] = telefone
        
        email = input(f"Email [{fornecedor['email']}]: ").strip()
        if email:
            fornecedor['email'] = email
        
        endereco = input(f"Endereço [{fornecedor['endereco']}]: ").strip()
        if endereco:
            fornecedor['endereco'] = endereco
        
        self.db.update_item("fornecedores", fornecedor['id'], fornecedor)
        print("✅ Fornecedor atualizado com sucesso!")
    
    def excluir_fornecedor(self):
        """Exclui um fornecedor"""
        fornecedor_id = input("Digite o ID do fornecedor: ").strip()
        if not fornecedor_id or not fornecedor_id.isdigit():
            print("❌ ID inválido!")
            return
        
        fornecedor = self.db.get_item("fornecedores", int(fornecedor_id))
        if not fornecedor:
            print("❌ Fornecedor não encontrado!")
            return
        
        print(f"\nFornecedor a ser excluído:")
        self.exibir_fornecedor_detalhado(fornecedor)
        
        confirmacao = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()
        if confirmacao == 's':
            self.db.delete_item("fornecedores", fornecedor['id'])
            print("✅ Fornecedor excluído com sucesso!")
        else:
            print("❌ Operação cancelada!")
