from openerp import models, fields, api, _

class website_config_settings(models.TransientModel):
    _name = 'facebook.config.settings'
    _inherit = 'res.config.settings'
    
    app_id= fields.Many2one('App', string="App", required=True),
    app_pwd=fields.Char(string='App Password')
    name=fields.Related('app_id', 'name', type="char", string="App Name"),
    fb_website=fields.Related('appe_id', 'fb_website', type="char", string='Facebook Account'),

    def on_change_website_id(self, cr, uid, ids, website_id, context=None):
        website_data = self.pool.get('website').read(cr, uid, [app_id], [], context=context)[0]
        values = {'name': website_data['name']}
        for fname, v in website_data.items():
            if fname in self._columns:
                values[fname] = v[0] if v and self._columns[fname]._type == 'Many2one' else v
        return {'value' : values}

    # FIXME in trunk for god sake. Change the fields above to fields.char instead of fields.related, 
    # and create the function set_website who will set the value on the website_id
    # create does not forward the values to the related many2one. Write does.
    def create(self, cr, uid, vals, context=None):
        config_id = super(facebook_config_settings, self).create(cr, uid, vals, context=context)
        self.write(cr, uid, config_id, vals, context=context)
        return config_id

    _defaults = {
        'app_id': lambda self,cr,uid,c: self.pool.get('website').search(cr, uid, [], context=c)[0],
    }
