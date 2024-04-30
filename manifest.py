{
    'name': 'Vendor Self-Service Portal',
    'version': '1.0',
    'category': 'Vendor',
    'summary': 'Vendor Self-Service Portal for Fatmug Designs',
    'description': 'Allows vendors to view forecasts, submit adjustment requests, and download reports.',
    'depends': ['base', 'sale', 'product', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/vendor_forecast_views.xml',
        'views/vendor_adjustment_request_views.xml',
        'views/vendor_portal_templates.xml',
        'views/report_vendor_forecast.xml',
        'wizards/vendor_adjustment_request_wizard.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}