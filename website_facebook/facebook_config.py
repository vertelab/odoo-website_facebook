from openerp import models, fields, api, _

class facebook_config_settings(models.TransientModel):
    _name = 'facebook.config.settings'
    _inherit = 'res.config.settings'
    
    name = fields.Char(string="App Name")
    app_id = fields.Char(string="App ID")
    app_pwd = fields.Char(string='App Password')
    fb_website = fields.Char(string='Facebook Account')
