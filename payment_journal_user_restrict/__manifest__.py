
{
    'name': 'Account Journal User Restrict',
    'version': '6.0.0',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://www.youtube.com/playlist?list=PLXFpENL3b6WU9TzMdawrHJsUBqMDXkcbn',
    'summary': """Account Journal User Restrict confirm""",
    'description': """
        In the standard odoo, 
        any user with accountant group policy can confirm cash and bank movements,
        whether send, receipt, or internal transfer between bank and cash journals,
        but with this module, the user associated with the cash or 
        bank journal can only confirm the bank and cash movement (exchange - receipt) if this book Among his powers,
        but if the movement is a bank and cash transfer between the bank and cash journals, then the user has the right only to send money
        from the book allowed to him and confirm the receipt of money for the authorized user,
        the bank and cash book receiving the money, and if the user has rights on the two journals (the sending book and the receiving book) 
        then he can make the bank and cash transfer Between the two journals and the appropriation for the bank and cash movement as well,
        as he has rights over the two journals together.
        """,
    'depends': ['base','account'],
    'data': [
        'views/view.xml',
    ],
    'images': ['static/description/logo.PNG'],
    'installable': True,
    'auto_install': False,
    'application': False,
    "price": 50.0,
    "currency": 'EUR',
}
