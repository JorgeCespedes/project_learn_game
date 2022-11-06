lista_preguntas = [
{
'pregunta' : '¿Cuánto es 1 + 3?',
'alternativa' : [2, 4],
'respuesta' : 4,
},
{
'pregunta' : '¿Cuánto suman los ángulos internos de un triángulo?',
'alternativa' : [180, 360],
'respuesta' : 180,
},
{
'pregunta' : 'Resuelve el valor de 4!',
'alternativa' : [16, 24],
'respuesta' : 24,
},
{
'pregunta' : '¿Cuánto es 2 * ( 5 - 2) ?',
'alternativa' : [6, 1],
'respuesta' : 6,
},
{
'pregunta' : '¿Cuánto es pow(2, 3)?',
'alternativa' : [6, 8],
'respuesta' : 8,
},
{
'pregunta': '¿Cuánto es 1 + 2: ?',
'alternativa': [2, 3],
'respuesta': 3,
},
{
'pregunta': '¿Cuánto es 2 * 2: ?',
'alternativa': [4 , 15],
'respuesta': 4,
},
{
'pregunta': '¿Cuánto es 5 * (2 + 1): ?',
'alternativa': [2, 15],
'respuesta': 15,
},
{
'pregunta': '¿Cuánto es (2 * 3) - 1: ?',
'alternativa': [8 , 5],
'respuesta': 5,
},
{
'pregunta': '¿Cuánto es 15 - 12: ?',
'alternativa': [2, 3],
'respuesta': 3,
},
{
'pregunta': '¿Cuánto es 2 * 2 * 2: ?',
'alternativa': [8 , 5],
'respuesta': 8,
},
{
'pregunta': '¿Cuánto es 15 + 12: ?',
'alternativa': [21, 27],
'respuesta': 27,
},
{
'pregunta': '¿Cuánto es 2 * 3 * 4: ?',
'alternativa': [24 , 25],
'respuesta': 24,
},
{
'pregunta': '¿Cuánto es 4!: ?',
'alternativa': [23 , 24],
'respuesta': 24,
},
{
'pregunta': '¿Cuánto es 2 * 3 - 4: ?',
'alternativa': [2 , 1],
'respuesta': 2,
},
]





def preguntas(lista_preguntas):
    preguntas = [ p['pregunta'] for p in lista_preguntas ]
    return preguntas

def alternativas(lista_preguntas):
    alternativas = [ a['alternativa'] for a in lista_preguntas ]
    return alternativas

def respuestas(lista_preguntas):
    respuestas = [ r['respuesta'] for r in lista_preguntas ]
    return respuestas