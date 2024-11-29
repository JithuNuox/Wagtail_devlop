from django.utils.translation import gettext_lazy as _

PAGINATION_PERPAGE=10
IND_TIMEZONE = 'Asia/india'

# STOCK TYPE 
POPULAR = 1
FOREX = 2
ENERGIES = 3 
INDICES = 4
COMMODITIES = 5
SHARES = 6
STOCK_TYPE = ((POPULAR,_('Popular')),(FOREX,_('Forex')),(COMMODITIES,_('Commodities')),(INDICES,_('Indices')),(ENERGIES,_('Energies')),(SHARES,_('Shares')))

MENU_CACHE_TIMEOUT = 60 * 60 * 24 # 1 day timeout
FOOTER_CACHE_TIMEOUT = 60 * 60 * 24 # 1 day timeout



#api urls corresponding to models
# API_URLS = [
# 	    ('aboutpage', 'about-us/',),
#         ('servicepage', 'service/',),
#         ('tradingpage', 'trading/',),
#         ('productpage', 'product/',),
#         ('partnershippage','partnership/',),
#         ('otherpage','secondary-pages/',),
#         ('learningcontentpage','learning-hub/page/',),
#         ('learninglinkpage','learning-hub/link-page/',),        
#         ('blogindexpage', 'learn-to-invest/',),
#         ('webinarindexpage', 'webinars/',),
#         ('economicreportindexpage', 'economic-reports/',),
#         ('technicalanalysisindexpage', 'technical-analysis/',),
#         ('marketupdateindexpage', 'market-updates/',),
#         ('workshopindexpage', 'workshop/',),
#         ('pressreleaseindexpage', 'press-release/',),
#         ('activityindexpage', 'activities/',),
#         ('awardindexpage', 'awards/',),
#     ]







CARD_CHOICES = [
	    ('2', _('2 cards per row'),),
        ('3', _('3 cards per row'),),
        ('4', _('4 cards per row'),),
    ]
    


ALIGNMENT_CHOICES = [
        ('center', _('Center'),),
	    ('right', _('Right'),),        
        ('left', _('Left'),),
    ]

# Define a list of social media options
SOCIAL_MEDIA_CHOICES = [
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
    ('linkedin', 'LinkedIn'),
    ('instagram', 'Instagram'),
    ('youtube', 'YouTube'),
]


# OTHER_FORM_TYPES = [
#     ('CONTACT','CONTACT'),
#     ('ENQUIRY','ENQUIRY'),
#     ('REQUEST_DEMO','REQUEST DEMO')
# ]

# FROM_EMAILS = [
#     ('web','web@noorcapital.ae'),
#     ('institutions','institutions@noorcapital.ae'),
#     ('sales','sales@noorcapital.ae')
# ]


