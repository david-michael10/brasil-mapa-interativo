import turtle
import pandas

screen = turtle.Screen()
image = "mapa-do-brasil.gif"
screen.addshape(image)
turtle.shape(image)

# def get_coord_mouse_click(x,y):
#     intx = int(x)
#     inty = int(y)
#     print(f"{intx},{inty}")
# turtle.onscreenclick(get_coord_mouse_click)


dados_bruto = pandas.read_csv("coordnates.csv")
estados_lista = dados_bruto.estado.to_list()
total_estados = len(estados_lista)

estados_certos = []
estados_acertados = len(estados_certos)

while estados_acertados <= total_estados:
    input_usuario = screen.textinput(title=f"{len(estados_certos)}/27", prompt="Digite a sigla de um estado").upper()

    if input_usuario == "EXIT":
        faltando = []
        for i in estados_lista:
            if not i in estados_certos:
                faltando.append(i)
        novo_df = pandas.DataFrame(faltando)
        novo_df.to_csv("estados faltando.csv")
        break

    if input_usuario in estados_lista:
        if input_usuario in estados_certos:
            pass
        else:
            estados_certos.append(input_usuario)
            estado = dados_bruto[dados_bruto.estado == input_usuario]

            estado_objeto = turtle.Turtle()
            estado_objeto.hideturtle()
            estado_objeto.penup()
            estado_objeto.goto(estado.x.item(), estado.y.item())
            estado_objeto.write(input_usuario, font=("Arial",10, "bold"))

screen.exitonclick()