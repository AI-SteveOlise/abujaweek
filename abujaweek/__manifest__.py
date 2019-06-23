# -*- coding: utf-8 -*-
{
    'name': "abuja_week",

    'summary': """
        Abuja Week Modules""",

    'description': """
        Long description of module's purpose
    """,

    'author': "MCEE Solutions",
    'website': "http://www.mceesolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'abujaweek',
    'version': '0.10',


    # any module necessary for this one to work correctly
    'depends': ['base','sale','website','website_event','website_event_sale', ],

    # always loaded
    'data': [
        'views/website_events_template.xml',
        'views/event_registration_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
