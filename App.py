# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script

import sys
from random import randint
from Individual import Individual
"""Importamos el modulo random.

random es la libreria para generar numero alaeatorios.

randint es una funcion de random para generar numeros
enteros aleatorios.

Se importa la clase Individual.

"""


class App(object):
    'Clase App'

    def __init__(self):
        """def __init__(self):

        Esta funcion es para definir todos los atributos del objeto:
            tamaño maximo del objeto = 300
            tamaño minimo del objeto = 1 
            poblacion maxima = 300
            poblacion minima = 100
            rango de mutación maxima = 0.0 
            rango de mutación minima = 1.0

        """
        self.maxLengthObjetive = 300
        self.minLengthObjetive = 1
        self.maxPopulation = 300
        self.minPopulation = 100
        self.minRateMutation = 0.0
        self.maxRateMutation = 1.0
        self.populations = []
        self.inputParams()
        self.executeGeneticAlgorithm()

    def inputParams(self):
        """def inputParams(self):

        Esta función es para definir los parametros de entrada.

            inputObjetive() --> es para introducir el obejto de entrada,
            ej: "all is well".

            inputPopulation() --> es para introdcir la poblacion definida 
            en el rango de 100 a 300.

            inputRateMutation() --> es para introcucir el valor de la 
            mutación definida en un rango dde 0.0 a a 1.0.

        """
        self.inputObjetive()
        self.inputPopulation()
        self.inputRateMutation()

    def inputObjetive(self):
        """def inputObjetive(self):

        esta función es para inresar el objeto, en este caso 
        un texto. 
        
        se defini una condicion, en caso de que no se haya
        ingresado el objeto se muestra una exception con algun mensaje,
        por otro lado si el objeto es muy corto o muy extenso, igual se 
        muestra un mensaje.


        """
        self.objetive = input("Ingrese el texto objetivo: ")
        if (len(self.objetive) == 0):
            raise Exception("Exception: El objetivo no fue ingresado!")
        if (len(self.objetive) < self.minLengthObjetive):
            raise Exception("Exception: El objetivo es muy corto!")
        if (len(self.objetive) > self.maxLengthObjetive):
            raise Exception("Exception: El objetivo es muy extenso!")

    def inputPopulation(self):
        """def inputPopulation(self):

        Esta función es para introducir la población.

        """
        self.numberPopulation = int(
            input("Ingrese cantidad de individuos por poblacion [100 a 300]: "))
        if (self.numberPopulation == 0):
            raise Exception(
                "Exception: La poblacion de individuos es invalida!")
        if (self.numberPopulation < self.minPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy reducida!")
        if (self.numberPopulation > self.maxPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy extensa!")

    def inputRateMutation(self):
        """def inputRateMutation(self):

        Esta funcion es para introducir la mutación.

        """
        self.rateMutation = float(
            input("Ingrese la tasa de mutacion [0 a 1]: "))
        if (self.rateMutation < self.minRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser menor de %s" % self.minRateMutation)
        if (self.rateMutation > self.maxRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser mayor de %s" % self.maxRateMutation)

    def executeGeneticAlgorithm(self):
        """def executeGeneticAlgorithm(self):

        Esta fución es para ejceutar el algoritmo.

        """

        for _ in range(0, self.numberPopulation):
            individual = Individual()
            individual.generateGenes(len(self.objetive), self.objetive)
            self.populations.append(individual)
        self.generation = 0
        print("Buscando mejor individuo....")
        while True:
            self.evaluateMembersGeneration()
            self.selectMembersGeneration()
            self.reproductionMembersGeneration()

    def evaluateMembersGeneration(self):
        """ef evaluateMembersGeneration(self):

        Esta función es para evaluar los miembros de la generación, 
        y mostrar la generación, el individuo y el fitness.

        """
        self.generation += 1
        print("\n*************** GENERACION %s\n" % self.generation)
        for _ in range(0, self.numberPopulation):
            print("Generacion[%s] | Individuo[%s]: %s | fitness: %s" % (
                self.generation, _, self.populations[_].getPhenotype(), self.populations[_].getFitness()))
            if (self.evaluateObjetive(self.populations[_])):
                sys.exit()

    def selectMembersGeneration(self):
        """def selectMembersGeneration(self):
        
        Esta función es para selecionar los miembos de la generación,

        """
        self.parents = []
        for _ in range(0, self.numberPopulation):
            n = int(self.populations[_].getFitness()*100)
            #for j in range(0, n):
            if n>0:
                self.parents.append(self.populations[_])

    def reproductionMembersGeneration(self):
        """def reproductionMembersGeneration(self):

        Esta funcion es para la generacion de nuevos miembros.

        """
        totalParents = len(self.parents)
        print("Padres seleccionados: ", totalParents)
        for i in range(0, self.numberPopulation):
            a = int(randint(0, (totalParents-1)))
            b = int(randint(0, (totalParents-1)))
            father = self.parents[a]
            mother = self.parents[b]
            children = father.cross(mother)
            children.mutate(self.rateMutation)
            self.populations[i] = children

    def evaluateObjetive(self, individual):
        """def evaluateObjetive(self, individual):

        Esta funcion evaluea el objeto 
            return True
        Cuando es encontrado.

        """
        if (individual.getFitness() == 1.0):
            print("Objetivo encontrado: %s" % individual.getPhenotype())
            return True
        return False

    def showIndividualPhenotype(self):
        """def showIndividualPhenotype(self):

        Esta funcion es para mostrar el objeto,
        (el texto cncatenado y/o unido)

        """
        for j in range(0, self.numberPopulation):
            print("Individuo %s : %s" %
                  (j, self.populations[j].getPhenotype()))


if __name__ == "__main__":
    try:
        app = App()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
