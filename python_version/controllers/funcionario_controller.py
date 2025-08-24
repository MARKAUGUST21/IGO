#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Funcionários - Sistema IGO
"""

from datetime import datetime

class FuncionarioController:
    """Controlador responsável pela gestão de funcionários"""
    
    def __init__(self, database):
        self.db = database
    
    def menu_funcionarios(self):
        """Menu de gestão de funcionários"""
        while True:
            print("\n" + "=" * 40)
            print("     GESTÃO DE FUNCIONÁRIOS")
            print("=" * 40)
            print("1 - Cadastrar Funcionário")
            print("2 - Listar Funcionários")
            print("3 - Buscar Funcionário")
            print("4 - Editar Funcionário")
            print("5 - Excluir Funcionário")
            print("0 - Voltar")
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == "1":
                self.cadastrar_funcionario()
            elif opcao == "2":
                self.listar_funcionarios()
            elif opcao == "3":
                self.buscar_funcionario()
            elif opcao == "4":
                self.editar_funcionario()
            elif opcao == "5":
                self.excluir_funcionario()
            elif opcao == "0":
                break
            else:
                print("❌ Opção inválida!")
    
    def cadastrar_funcionario(self):
        """Cadastra um novo funcionário"""
        print("\n" + "=" * 40)
        print("   CADASTRO DE FUNCIONÁRIO")
        print("=" * 40)
        
        nome = input("Nome completo: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        cpf = input("CPF: ").strip()
        if not cpf:
            print("❌ CPF não pode estar vazio!")
            return
        
        cargo = input("Cargo: ").strip()
        if not cargo:
            print("❌ Cargo não pode estar vazio!")
            return
        
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        salario = input("Salário: R$ ").strip()
        
        funcionario = {
            "nome": nome,
            "cpf": cpf,
            "cargo": cargo,
            "telefone": telefone,
            "email": email,
            "salario": salario,
            "data_admissao": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        novo_funcionario = self.db.add_item("funcionarios", funcionario)
        print(f"\n✅ Funcionário '{novo_funcionario['nome']}' cadastrado com sucesso!")
    
    def listar_funcionarios(self):
        """Lista todos os funcionários"""
        funcionarios = self.db.get_items("funcionarios")
        
        if not funcionarios:
            print("\n📭 Nenhum funcionário cadastrado!")
            return
        
        print("\n" + "=" * 70)
        print("                        LISTA DE FUNCIONÁRIOS")
        print("=" * 70)
        print(f"{'ID':<4} {'Nome':<25} {'Cargo':<15} {'CPF':<15} {'Telefone':<15}")
        print("-" * 70)
        
        for funcionario in funcionarios:
            print(f"{funcionario['id']:<4} {funcionario['nome']:<25} {funcionario['cargo']:<15} {funcionario['cpf']:<15} {funcionario['telefone']:<15}")
        
        print("=" * 70)
        print(f"Total de funcionários: {len(funcionarios)}")
    
    def buscar_funcionario(self):
        """Busca funcionário por nome ou CPF"""
        termo = input("Digite o nome ou CPF do funcionário: ").strip()
        if not termo:
            print("❌ Termo de busca não pode estar vazio!")
            return
        
        funcionarios = self.db.get_items("funcionarios")
        encontrados = []
        
        for funcionario in funcionarios:
            if (termo.lower() in funcionario['nome'].lower() or 
                termo in funcionario['cpf']):
                encontrados.append(funcionario)
        
        if not encontrados:
            print("❌ Nenhum funcionário encontrado!")
            return
        
        print(f"\n🔍 Encontrados {len(encontrados)} funcionário(s):")
        for funcionario in encontrados:
            self.exibir_funcionario_detalhado(funcionario)
    
    def exibir_funcionario_detalhado(self, funcionario):
        """Exibe detalhes de um funcionário"""
        print("\n" + "-" * 50)
        print(f"ID: {funcionario['id']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"CPF: {funcionario['cpf']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Telefone: {funcionario['telefone']}")
        print(f"Email: {funcionario['email']}")
        print(f"Salário: R$ {funcionario['salario']}")
        print(f"Data de Admissão: {funcionario['data_admissao']}")
        print("-" * 50)
    
    def editar_funcionario(self):
        """Edita um funcionário existente"""
        funcionario_id = input("Digite o ID do funcionário: ").strip()
        if not funcionario_id or not funcionario_id.isdigit():
            print("❌ ID inválido!")
            return
        
        funcionario = self.db.get_item("funcionarios", int(funcionario_id))
        if not funcionario:
            print("❌ Funcionário não encontrado!")
            return
        
        print(f"\nEditando funcionário: {funcionario['nome']}")
        self.exibir_funcionario_detalhado(funcionario)
        
        print("\nDeixe em branco para manter o valor atual:")
        
        nome = input(f"Nome [{funcionario['nome']}]: ").strip()
        if nome:
            funcionario['nome'] = nome
        
        cargo = input(f"Cargo [{funcionario['cargo']}]: ").strip()
        if cargo:
            funcionario['cargo'] = cargo
        
        telefone = input(f"Telefone [{funcionario['telefone']}]: ").strip()
        if telefone:
            funcionario['telefone'] = telefone
        
        email = input(f"Email [{funcionario['email']}]: ").strip()
        if email:
            funcionario['email'] = email
        
        salario = input(f"Salário [{funcionario['salario']}]: ").strip()
        if salario:
            funcionario['salario'] = salario
        
        self.db.update_item("funcionarios", funcionario['id'], funcionario)
        print("✅ Funcionário atualizado com sucesso!")
    
    def excluir_funcionario(self):
        """Exclui um funcionário"""
        funcionario_id = input("Digite o ID do funcionário: ").strip()
        if not funcionario_id or not funcionario_id.isdigit():
            print("❌ ID inválido!")
            return
        
        funcionario = self.db.get_item("funcionarios", int(funcionario_id))
        if not funcionario:
            print("❌ Funcionário não encontrado!")
            return
        
        print(f"\nFuncionário a ser excluído:")
        self.exibir_funcionario_detalhado(funcionario)
        
        confirmacao = input("\nTem certeza que deseja excluir? (s/n): ").strip().lower()
        if confirmacao == 's':
            self.db.delete_item("funcionarios", funcionario['id'])
            print("✅ Funcionário excluído com sucesso!")
        else:
            print("❌ Operação cancelada!")
