# !/usr/bin/env python
# -*- coding: utf-8 -*-

#import random module
from random import randint
import random
"""Importamos el modulo random.

random es la libreria para generar numero alaeatorios.

randint es una funcion de random para generar numeros
enteros aleatorios.

"""

class Individual(object):
    """Clase Individual.

    Esta clase define el comportamiento del individuo.

    Se crea un objeto.
    
    El metodo __int__ es para inicializar los atributos
    del objeto creado.

    Los atributos del objeto son:
        self.minNumberChar = 32 
        self.maxNumberChar = 128

    La mutación se define entre 0.0 y 1.0

        self.minRateMutation = 0.0
        self.maxRateMutation = 1.0

        self.genes = []
    Es un arreglo utilizado en la funcion:
        def getFitness(self):
        

    """

    def __init__(self):
        self.minNumberChar = 32
        self.maxNumberChar = 128
        self.minRateMutation = 0.0
        self.maxRateMutation = 1.0
        self.genes = []

    def generateGenes(self, numberGenes, objetive):
        """def generateGenes(self, numberGenes, objetive):.
        
        Esta función es para genera los numeros aleatorios
        que se eencuentren dentro del rango:

            minNumberChart = 32
            maxNumberchart = 128

        Es decir entre los numeros 32 y 128, estos son los
        los numeros que representan a los Genes.

            for _ in range(0, self.numberGenes):
        
        Es el ciclo que realiza iteraciones hasta que 
        se cumpla con el numero de genes establecido, y los
        números que genera son letras (caracteres).

        """
        self.numberGenes = numberGenes
        self.objetive = objetive
        for _ in range(0, self.numberGenes):
            self.genes.append(
                chr(randint(self.minNumberChar, self.maxNumberChar)))

    def getPhenotype(self):
        """def getPhenotype(self):.

        Esta función es para construir el Genotipo.

            return ''.join(self.genes).encode("utf-8")

        retona la union de los caracteres generados aleatoriamente
        en letras concatenadas y/o unidas en una cadena.

        """
        return ''.join(self.genes).encode("utf-8")

    def getFitness(self):
        """def getFitness(self):.

        Esta función es para establecer el valor numerico aleatoriamente
        a partir de un ciclo:

            for i in range(0, len(self.genes)):

            i es una variable que almacena cada caracter de la
            cadena ingresada en cada posición de Array.

            
            (self.genes) es un arreglo definido en los atributos del 
                            objeto y contiene el numero total de caracteres 
                            de una cadena.

            score = 0 es una varable qe aumenta de uno en uno
            para recorrer el array de los caracteres y/o cadena. 

            return float(score)/float(len(self.objetive))
        Retorna el score en decimal.

        """
        score = 0
        for i in range(0, len(self.genes)):
            if self.genes[i] == self.objetive[i]:
                score += 1
        return float(score)/float(len(self.objetive))

    def cross(self, couple):
        """def cross(self, couple):.

        Esta Función mezcla las caracteristicas de los padres
        entre los individuos de la población. 

            children = Individual()

        children es un objeto que se instancia a la clase Individual()

        El objeto children llama al metodo generateGenes:
            children.generateGenes(self.numberGenes,self.objetive)
        con el numero de genes y el objeto.
            
        Se vuelven a generar los numeros aleatorios tomando en cuenta
        el tamaño de la variable genes.

            middlePoint = int(randint(1, len(self.genes) - 1))


        """
        children = Individual()
        children.generateGenes(self.numberGenes,self.objetive)
        middlePoint = int(randint(1, len(self.genes) - 1))
        for i in range(0, len(self.genes)):
            if (i > middlePoint):
                children.genes[i] = self.genes[i]
            else:
                children.genes[i] = couple.genes[i]
        return children

    def mutate(self, rateMutation):
        """def mutate(self, rateMutation):.

        Esta funcion es para modficar al azar algunas partes del 
        genotipo.

        Los numeros aleatorios que se generan son flotantes y se
        encuentran entre minRateMutation y maxRateMutation.

            randRateMutation = float(random.uniform(
                self.minRateMutation, self.maxRateMutation))

        """
        for i in range(0, len(self.genes)):
            randRateMutation = float(random.uniform(
                self.minRateMutation, self.maxRateMutation))
            if (randRateMutation < rateMutation):
                if (self.genes[i] != self.objetive[i]):
                    self.genes[i] = chr(
                        randint(self.minNumberChar, self.maxNumberChar))
