import json
with open ('elemento.json', 'r') as file:
    lista_elements = json.load(file)


lista_elemts=[]

def add_elemet(id,name,ape):
    lista_elemts.append({
        "id": id,
        "nombre": name,
        "apellido": ape
        })
    return name
    ##lista_elemnts.append()()
    pass
            ##Agregamos elemntosprint("Agregado!!")
def remove_elemet(bus):
    alumno_buscado= {}
    for alumno in lista_elemts:
        if alumno['nombre']== bus:
            alumno_buscado = alumno
        lista_elemts.remove(alumno_buscado)
    return bus
    #lista_remove.remove()
    pass
def find_element(mos):
    alumno_buscado= {}
    for alumno in lista_elemts:
        if alumno['nombre']==mos:
            alumno_buscado = alumno
    return alumno_buscado
    #for para buscar uno solo
    pass
def show_elements():
    return lista_elemts
    #for para buscar todos
    pass
def edit_elemnt(edi):
    alumno_buscado= {}
    for alumno in lista_elemts:
        if alumno['nombre']== edi:
            alumno_buscado = alumno
            id=input("Cambia el nuevo id: \n")
            n=input("Cambia el nombre: \n")
            a=input("Cambia el apellido: \n")
            alumno_buscado['id']=id
            alumno_buscado['nombre']=n
            alumno_buscado['apellido']=a
            return alumno_buscado
    # for o find para buscar
    #editar
    pass

if __name__ == '__main__':
    print("Muestra menu")
    message= f"\n \nCRUD PYTHON: \n Elige una opcion \n 1- AGREGAR ELEMENTO \n 2- ELIMINAR ELEMENTO \n 3- MOSTRAR ELEMENTO \n 4- MOSTRAR TODOS LOS ELEMENTOS \n 5- EDITAR ELEMNTO \n 6- SALIR \n"
    while True:
        opcion= int(input(message))
        if opcion == 1:
            print(f"Ingresa los datos del alumno\n")
            id=int(input("Ingresa el id: "))
            name=input("Ingresa el nombre: ")
            ape=input("Ingresa el apellido: ")
            print(f"Agregado {add_elemet(id, name, ape)} ala lista")

            #print(lista_elemts)
        elif opcion == 2:
            bus=input("Ingresa el nombre para eliminar: ")
            print(f" {remove_elemet(bus)} eliminado de la lista")

            ##Eliminamos el elemto
            # 
        elif opcion == 3:
            mos=input("Ingresa el nombre para buscar: \n")

            print(f"Elemento buscado:\n{find_element(mos)}\n")
        elif opcion == 4:
            print(f"Todos los elemtos:\n{show_elements()}")
        elif opcion == 5:
            edi=input("Ingresa el alumno a editar: ")
            print(f"{edi} Editado\n {edit_elemnt(edi)}")
        ##print(lista_elemts)
        else:
            print("miSQL")
            break