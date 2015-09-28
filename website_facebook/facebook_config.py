from openerp.osv import fields, osv

class facebook_config_settings(osv.osv_memory):
    _name = 'facebook.config.settings'
    _inherit = 'res.config.settings'
    
    _columns = {
    'app_id': fields.many2one("app", string="App ID"),
    'fb_id' : fields.related("app_id", "App ID", string="Facebook ID", type="char"),
    'name': fields.related("app_id", "name", string="App Name", type="char"),
    'app_pwd':  fields.related("app_id", "app_pwd" ,string='App Password', type="char"),
    'fb_website': fields.related("app_id", "fb_website", string='Facebook Account', type="char"),
    }
    
    def on_change_app_id(self, cr, uid, ids, app_id, context=None):
        website_data = self.pool.get('facebook.config.settings').read(cr, uid, [app_id], [], context=context)[0]
        values = {'name': website_data['name']}
        for fname, v in website_data.items():
            if fname in self._columns:
                values[fname] = v[0] if v and self._columns[fname]._type == 'many2one' else v
        return {'value' : values}
    
    def create(self, cr, uid, vals, context=None):
        config_id = super(facebook_config_settings, self).create(cr, uid, vals, context=context)
        self.write(cr, uid, config_id, vals, context=context)
        return config_id
