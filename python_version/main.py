#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema IGO - Gestão de Produtos
Versão Python com Arquitetura MVC
"""

from controllers.auth_controller import AuthController
from controllers.main_controller import MainController
from models.database import Database
from views.menu_view import MenuView
import os

def main():
    """Função principal do sistema"""
    print("=" * 50)
    print("    SISTEMA IGO - GESTÃO DE PRODUTOS")
    print("=" * 50)
    
    # Inicializa o banco de dados
    db = Database()
    
    # Inicializa o controlador de autenticação
    auth_controller = AuthController(db)
    
    # Inicializa o controlador principal
    main_controller = MainController(db)
    
    # Inicializa a view do menu
    menu_view = MenuView()
    
    # Loop principal do sistema
    while True:
        try:
            # Tela de login
            user = auth_controller.login()
            if user:
                print(f"\nBem-vindo, {user['nome']}!")
                
                # Menu principal baseado no nível de acesso
                main_controller.show_main_menu(user['nivel_acesso'])
            else:
                print("Login falhou. Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nSaindo do sistema...")
            break
        except Exception as e:
            print(f"Erro: {e}")
            continue

if __name__ == "__main__":
    main()
