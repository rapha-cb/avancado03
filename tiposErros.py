try:
    print(x)
except NameError:
    print("ops, sua variável não está definida")

try:
    num = "1"
    num2 = "2"
    print(num * num2)
except TypeError:
    print("Você teve um erro de tipo de dados, corrige aí!")

try:
    dicionario = {"a": "aaaa"}
    print(dicionario["b"])
except KeyError:

    print("essa chave do dicionario não existe")

try:
    lista=[1,2,3]
    print(lista[5])
except IndexError:
    print("eita! Você ta tentando acessar um index de uma lista que não existe")

try:
    umOld= " taylor swift é uma merda!"
    umOld.reverse()
except:
    print("Presta atenção, tu tá tendo algum erro de atributo")

try:
    a= int("a casca da bânanaaa")
    print(a)
except ValueError:
    print("ta tendo um erro de valor ai hein!!")



