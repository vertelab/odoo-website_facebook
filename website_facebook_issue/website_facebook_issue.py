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

import logging
_logger = logging.getLogger(__name__)

class website_facebook_issue(http.Controller):
    @http.route(['/fb/issue', '/fb/issue/<model("project.issue"):project_issue>'], type='http', auth="public", website=True)
    def facebook_issue(self, project_issue=False, **post):
       
        _logger.info(request.httprequest.cookies)
        
        user = request.env['res.users'].browse(request.uid)
        facebook_app_id = request.env['ir.config_parameter'].search([("key","=","website_facebook.app_id")])
        facebook_app_secret = request.env['ir.config_parameter'].search([("key","=","website_facebook.app_secret")])
        _logger.info(facebook_app_id.value)
        _logger.info(facebook_app_secret.value)
        cookie = facebook.get_user_from_cookie(
                request.httprequest.cookies, facebook_app_id.value, facebook_app_secret.value)
        
        _logger.info(cookie)
        
        ctx = {
            'user' : user,
            'app_id' : facebook_app_id.value,
            'app_secret' : facebook_app_secret.value,
            'project_issue' : project_issue,
            'project_issues' : request.env['project.issue'].search([('partner_id','=',user.partner_id.id)]),
             }
            
        return request.render('website_facebook.issue', ctx)

    #~ def current_user(self):
        #~ """Returns the active user, or None if the user has not logged in."""   
        #~ if not hasattr(self, "_current_user"):
            #~ self._current_user = None
            #~ cookie = facebook.get_user_from_cookie(
                #~ request.cookies.get(), FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
       #~ 
            #~ if cookie:
                #~ # Store a local instance of the user data so we don't need
                #~ # a round-trip to Facebook on every request
                #~ user = User.get_by_key_name(cookie["uid"])
           #~ 
                #~ if not user:
                    #~ graph = facebook.GraphAPI(cookie["access_token"])
                    #~ profile = graph.get_object("me")
                    #~ user = User(key_name=str(profile["id"]),
                                #~ id=str(profile["id"]),
                                #~ name=profile["name"],
                                #~ profile_url=profile["link"],
                                #~ access_token=cookie["access_token"])
                    #~ user.put()
               #~ 
                #~ elif user.access_token != cookie["access_token"]:
                    #~ user.access_token = cookie["access_token"]
                    #~ user.put()
                #~ self._current_user = user
                #~ 
        #~ return self._current_user
