#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste do Sistema IGO - Verificação de Funcionamento
"""

import os
import sys

def testar_imports():
    """Testa se todos os módulos podem ser importados"""
    print("🧪 TESTANDO IMPORTS...")
    
    try:
        from models.database import Database
        print("✅ Database importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar Database: {e}")
        return False
    
    try:
        from controllers.auth_controller import AuthController
        print("✅ AuthController importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar AuthController: {e}")
        return False
    
    try:
        from controllers.main_controller import MainController
        print("✅ MainController importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar MainController: {e}")
        return False
    
    try:
        from controllers.produto_controller import ProdutoController
        print("✅ ProdutoController importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar ProdutoController: {e}")
        return False
    
    try:
        from views.menu_view import MenuView
        print("✅ MenuView importado com sucesso")
    except Exception as e:
        print(f"❌ Erro ao importar MenuView: {e}")
        return False
    
    return True

def testar_database():
    """Testa funcionalidades básicas do banco de dados"""
    print("\n🗄️  TESTANDO BANCO DE DADOS...")
    
    try:
        from models.database import Database
        
        # Criar instância do banco
        db = Database()
        print("✅ Instância do banco criada")
        
        # Verificar estrutura inicial
        colecoes = ["usuarios", "produtos", "fornecedores", "clientes", "funcionarios", "pedidos", "movimentacoes"]
        for colecao in colecoes:
            if colecao in db.data:
                print(f"✅ Coleção '{colecao}' encontrada")
            else:
                print(f"❌ Coleção '{colecao}' não encontrada")
        
        # Verificar usuários padrão
        usuarios = db.get_items("usuarios")
        if len(usuarios) >= 4:
            print(f"✅ {len(usuarios)} usuários padrão carregados")
        else:
            print(f"❌ Apenas {len(usuarios)} usuários encontrados")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar banco de dados: {e}")
        return False

def testar_controllers():
    """Testa funcionalidades básicas dos controladores"""
    print("\n🎮 TESTANDO CONTROLADORES...")
    
    try:
        from models.database import Database
        from controllers.produto_controller import ProdutoController
        
        db = Database()
        controller = ProdutoController(db)
        print("✅ ProdutoController instanciado com sucesso")
        
        # Testar listagem de produtos
        produtos = controller.db.get_items("produtos")
        print(f"✅ Listagem de produtos: {len(produtos)} produtos")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar controladores: {e}")
        return False

def testar_views():
    """Testa funcionalidades básicas das views"""
    print("\n🖥️  TESTANDO VIEWS...")
    
    try:
        from views.menu_view import MenuView
        
        view = MenuView()
        print("✅ MenuView instanciada com sucesso")
        
        # Testar métodos básicos
        view.mostrar_cabecalho("TESTE")
        print("✅ Método mostrar_cabecalho funcionando")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar views: {e}")
        return False

def main():
    """Função principal de teste"""
    print("=" * 60)
    print("           TESTE DO SISTEMA IGO")
    print("=" * 60)
    
    print(f"📁 Diretório atual: {os.getcwd()}")
    print(f"🐍 Versão Python: {sys.version}")
    
    # Executar testes
    testes = [
        ("Imports", testar_imports),
        ("Database", testar_database),
        ("Controllers", testar_controllers),
        ("Views", testar_views)
    ]
    
    resultados = []
    for nome, teste in testes:
        try:
            resultado = teste()
            resultados.append((nome, resultado))
        except Exception as e:
            print(f"❌ Erro no teste {nome}: {e}")
            resultados.append((nome, False))
    
    # Resumo dos resultados
    print("\n" + "=" * 60)
    print("              RESUMO DOS TESTES")
    print("=" * 60)
    
    sucessos = 0
    for nome, resultado in resultados:
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"{nome:<15}: {status}")
        if resultado:
            sucessos += 1
    
    print(f"\n📊 Resultado: {sucessos}/{len(resultados)} testes passaram")
    
    if sucessos == len(resultados):
        print("\n🎉 SISTEMA FUNCIONANDO PERFEITAMENTE!")
        print("🚀 Você pode executar o sistema com: python main.py")
    else:
        print("\n⚠️  Alguns testes falharam. Verifique os erros acima.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
