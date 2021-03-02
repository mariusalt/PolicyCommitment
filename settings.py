from os import environ
import dj_database_url
import os
#from boto.mturk import qualification

import otree.settings
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


# DATABASES = {
#     'default': dj_database_url.config(
#         # Rather than hardcoding the DB parameters here,
#         # it's recommended to set the DATABASE_URL environment variable.
#         # This will allow you to use SQLite locally, and postgres/mysql
#         # on the server
#         # Examples:
#         export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#         # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME
#         export REDIS_URL=redis://localhost:6379
#         # fall back to SQLite if the DATABASE_URL env var is missing
#         # default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
#     )
# }

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
 #   'use_browser_bots':True,
}

SESSION_CONFIGS = [
    #{
    #    'name': 'public_goods',
    #    'display_name': "Public Goods",
    #    'num_demo_participants': 3,
    #    'app_sequence': ['public_goods', 'payment_info'],
    #},
        {
         'name': 'firstround',
         'display_name': "Real Effort Task",
         'num_demo_participants': 4,
         'app_sequence': ['Introduction1','pebs1','Introduction2','Introduction2zwei','mail'],
    }, 
      {
         'name': 'firstround1',
         'display_name': "testReal Effort Task",
         'num_demo_participants': 13,
         'app_sequence': ['Introduction1','Introduction2'],
    }, 
    {
         'name': 'pebs0',
         'display_name': "pebs0",
         'num_demo_participants': 60,
         'app_sequence': ['pebs0'],
    },
            {
         'name': 'ques',
         'display_name': "ques",
         'num_demo_participants': 60,
         'app_sequence': ['ques'],
    }, 
                {
         'name': 'quesundpebs',
         'display_name': "quesundpebs",
         'num_demo_participants': 60,
         'app_sequence': ['ques',"pebs0"],
    },
            {
         'name': 'intro',
         'display_name': "intro",
         'num_demo_participants': 5,
         'app_sequence': ['Introduction21','pebs1','decision2'],
    },
    {
         'name': 'last_part',
         'display_name': "last_part",
         'num_demo_participants': 50,
         'app_sequence': ['Introduction21','pebs1','decision2','ques','pebs0'],
    },
        {
         'name': 'zwei',
         'display_name': "zwei",
         'num_demo_participants': 4,
         'app_sequence': ['Introduction2zwei'],
    },
        {
         'name': 'kcount',
         'display_name': "kcount",
         'num_demo_participants': 50,
         'app_sequence': ['kcount'],
    },
           
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '*n6csl6k*yqmed_jdub%97rs_!ew($yg6q_7)uod%(6r(yh#+y'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

ROOM_DEFAULTS = {}
ROOMS=[
{
    'name': 'UWM',
    'display_name': 'UWE',
    
},
{
    'name':'lab',
    'display_name':'Experimental Economics Lab',
},
]
