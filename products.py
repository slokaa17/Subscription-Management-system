from odoo import models, fields


class SubscriptionProduct(models.Model):
    _name = 'subscription.product'
    _description = 'Subscription Product'
    _order = 'name'

    name = fields.Char(
        string='Product Name',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    price = fields.Float(
        string='Product Price',
        required=True,
        default=0.0
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )