from IPython.display import display, HTML
import time
import math
import re

# Created at: 23rd October 2018
#         by: Tolga Atam
# v2.1.0 Updated at: 15th March 2021
#         by: Tolga Atam
# from https://github.com/tolgaatam/ColabTurtle/blob/master/ColabTurtle/Turtle.py

# vX.X.X Atualizado por Allen Downey para Think Python 3e

# Módulo para desenhar figuras clássicas de tartaruga em notebooks do Google Colab.
# Usa os recursos HTML da biblioteca IPython para desenhar formas SVG no próprio documento.
# O visual das figuras é inspirado no Blockly Games / Turtle (blockly-games.appspot.com/turtle)

DEFAULT_WINDOW_SIZE = (300, 150)
DEFAULT_SPEED = 6
DEFAULT_TURTLE_VISIBILITY = True
DEFAULT_PEN_COLOR = '#663399'
DEFAULT_TURTLE_COLOR = 'gray'
DEFAULT_TURTLE_DEGREE = 0
DEFAULT_BACKGROUND_COLOR = 'white'
DEFAULT_IS_PEN_DOWN = True
DEFAULT_SVG_LINES_STRING = ""
DEFAULT_PEN_WIDTH = 2
# os 140 nomes de cores que os navegadores modernos aceitam. fonte: https://www.w3schools.com/colors/colors_names.asp
VALID_COLORS = ('black', 'navy', 'darkblue', 'mediumblue', 'blue', 'darkgreen', 'green', 'teal', 'darkcyan', 'deepskyblue', 'darkturquoise', 'mediumspringgreen', 'lime', 'springgreen', 'aqua', 'cyan', 'midnightblue', 'dodgerblue', 'lightseagreen', 'forestgreen', 'seagreen', 'darkslategray', 'darkslategrey', 'limegreen', 'mediumseagreen', 'turquoise', 'royalblue', 'steelblue', 'darkslateblue', 'mediumturquoise', 'indigo', 'darkolivegreen', 'cadetblue', 'cornflowerblue', 'rebeccapurple', 'mediumaquamarine', 'dimgray', 'dimgrey', 'slateblue', 'olivedrab', 'slategray', 'slategrey', 'lightslategray', 'lightslategrey', 'mediumslateblue', 'lawngreen', 'chartreuse', 'aquamarine', 'maroon', 'purple', 'olive', 'gray', 'grey', 'skyblue', 'lightskyblue', 'blueviolet', 'darkred', 'darkmagenta', 'saddlebrown', 'darkseagreen', 'lightgreen', 'mediumpurple', 'darkviolet', 'palegreen', 'darkorchid', 'yellowgreen', 'sienna', 'brown', 'darkgray', 'darkgrey', 'lightblue', 'greenyellow', 'paleturquoise', 'lightsteelblue', 'powderblue', 'firebrick', 'darkgoldenrod', 'mediumorchid', 'rosybrown', 'darkkhaki', 'silver', 'mediumvioletred', 'indianred', 'peru', 'chocolate', 'tan', 'lightgray', 'lightgrey', 'thistle', 'orchid', 'goldenrod', 'palevioletred', 'crimson', 'gainsboro', 'plum', 'burlywood', 'lightcyan', 'lavender', 'darksalmon', 'violet', 'palegoldenrod', 'lightcoral', 'khaki', 'aliceblue', 'honeydew', 'azure', 'sandybrown', 'wheat', 'beige', 'whitesmoke', 'mintcream', 'ghostwhite', 'salmon', 'antiquewhite', 'linen', 'lightgoldenrodyellow', 'oldlace', 'red', 'fuchsia', 'magenta', 'deeppink', 'orangered', 'tomato', 'hotpink', 'coral', 'darkorange', 'lightsalmon', 'orange', 'lightpink', 'pink', 'gold', 'peachpuff', 'navajowhite', 'moccasin', 'bisque', 'mistyrose', 'blanchedalmond', 'papayawhip', 'lavenderblush', 'seashell', 'cornsilk', 'lemonchiffon', 'floralwhite', 'snow', 'yellow', 'lightyellow', 'ivory', 'white')
VALID_COLORS_SET = set(VALID_COLORS)
DEFAULT_TURTLE_SHAPE = 'circle'
VALID_TURTLE_SHAPES = ('turtle', 'circle')
SVG_TEMPLATE = """
      <svg width="{window_width}" height="{window_height}">
        <rect width="100%" height="100%" fill="{background_color}"/>
        {lines}
        {turtle}
      </svg>
    """
TURTLE_TURTLE_SVG_TEMPLATE = """<g visibility="{visibility}" transform="rotate({degrees},{rotation_x},{rotation_y}) translate({turtle_x}, {turtle_y})">
<path style=" stroke:none;fill-rule:evenodd;fill:{turtle_color};fill-opacity:1;" d="M 18.214844 0.632812 C 16.109375 1.800781 15.011719 4.074219 15.074219 7.132812 L 15.085938 7.652344 L 14.785156 7.496094 C 13.476562 6.824219 11.957031 6.671875 10.40625 7.066406 C 8.46875 7.550781 6.515625 9.15625 4.394531 11.992188 C 3.0625 13.777344 2.679688 14.636719 3.042969 15.027344 L 3.15625 15.152344 L 3.519531 15.152344 C 4.238281 15.152344 4.828125 14.886719 8.1875 13.039062 C 9.386719 12.378906 10.371094 11.839844 10.378906 11.839844 C 10.386719 11.839844 10.355469 11.929688 10.304688 12.035156 C 9.832031 13.09375 9.257812 14.820312 8.96875 16.078125 C 7.914062 20.652344 8.617188 24.53125 11.070312 27.660156 C 11.351562 28.015625 11.363281 27.914062 10.972656 28.382812 C 8.925781 30.84375 7.945312 33.28125 8.238281 35.1875 C 8.289062 35.527344 8.28125 35.523438 8.917969 35.523438 C 10.941406 35.523438 13.074219 34.207031 15.136719 31.6875 C 15.359375 31.417969 15.328125 31.425781 15.5625 31.574219 C 16.292969 32.042969 18.023438 32.964844 18.175781 32.964844 C 18.335938 32.964844 19.941406 32.210938 20.828125 31.71875 C 20.996094 31.625 21.136719 31.554688 21.136719 31.558594 C 21.203125 31.664062 21.898438 32.414062 22.222656 32.730469 C 23.835938 34.300781 25.5625 35.132812 27.582031 35.300781 C 27.90625 35.328125 27.9375 35.308594 28.007812 34.984375 C 28.382812 33.242188 27.625 30.925781 25.863281 28.425781 L 25.542969 27.96875 L 25.699219 27.785156 C 28.945312 23.960938 29.132812 18.699219 26.257812 11.96875 L 26.207031 11.84375 L 27.945312 12.703125 C 31.53125 14.476562 32.316406 14.800781 33.03125 14.800781 C 33.976562 14.800781 33.78125 13.9375 32.472656 12.292969 C 28.519531 7.355469 25.394531 5.925781 21.921875 7.472656 L 21.558594 7.636719 L 21.578125 7.542969 C 21.699219 6.992188 21.761719 5.742188 21.699219 5.164062 C 21.496094 3.296875 20.664062 1.964844 19.003906 0.855469 C 18.480469 0.503906 18.457031 0.5 18.214844 0.632812"/>
</g>"""
TURTLE_CIRCLE_SVG_TEMPLATE = """
      <g visibility="{visibility}" transform="rotate({degrees},{rotation_x},{rotation_y}) translate({turtle_x}, {turtle_y})">
        <circle stroke="{turtle_color}" stroke-width="2" fill="transparent" r="5.5" cx="0" cy="0"/>
        <polygon points="0,12 2,9 -2,9" style="fill:{turtle_color};stroke:{turtle_color};stroke-width:2"/>
      </g>
    """


SPEED_TO_SEC_MAP = {1: 1.5, 2: 0.9, 3: 0.7, 4: 0.5, 5: 0.3, 6: 0.18, 7: 0.12, 8: 0.06, 9: 0.04, 10: 0.02, 11: 0.01, 12: 0.001, 13: 0.0001}


# função auxiliar que mapeia valores de velocidade [1,13] para atrasos em ms
def _speedToSec(speed):
    return SPEED_TO_SEC_MAP[speed]


turtle_speed = DEFAULT_SPEED

is_turtle_visible = DEFAULT_TURTLE_VISIBILITY
pen_color = DEFAULT_PEN_COLOR
window_size = DEFAULT_WINDOW_SIZE
turtle_pos = (DEFAULT_WINDOW_SIZE[0] // 2, DEFAULT_WINDOW_SIZE[1] // 2)
turtle_degree = DEFAULT_TURTLE_DEGREE
background_color = DEFAULT_BACKGROUND_COLOR
is_pen_down = DEFAULT_IS_PEN_DOWN
svg_lines_string = DEFAULT_SVG_LINES_STRING
pen_width = DEFAULT_PEN_WIDTH
turtle_shape = DEFAULT_TURTLE_SHAPE

drawing_window = None


# monta a exibição da tartaruga
def make_turtle(speed=DEFAULT_SPEED, width=DEFAULT_WINDOW_SIZE[0], height=DEFAULT_WINDOW_SIZE[1]):
    global window_size
    global drawing_window
    global turtle_speed
    global is_turtle_visible
    global pen_color
    global turtle_color
    global turtle_pos
    global turtle_degree
    global background_color
    global is_pen_down
    global svg_lines_string
    global pen_width
    global turtle_shape

    if isinstance(speed,int) == False or speed not in range(1, 14):
        raise ValueError('speed must be an integer in interval [1,13]')
    turtle_speed = speed

    window_size = width, height
    if not (isinstance(window_size, tuple) and
            isinstance(window_size[0], int) and
            isinstance(window_size[1], int)):
        raise ValueError('window_size must be a tuple of 2 integers')

    is_turtle_visible = DEFAULT_TURTLE_VISIBILITY
    pen_color = DEFAULT_PEN_COLOR
    turtle_color = DEFAULT_TURTLE_COLOR
    turtle_pos = (window_size[0] // 2, window_size[1] // 2)
    turtle_degree = DEFAULT_TURTLE_DEGREE
    background_color = DEFAULT_BACKGROUND_COLOR
    is_pen_down = DEFAULT_IS_PEN_DOWN
    svg_lines_string = DEFAULT_SVG_LINES_STRING
    pen_width = DEFAULT_PEN_WIDTH
    turtle_shape = DEFAULT_TURTLE_SHAPE

    drawing_window = display(HTML(_generateSvgDrawing()), display_id=True)


# função auxiliar que gera a string SVG da tartaruga
def _generateTurtleSvgDrawing():
    if is_turtle_visible:
        vis = 'visible'
    else:
        vis = 'hidden'

    turtle_x = turtle_pos[0]
    turtle_y = turtle_pos[1]
    degrees = turtle_degree
    template = ''

    if turtle_shape == 'turtle':
        turtle_x -= 18
        turtle_y -= 18
        degrees += 90
        template = TURTLE_TURTLE_SVG_TEMPLATE
    else: #circle
        degrees -= 90
        template = TURTLE_CIRCLE_SVG_TEMPLATE

    return template.format(turtle_color=turtle_color, turtle_x=turtle_x, turtle_y=turtle_y, \
                                      visibility=vis, degrees=degrees, rotation_x=turtle_pos[0], rotation_y=turtle_pos[1])


# função auxiliar que gera a string SVG inteira
def _generateSvgDrawing():
    return SVG_TEMPLATE.format(window_width=window_size[0], window_height=window_size[1],
                               background_color=background_color, lines=svg_lines_string,
                               turtle=_generateTurtleSvgDrawing())


# funções auxiliares para atualizar a tela com as posições, ângulos e linhas mais recentes.
def _updateDrawing():
    if drawing_window == None:
        raise AttributeError("Display has not been initialized yet. Call make_turtle() before using.")
    time.sleep(_speedToSec(turtle_speed))
    drawing_window.update(HTML(_generateSvgDrawing()))


# função auxiliar para qualquer movimento até 'new_pos' e para desenhar linhas se a caneta estiver abaixada
def _moveToNewPosition(new_pos):
    global turtle_pos
    global svg_lines_string

    # arredonda new_pos para eliminar erros de ponto flutuante.
    new_pos = ( round(new_pos[0],3), round(new_pos[1],3) )

    start_pos = turtle_pos
    if is_pen_down:
        svg_lines_string += """<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-linecap="round" style="stroke:{pen_color};stroke-width:{pen_width}"/>""".format(
            x1=start_pos[0], y1=start_pos[1], x2=new_pos[0], y2=new_pos[1], pen_color=pen_color, pen_width=pen_width)

    turtle_pos = new_pos
    _updateDrawing()


# faz a tartaruga avançar 'units' unidades
def forward(units):
    if not isinstance(units, (int,float)):
        raise ValueError('units must be a number.')

    alpha = math.radians(turtle_degree)
    ending_point = (turtle_pos[0] + units * math.cos(alpha), turtle_pos[1] + units * math.sin(alpha))

    _moveToNewPosition(ending_point)

fd = forward # alias

# faz a tartaruga recuar 'units' unidades
def backward(units):
    if not isinstance(units, (int,float)):
        raise ValueError('units must be a number.')
    forward(-1 * units)

bk = backward # alias
back = backward # alias


# faz a tartaruga girar 'degrees' graus à direita (NÃO radianos)
def right(degrees):
    global turtle_degree

    if not isinstance(degrees, (int,float)):
        raise ValueError('degrees must be a number.')

    turtle_degree = (turtle_degree + degrees) % 360
    _updateDrawing()

rt = right # alias

# faz a tartaruga apontar para uma direção dada
def face(degrees):
    global turtle_degree

    if not isinstance(degrees, (int,float)):
        raise ValueError('degrees must be a number.')

    turtle_degree = degrees % 360
    _updateDrawing()

setheading = face # alias
seth = face # alias

# faz a tartaruga girar 'degrees' graus à direita (NÃO radianos; esta biblioteca ainda não aceita radianos)
def left(degrees):
    if not isinstance(degrees, (int,float)):
        raise ValueError('degrees must be a number.')
    right(-1 * degrees)

lt = left

# levanta a caneta para que os movimentos seguintes não desenhem
def penup():
    global is_pen_down

    is_pen_down = False
    # TODO: decidir se o timeout deve vir depois de levantar a caneta
    # _updateDrawing()

pu = penup # alias
up = penup # alias

# abaixa a caneta para que os movimentos seguintes passem a desenhar
def pendown():
    global is_pen_down

    is_pen_down = True
    # TODO: decidir se o timeout deve vir depois de abaixar a caneta
    # _updateDrawing()

pd = pendown # alias
down = pendown # alias

def isdown():
    return is_pen_down

# atualiza a velocidade dos movimentos, [1,13]
# se o argumento for omitido, devolve a velocidade.
def speed(speed = None):
    global turtle_speed

    if speed is None:
        return turtle_speed

    if isinstance(speed,int) == False or speed not in range(1, 14):
        raise ValueError('speed must be an integer in the interval [1,13].')
    turtle_speed = speed
    # TODO: decidir se o timeout deve vir depois de mudar a velocidade
    # _updateDrawing()


# move a tartaruga para a coordenada x indicada; y permanece o mesmo
def setx(x):
    if not isinstance(x, (int,float)):
        raise ValueError('new x position must be a number.')
    if x < 0:
        raise ValueError('new x position must be non-negative.')
    _moveToNewPosition((x, turtle_pos[1]))


# move a tartaruga para a coordenada y indicada; x permanece o mesmo
def sety(y):
    if not isinstance(y, (int,float)):
        raise ValueError('new y position must be a number.')
    if y < 0:
        raise ValueError('new y position must be non-negative.')
    _moveToNewPosition((turtle_pos[0], y))


def home():
    global turtle_degree

    turtle_degree = DEFAULT_TURTLE_DEGREE
    _moveToNewPosition( (window_size[0] // 2, window_size[1] // 2) ) # isto cuida de atualizar o desenho.

# obtém a coordenada x atual da tartaruga
def getx():
    return(turtle_pos[0])

xcor = getx # alias

# obtém a coordenada y atual da tartaruga
def gety():
    return(turtle_pos[1])

ycor = gety # alias

# obtém a posição atual da tartaruga como vetor (x, y)
def position():
    return turtle_pos

pos = position # alias

# obtém o ângulo atual da tartaruga
def getheading():
    return turtle_degree

heading = getheading # alias

# move a tartaruga para a coordenada x-y indicada
def moveto(x, y=None):
    if isinstance(x, tuple) and y is None:
        if len(x) != 2:
            raise ValueError('the tuple argument must be of length 2.')

        y = x[1]
        x = x[0]

    if not isinstance(x, (int,float)):
        raise ValueError('new x position must be a number.')
    if x < 0:
        raise ValueError('new x position must be non-negative')
    if not isinstance(y, (int,float)):
        raise ValueError('new y position must be a number.')
    if y < 0:
        raise ValueError('new y position must be non-negative.')
    _moveToNewPosition((x, y))

goto = moveto # alias
setpos = moveto # alias
setposition = moveto # alias

# salta para um lugar dado sem deixar rastro
def jumpto(x, y=None):
    flag = is_pen_down
    penup()
    goto(x, y)
    if flag:
        pendown()

# torna a tartaruga visível
def showturtle():
    global is_turtle_visible

    is_turtle_visible = True
    _updateDrawing()

st = showturtle # alias

# torna a tartaruga invisível
def hideturtle():
    global is_turtle_visible

    is_turtle_visible = False
    _updateDrawing()

ht = hideturtle # alias

def isvisible():
    return is_turtle_visible

def _validateColorString(color):
    if color in VALID_COLORS_SET: # 140 nomes de cores HTML predefinidos
        return True
    if re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", color): # código hexadecimal de 3 ou 6 dígitos
        return True
    if re.search("rgb\(\s*(?:(?:\d{1,2}|1\d\d|2(?:[0-4]\d|5[0-5]))\s*,?){3}\)$", color): # código de cor RGB
        return True
    return False

def _validateColorTuple(color):
    if len(color) != 3:
        return False
    if not isinstance(color[0], int) or not isinstance(color[1], int) or not isinstance(color[2], int):
        return False
    if not 0 <= color[0] <= 255 or not 0 <= color[1] <= 255 or not 0 <= color[2] <= 255:
        return False
    return True

def _processColor(color):
    if isinstance(color, str):
        color = color.lower()
        if not _validateColorString(color):
            raise ValueError('color is invalid. it can be a known html color name, 3-6 digit hex string or rgb string.')
        return color
    elif isinstance(color, tuple):
        if not _validateColorTuple(color):
            raise ValueError('color tuple is invalid. it must be a tuple of three integers, which are in the interval [0,255]')
        return 'rgb(' + str(color[0]) + ',' + str(color[1]) + ',' + str(color[2]) + ')'
    else:
        raise ValueError('the first parameter must be a color string or a tuple')

# muda a cor de fundo da área de desenho
# sem parâmetros, devolve a cor de fundo atual
def bgcolor(color = None, c2 = None, c3 = None):
    global background_color

    if color is None:
        return background_color
    elif c2 is not None:
        if c3 is None:
            raise ValueError('if the second argument is set, the third arguments must be set as well to complete the rgb set.')
        color = (color, c2, c3)

    background_color = _processColor(color)
    _updateDrawing()


# muda a cor da caneta
# sem parâmetros, devolve a cor atual da caneta
def color(color = None, c2 = None, c3 = None):
    global pen_color

    if color is None:
        return pen_color
    elif c2 is not None:
        if c3 is None:
            raise ValueError('if the second argument is set, the third arguments must be set as well to complete the rgb set.')
        color = (color, c2, c3)

    pen_color = _processColor(color)
    _updateDrawing()

pencolor = color

# muda a largura das linhas desenhadas pela tartaruga, em pixels
# se a função for chamada sem argumentos, devolve a largura atual
def width(width = None):
    global pen_width

    if width is None:
        return pen_width
    else:
        if not isinstance(width, int):
            raise ValueError('new width position must be an integer.')
        if not width > 0:
            raise ValueError('new width position must be positive.')

        pen_width = width
        # TODO: decidir se o timeout deve vir depois de mudar pen_width
        # _updateDrawing()

# pensize é um alias de width
pensize = width

# apaga texto e desenho da tela
def clear():
    global svg_lines_string

    svg_lines_string = ""
    _updateDrawing()

def write(obj, **kwargs):
    global svg_lines_string
    global turtle_pos
    text = str(obj)
    font_size = 12
    font_family = 'Arial'
    font_type = 'normal'
    align = 'start'

    if 'align' in kwargs and kwargs['align'] in ('left', 'center', 'right'):
        if kwargs['align'] == 'left':
            align = 'start'
        elif kwargs['align'] == 'center':
            align = 'middle'
        else:
            align = 'end'

    if "font" in kwargs:
        font = kwargs["font"]
        if len(font) != 3 or isinstance(font[0], int) == False or isinstance(font[1], str) == False or font[2] not in {'bold','italic','underline','normal'}:
            raise ValueError('font parameter must be a triplet consisting of font size (int), font family (str) and font type. font type can be one of {bold, italic, underline, normal}')
        font_size = font[0]
        font_family = font[1]
        font_type = font[2]

    style_string = ""
    style_string += "font-size:" + str(font_size) + "px;"
    style_string += "font-family:'" + font_family + "';"

    if font_type == 'bold':
        style_string += "font-weight:bold;"
    elif font_type == 'italic':
        style_string += "font-style:italic;"
    elif font_type == 'underline':
        style_string += "text-decoration: underline;"


    svg_lines_string += """<text x="{x}" y="{y}" fill="{fill_color}" text-anchor="{align}" style="{style}">{text}</text>""".format(x=turtle_pos[0], y=turtle_pos[1], text=text, fill_color=pen_color, align=align, style=style_string)

    _updateDrawing()

def shape(shape=None):
    global turtle_shape
    if shape is None:
        return turtle_shape
    elif shape not in VALID_TURTLE_SHAPES:
        raise ValueError('shape is invalid. valid options are: ' + str(VALID_TURTLE_SHAPES))

    turtle_shape = shape
    _updateDrawing()

# devolve a largura da janela da tartaruga
def window_width():
    return window_size[0]

# devolve a altura da janela da tartaruga
def window_height():
    return window_size[1]
