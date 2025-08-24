#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo de Banco de Dados - Sistema IGO
"""

import json
import os
from datetime import datetime, timedelta

class Database:
    """Classe responsável pelo gerenciamento dos dados do sistema"""
    
    def __init__(self):
        self.data_file = "igo_data.json"
        self.data = self.load_data()
    
    def load_data(self):
        """Carrega dados do arquivo JSON ou cria estrutura inicial"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        
        # Estrutura inicial do banco
        initial_data = {
            "usuarios": [
                {
                    "id": 1,
                    "username": "admin",
                    "senha": "admin123",
                    "nome": "Administrador",
                    "nivel_acesso": "administrador",
                    "email": "admin@igo.com"
                },
                {
                    "id": 2,
                    "username": "gerente",
                    "senha": "gerente123",
                    "nome": "Gerente",
                    "nivel_acesso": "gerente",
                    "email": "gerente@igo.com"
                },
                {
                    "id": 3,
                    "username": "vendedor",
                    "senha": "vendedor123",
                    "nome": "Vendedor",
                    "nivel_acesso": "vendedor",
                    "email": "vendedor@igo.com"
                },
                {
                    "id": 4,
                    "username": "cliente",
                    "senha": "cliente123",
                    "nome": "Cliente",
                    "nivel_acesso": "cliente",
                    "email": "cliente@igo.com"
                }
            ],
            "produtos": [],
            "fornecedores": [],
            "clientes": [],
            "funcionarios": [],
            "pedidos": [],
            "movimentacoes": []
        }
        
        self.save_data(initial_data)
        return initial_data
    
    def save_data(self, data=None):
        """Salva dados no arquivo JSON"""
        if data is None:
            data = self.data
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        
        self.data = data
    
    def get_next_id(self, collection):
        """Gera próximo ID para uma coleção"""
        if not self.data[collection]:
            return 1
        
        max_id = max(item['id'] for item in self.data[collection])
        return max_id + 1
    
    def add_item(self, collection, item):
        """Adiciona item a uma coleção"""
        item['id'] = self.get_next_id(collection)
        self.data[collection].append(item)
        self.save_data()
        return item
    
    def update_item(self, collection, item_id, updates):
        """Atualiza item de uma coleção"""
        for item in self.data[collection]:
            if item['id'] == item_id:
                item.update(updates)
                self.save_data()
                return item
        return None
    
    def delete_item(self, collection, item_id):
        """Remove item de uma coleção"""
        for i, item in enumerate(self.data[collection]):
            if item['id'] == item_id:
                deleted = self.data[collection].pop(i)
                self.save_data()
                return deleted
        return None
    
    def get_item(self, collection, item_id):
        """Busca item por ID"""
        for item in self.data[collection]:
            if item['id'] == item_id:
                return item
        return None
    
    def get_items(self, collection, filters=None):
        """Busca itens de uma coleção com filtros opcionais"""
        items = self.data[collection]
        
        if filters:
            filtered_items = []
            for item in items:
                match = True
                for key, value in filters.items():
                    if key not in item or item[key] != value:
                        match = False
                        break
                if match:
                    filtered_items.append(item)
            return filtered_items
        
        return items
    
    def get_produtos_baixo_estoque(self, limite=10):
        """Retorna produtos com estoque baixo"""
        return [p for p in self.data['produtos'] if p['quantidade'] <= limite]
    
    def get_produtos_vencendo(self, dias=30):
        """Retorna produtos próximos do vencimento (apenas alimentos)"""
        hoje = datetime.now()
        limite = hoje + timedelta(days=dias)
        
        produtos_vencendo = []
        for produto in self.data['produtos']:
            if produto['categoria'] == 'alimento' and 'validade' in produto:
                try:
                    validade = datetime.strptime(produto['validade'], '%Y-%m-%d')
                    if validade <= limite:
                        produtos_vencendo.append(produto)
                except:
                    pass
        
        return produtos_vencendo
