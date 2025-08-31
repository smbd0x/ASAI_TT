{
    'name': 'АРМ Оператора',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Автоматизированное рабочее место оператора',
    'author': 'Kirill',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/operator_task_views.xml',
        'views/operator_task_menus.xml',
        'data/operator_demo.xml',
    ],
    'tests': ['tests/test_operator.py'],
    'installable': True,
    'application': True,
}
