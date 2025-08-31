from odoo import models, fields, api
from datetime import datetime


class OperatorTask(models.Model):
    _name = 'operator.task'
    _description = 'Operator Task'

    name = fields.Char(string='Задание', required=True)
    status = fields.Selection([
        ('ready', 'Готово к работе'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
        ('defect', 'Брак')
    ], string='Статус', default='ready', required=True)
    start_time = fields.Datetime(string='Начало работы')
    end_time = fields.Datetime(string='Конец работы')
    drawing = fields.Binary(string='Чертеж')
    operator_id = fields.Many2one('res.users', string='Оператор', default=lambda self: self.env.user)


    def action_start(self):
        for task in self:
            task.write({
                'status': 'in_progress',
                'start_time': datetime.now()
            })

    def action_done(self):
        for task in self:
            task.write({
                'status': 'done',
                'end_time': datetime.now()
            })

    def action_defect(self):
        for task in self:
            task.write({
                'status': 'defect',
                'end_time': datetime.now()
            })

    def action_show_drawing(self):
        # Пока ничего не делаем
        return True
