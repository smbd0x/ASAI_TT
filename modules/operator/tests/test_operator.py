from odoo.tests.common import TransactionCase


class TestOperatorTask(TransactionCase):
    def setUp(self):
        super().setUp()
        self.task = self.env['operator.task'].create({'name': 'Test Task'})

    def test_start_done_defect(self):
        self.task.action_start()
        self.assertEqual(self.task.status, 'in_progress')
        self.assertIsNotNone(self.task.start_time)

        self.task.action_done()
        self.assertEqual(self.task.status, 'done')
        self.assertIsNotNone(self.task.end_time)

        t2 = self.env['operator.task'].create({'name': 'Test Task 2'})
        t2.action_start()
        t2.action_defect()
        self.assertEqual(t2.status, 'defect')
