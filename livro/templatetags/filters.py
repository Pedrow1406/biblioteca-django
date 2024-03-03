from django import template

register = template.Library()
@register.filter
def mostra_duracao(data_devolucao, data_emprestimo):
    tempo = data_devolucao - data_emprestimo
    return tempo.days