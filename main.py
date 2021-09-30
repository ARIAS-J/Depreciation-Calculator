
def depreciacion_linea_recta():
    print("Metodo Linea Recta")

    valor_del_activo = int(input("\nIngrese el valor del activo: "))
    vida_util = int(input("Ingrese la vida util del activo: "))

    linea_recta = valor_del_activo / vida_util

    print(f"\nLa Depreciacion En Linea recta es: {linea_recta}")



def depreciacion_digito_años():
    print("Metodo Suma de los Digitos")

    valor_del_activo = int(input("\nIngrese el valor del activo: "))
    vida_util = int(input("Ingrese la vida util del activo: "))

    suma_digitos = vida_util * (vida_util + 1) / 2

    for i in range(1, vida_util + 1):

        digitos_años = vida_util / suma_digitos * valor_del_activo

        print(f"Año {i} = {round(digitos_años,2)}")

        vida_util =  vida_util - 1


print("=============================================")
print("                [Bienvenido]                 ")
print("=============================================")

print("\nCalculadora de Depreciacion de Activo Fijo.")
print("\n=============================================")
print("Opcion #1: Metodo Linea Recta.\nOpcion #2: Metodo Suma de los Digitos.")
print("=============================================")

opcion = int(input("\nOpcion: "))

if opcion == 1:
    depreciacion_linea_recta()
elif opcion == 2:
    depreciacion_digito_años()
else:
    exit(0)





# ((`~\\_  __/'~/   .' .'`.`:';,". '
#  `\`  `\/  //'  .   .' `.`:;,  ,
#    `\`    //             `!'  '
#      \\  '/   ,,----------"--.
#     ` `\  \\,/,           \ww \
#    `   \\               _ >(@, \
#  `  , `.`\     .``,=-   (_______)
#    .  . `.\     \\   ,   \====/
#        ``.`\     `~~~     `---)
#             -------------------  {𐐒∀𐐒⅄ WH∀LE}

