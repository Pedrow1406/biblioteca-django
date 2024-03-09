from django import template
from datetime import date
register = template.Library()
@register.filter
def mostra_duracao(data_devolucao, data_emprestimo):
    if all((isinstance(data_devolucao, date),isinstance(data_emprestimo, date))):
        duracao = (data_devolucao - data_emprestimo).days
        if duracao == 1:
            return f'{duracao} dia'
        elif duracao == 0 or 1 < duracao < 7:
            return f'{duracao} dias'
        elif duracao >= 7 and duracao <= 13:
            duracao //= 7
            return f'{duracao} semana'
        elif 14 <= duracao <= 30:
            duracao //=7
            return f'{duracao} semanas'
        elif duracao > 30 and duracao < 60:
            duracao //= 30
            return f'{duracao} mês'
        elif duracao >= 60 and duracao < 365: 
            duracao //= 30
            return f'{duracao} meses'
        elif 365 <= duracao < 730:
            duracao //= 365
            return f'{duracao} ano'
        duracao //= 365
        return f'{duracao} anos'
    