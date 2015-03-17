# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request
from openerp import SUPERUSER_ID
from datetime import datetime
import openerp.tools
import werkzeug
import facebook

class website_facebook_issue(http.Controller):        
    @http.route(['/fb/issue', '/fb/issue/<model("project.issue"):project_issue>'], type='http', auth="public", website=True)
    def facebook_issue(self, project_issue=False, company=False,  **post):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        
        user = request.registry.get('res.users').browse(cr,uid,uid)
        ctx = {
            'user' : request.registry.get('res.users').browse(cr,uid,uid),
            'project_issue' : project_issue,
            'project_issues' : request.registry.get('project.issue').browse(cr,uid,request.registry.get('project.issue').search(cr,uid,[('partner_id','=',user.partner_id.id)]),),
             }
            
            
        return request.render('website_facebook.issue', ctx)  
