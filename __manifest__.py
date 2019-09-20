# -*- coding: utf-8 -*-
{
    'name': "runbot",
    'summary': "Runbot",
    'description': "Runbot for Odoo 11.0",
    'author': "Odoo SA",
    'website': "http://runbot.odoo.com",
    'category': 'Website',
    'version': '4.4',
    'depends': ['website', 'base'],
    'data': [
        'security/runbot_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
        'views/assets.xml',
        'views/repo_views.xml',
        'views/branch_views.xml',
        'views/build_views.xml',
        'views/host_views.xml',
        'views/build_error_views.xml',
        'views/error_log_views.xml',
        'views/config_views.xml',
        'views/res_config_settings_views.xml',
        'templates/frontend.xml',
        'templates/build.xml',
        'templates/assets.xml',
        'templates/dashboard.xml',
        'templates/nginx.xml',
        'templates/badge.xml',
        'templates/branch.xml',
        'data/runbot_build_config_data.xml',
        'data/build_parse.xml',
        'data/runbot_error_regex_data.xml',
        'data/error_link.xml',
    ],
}