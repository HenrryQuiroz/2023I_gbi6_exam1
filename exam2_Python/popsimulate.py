#_____________ Función 1
import numpy as  np # Importamos el módulo "Numpy" y lo guardamos como "np"
np.random.seed(20) # Luego generamos una matriz de numeros random en una semilla cualquiera
def build_population(N, p): # Se define la función "build_population" que construirá una población de tamaño "N", donde cada
#individuo tiene dos alelos y "p" que será la praobabilidad que un alelo sea `` en ves de `A`.
    population = [] # iniciará una lista vacía "population" en la cual se almacenará los individuos de la población.
    for i in range(N): # Se inicia un bucle donde se ejecutará "N" veces, donde "i" toma los valores "N-1". Esto asegura que se construirá "N" individuos para la población.
        allele1 = "A" # llamamos a la variable "allele1" del individuo actual con el valor "A" que sería el alelo dominante.
        if np.random.random() > p: # Se genera un número aleatorio entre 0 y 1 utilizando la función `random()´ del módulo `numpy.random´. Si este número aleatorio es mayor que "p",
            # se ejecutará la siguiente linea de código, de lo contrario, no.
            allele1 = "a" # Si el número aleatorio generado es mayor que `p´, el alelo1 se establece como "a" que sería el alelo recesivo.
        allele2 = "A" # Llamamos a la variable "allele2" del individu actual son el valor "A" que sería el alelo dominante.
        if np.random.random() > p: # Se genera otro número aleatorio entre 0 y 1 utilizando la función `random()´ del módulo `numpy.random´. Si este número aleatorio es mayor que "p",
            # se ejecutará la siguiente linea de código, de lo contrario, no.
            allele2 = "a" # Si el número aleatorio generado es mayor que `p´, el alelo2 se establece como "a" que sería el alelo recesivo.
        population.append((allele1, allele2)) # Se genera una tupla que contiene los valores de "allele1" y "allele2" a la lista de "population". Cada tupla representa un individuo
        # de la población
    return population # Devuelve a la lista "population", que representa la población genética completa con "N" individuos.


#_________________ Función 2
def compute_frequencies(population): # Se define la función "compute_frequencies" que calculará las frecuencias de los diferentes genotipos en una pobación dada,
    # donde variable "population" es una lista de tuplas que representan a la población.
    AA = population.count(("A", "A")) # Se cuenta el número de veces que la tupla ("A","A") aparecese en la lista de "población" y lo guarda en la variable "AA".
    Aa = population.count(("A", "a")) # Se cuenta el número de veces que la tupla ("A","a") aparecese en la lista de "población" y lo guarda en la variable "Aa".
    aA = population.count(("a", "A")) # Se cuenta el número de veces que la tupla ("a","A") aparecese en la lista de "población" y lo guarda en la variable "aA".
    aa = population.count(("a", "a")) # Se cuenta el número de veces que la tupla ("a","a") aparecese en la lista de "población" y lo guarda en la variable "aa"
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA}) # Devuelve el número de veces que se ha repetido cada genotipo de la variable "poblacion"

#_________________ Función 3
def reproduce_population(population): # Se define la función "reproduce_population" que simulará el proceso de reproducción en una población dada tomando como parámetro
    # "population" que será una lista de tuplas de genotipos.
    new_generation = [] # Se define una variable "new_generatio" que será una lista vacía donde se almacenará la reprodución.
    N = len(population) # Se define una variable "N" donde se contará el tamaño de la poblaciòn actual.
    for i in range(N): # Se inicia un bucle que ejecutará "N" veces, donde "i" toma valore desde 0 hasta "N-1". Esto nos dice que se generará "N" decendintes.
        dad = np.random.randint(N) # Se define la vaiable "dad" donde se selecciona aleatoriamente un índice de individuo(del padre) en el rango 0 a "N-1",
        # utilizando la función "randint()" del módulo "numpy.random". Representa la selecciòn del padre.
        mom = np.random.randint(N) # Se define la vaiable "mom" donde se selecciona aleatoriamente un índice de individuo(de la madre) en el rango 0 a "N-1",
        # utilizando la función "randint()" del módulo "numpy.random". Representa la selecciòn de la madre.
        chr_mom = np.random.randint(2) # Se define la variable "chr_mom" donde se seleccionará un varon dentro de 0 a 1 el cual representará el cromosoma que se hereda de la madre.
        # esta función determina el alelo que se tomará del genotipo de la madre.
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom]) # Se define la variable "offspring" donde crea una tupla que represetna el genotipo del descendiente.
        # el primer elemento "population[mom][chr_mom]" toma el genotipo de la madre y el segundo elemento "population[dad][1 - chr_mom]" toma el genotipo del padre.
        new_generation.append(offspring) # Se genera una tupla "offspring" a la lista "new_generation" la cual representa los individuos generados
    return new_generation # Devuelve la lista "new_generation" la cual es la nueva generación.

#_________________ Función 4
def simulate_drift(N, p):
    my_pop = build_population(N, p)
    fixation = False
    num_generations = 0
    while fixation == False:
        genotype_counts = compute_frequencies(my_pop)
        if (genotype_counts["AA"] == N or genotype_counts["aa"] == N):
            print("An allele reached fixation at generation", num_generations)
            print("The genotype counts are")
            print(genotype_counts)
            fixation == True
            break
        my_pop = reproduce_population(my_pop)
        num_generations += 1
    return num_generations, genotype_counts