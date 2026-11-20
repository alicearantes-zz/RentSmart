# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:20:13 2026

@author: alice
"""

import csv

class Imovel:
    def __init__(self, tipo, quartos, vagas, possui_criancas):
        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas
        self.possui_criancas= possui_criancas
        
    def calcular_aluguel(self):
        
        if self.tipo == "apartamento":
            valor = 700
            
            if self.quartos == 2:
                valor += 200
            
        elif self.tipo == "casa":
            valor = 900
            
            if self.quartos == 2:
                valor += 250
                
        else:
            valor = 1200
            
        if self.tipo == "estudio":
            if self.vagas > 0:
                valor += 250
                
                if self.vagas > 2:
                    valor += (self.vagas - 2) * 60
                    
        elif self.vagas > 0:
            valor += 300
            
        if self.tipo == "apartamento":
            if not self. possui_criancas:
                valor -= valor * 0.05
                
        return valor
    
class Orcamento:
    def __init__(self, imovel, parcelas):
        self.imovel = imovel
        self.parcelas = parcelas
        self.taxa_contratual = 2000
        
    def calcular_parcela(self):
        return self.taxa_contratual / self.parcelas
    
    def exibir_orcamento(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela()
        
        print("============= RENTSMART ==============")
        print("RESUMO DO ORÇAMENTO")
        print("Tipo de imóvel:", self.imovel.tipo)
        print("Quantidade de quartos:", self.imovel.quartos)
        print("Vagas de garagem:", self.imovel.vagas)
        print(f"Aluguel mensal: R$ {aluguel:.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contratual:.2f}")
        print(f"Parcelamento: {self.parcelas}x de R$ {parcela:.2f}")
        print("========================================")
        
    def gerar_csv(self):
        aluguel = self.imovel.calcular_aluguel()
        parcela = self.calcular_parcela()
        
        with open("projecao_rentsmart.csv", "w",
                  newline="", encoding="utf-8-sig") as arquivo:
            
            escritor = csv.writer(arquivo, delimiter=";")
            
            escritor.writerow([
                "Mes",
                "Aluguel",
                "Taxa Contratual",
                "Total Mensal"
            ])
            
            for mes in range(1, 13):
                if mes <= self.parcelas:
                    taxa = parcela
                else:
                    taxa = 0
                    
                total = aluguel + taxa
                
                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}",
                    f"{taxa:.2f}",
                    f"{total:.2f}"
                ])
                    
        print("\nArquivo CSV gerado com sucesso!")
        
def solicitar_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            valor = int(input(mensagem))
            
            if minimo <= valor <= maximo:
                return valor
            
            print("Valor fora do intervalo permitido.")
            
        except ValueError:
            print("Digite um número inteiro válido.")
            
def iniciar_sistema():
    print("========================================")
    print("         BEM-VINDO AO RENTSMART         ")
    print("========================================")
    
    print("\nTipos de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")
    
    opcao = solicitar_inteiro("Escolha o imóvel: ", 1, 3)
    
    if opcao == 1:
        tipo = "apartamento"
        quartos = solicitar_inteiro(
            "Quantidade de quartos (1 ou 2): ", 1, 2
        )
        
        criancas = input("Possui crianças? (s/n): ").lower()
        
        while criancas not in {"s", "n"}:
            print("Digite apenas s ou n.")
            criancas = input("Possui crianças? (s/n): ").lower()
            
        possui_criancas = criancas == "s"
        
    elif opcao == 2:
        tipo = "casa"
        quartos = solicitar_inteiro(
            "Quantidade de quartos (1 ou 2): ", 1, 2
        )
        possui_criancas = False
        
    else:
        tipo = "estudio"
        quartos = 0
        possui_criancas = False
        
    vagas = solicitar_inteiro(
        "Quantidade de vagas de garagem (0 a 10): ", 0, 10
    )
    
    parcelas = solicitar_inteiro(
        "Quantidade de parcelas de taxa (1 a 5): ", 1, 5
    )
    
    imovel = Imovel(tipo, quartos, vagas, possui_criancas)
    
    orcamento = Orcamento(imovel, parcelas)
    
    orcamento.exibir_orcamento()
    orcamento.gerar_csv()
    
iniciar_sistema()

        
                
                
            
        
        
