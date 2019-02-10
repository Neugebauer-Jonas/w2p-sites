# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
      
      (T('Home'), False, URL('default', 'hrdatabase'), []),
       (T('Hr To IW'), False, URL('default', 'HRtoIW',args=100), []),
      (T('Hr To EN'), False, URL('default', 'HRtoEN',args=100), []),
      (T('Hr To DE'), False, URL('default','HRtoDE',args=100), []),
     (T('Hr To IT'), False, URL('default','HRtoIT',args=100), []),
    (T('Hr To FR'), False, URL('default','HRtoFR',args=100), []),
    (T('Hrvatski'), False, URL('default', 'hrvatski',args=100), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------
