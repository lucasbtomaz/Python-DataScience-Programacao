# Criando um arquivo com funções

arquivo = open('arq.txt', 'w')

arquivo.write("Curso Python \n")
arquivo.write("Aula Prática")
arquivo.close()

# Leitura do arquivo criado com funções
leitura = open('arq.txt', 'r')
print (leitura.read())
leitura.close()