#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controlador de Autenticação - Sistema IGO
"""

import getpass

class AuthController:
    """Controlador responsável pela autenticação e controle de acesso"""
    
    def __init__(self, database):
        self.db = database
    
    def login(self):
        """Realiza o processo de login do usuário"""
        print("\n" + "=" * 40)
        print("           LOGIN - SISTEMA IGO")
        print("=" * 40)
        
        while True:
            try:
                username = input("Usuário: ").strip()
                if not username:
                    print("❌ Usuário não pode estar vazio!")
                    continue
                
                # Senha oculta para segurança
                senha = getpass.getpass("Senha: ").strip()
                if not senha:
                    print("❌ Senha não pode estar vazia!")
                    continue
                
                # Verificar credenciais
                user = self.verificar_credenciais(username, senha)
                if user:
                    return user
                else:
                    print("❌ Usuário ou senha incorretos!")
                    
                    # Opção de recuperação de senha
                    opcao = input("\nEsqueceu a senha? (s/n): ").strip().lower()
                    if opcao == 's':
                        self.recuperar_senha(username)
                    
            except KeyboardInterrupt:
                print("\n\nSaindo...")
                return None
            except Exception as e:
                print(f"❌ Erro no login: {e}")
                continue
    
    def verificar_credenciais(self, username, senha):
        """Verifica se as credenciais estão corretas"""
        usuarios = self.db.get_items("usuarios")
        
        for usuario in usuarios:
            if usuario['username'] == username and usuario['senha'] == senha:
                return usuario
        
        return None
    
    def recuperar_senha(self, username):
        """Sistema simples de recuperação de senha"""
        print("\n" + "=" * 40)
        print("        RECUPERAÇÃO DE SENHA")
        print("=" * 40)
        
        usuarios = self.db.get_items("usuarios")
        usuario = None
        
        for u in usuarios:
            if u['username'] == username:
                usuario = u
                break
        
        if not usuario:
            print("❌ Usuário não encontrado!")
            return
        
        print(f"Usuário: {usuario['username']}")
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        
        # Senhas padrão para recuperação
        senhas_padrao = {
            'admin': 'admin123',
            'gerente': 'gerente123',
            'vendedor': 'vendedor123',
            'cliente': 'cliente123'
        }
        
        if username in senhas_padrao:
            print(f"\n✅ Sua senha padrão é: {senhas_padrao[username]}")
            print("⚠️  Recomendamos alterar a senha após o primeiro acesso!")
        else:
            print("\n❌ Usuário não possui senha padrão configurada.")
            print("Entre em contato com o administrador do sistema.")
        
        input("\nPressione ENTER para continuar...")
    
    def alterar_senha(self, user_id):
        """Permite ao usuário alterar sua senha"""
        print("\n" + "=" * 40)
        print("         ALTERAR SENHA")
        print("=" * 40)
        
        senha_atual = getpass.getpass("Senha atual: ").strip()
        
        # Verificar senha atual
        usuario = self.db.get_item("usuarios", user_id)
        if not usuario or usuario['senha'] != senha_atual:
            print("❌ Senha atual incorreta!")
            return False
        
        nova_senha = getpass.getpass("Nova senha: ").strip()
        if not nova_senha:
            print("❌ Nova senha não pode estar vazia!")
            return False
        
        confirmar_senha = getpass.getpass("Confirmar nova senha: ").strip()
        if nova_senha != confirmar_senha:
            print("❌ As senhas não coincidem!")
            return False
        
        # Atualizar senha
        self.db.update_item("usuarios", user_id, {"senha": nova_senha})
        print("✅ Senha alterada com sucesso!")
        return True
    
    def verificar_permissao(self, user, acao):
        """Verifica se o usuário tem permissão para realizar uma ação"""
        nivel = user['nivel_acesso']
        
        # Matriz de permissões
        permissoes = {
            'administrador': ['tudo'],
            'gerente': ['cadastrar_produto', 'editar_produto', 'gerenciar_estoque', 'aprovar_pedidos', 'gerar_relatorios'],
            'vendedor': ['visualizar_produtos', 'atualizar_estoque', 'criar_pedidos', 'visualizar_pedidos'],
            'cliente': ['visualizar_produtos', 'criar_pedidos', 'visualizar_meus_pedidos']
        }
        
        if nivel in permissoes:
            if 'tudo' in permissoes[nivel] or acao in permissoes[nivel]:
                return True
        
        return False
