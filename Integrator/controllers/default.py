# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
from gluon import *
import scipy.integrate as integrate
from scipy.integrate import odeint
import numpy as np





def index():
   
    return locals()



@auth.requires_membership('managers')
def manage():
   
    eqgrid=SQLFORM.grid(db.jednadzbe)
    return locals()





@auth.requires_login()
def neweq():
    
    db.jednadzbe.kreiran.default=request.now
    db.jednadzbe.kreiran.writable=False
    db.jednadzbe.kreiran.readable=False
    
    db.jednadzbe.vlasnik.default=auth.user.first_name
    db.jednadzbe.vlasnik.writable=False
    db.jednadzbe.vlasnik.readable=False
    
    db.jednadzbe.vlasnikID.default=auth.user.id
    db.jednadzbe.vlasnikID.writable=False
    db.jednadzbe.vlasnikID.readable=False
    
    db.jednadzbe.formula.default="def model(y,t):\n    dydt=3*t\n    return dydt"
    
   
    
    
    
    
    form=SQLFORM(db.jednadzbe).process()
  
    rows=db(db.jednadzbe).select()
    if form.accepted:
             
        redirect(URL('eqoverview'))
    elif form.errors:
            pass
    return locals()

def eqoverview():
    
    rows=db(db.jednadzbe).select()
    return locals()


def displayeq():
    jed=db.jednadzbe(request.args(0,cast=int))
    start=float(jed.pocetak)
    end=float(jed.kraj)

    funkcija=jed.formula
    exec(jed.formula)
    y0=jed.pocetni
    t=np.linspace(start,end)
    result=odeint(model,y0,t)

    
    
    
    
    
    if auth.is_logged_in():
        db.komentari.Autor.default=auth.user.first_name
        
    else:
        db.komentari.Autor.default="Anonimus"
    db.komentari.Autor.writable=False
    db.komentari.Autor.readable=True
    db.komentari.vlasnikID.default=jed.vlasnikID      
    db.komentari.vlasnikID.writable=False
    db.komentari.vlasnikID.readable=False
    db.komentari.FormulaID.writable=False
    db.komentari.FormulaID.readable=False
    db.komentari.FormulaID.default=jed.id
    db.komentari.kreiran.default=request.now
    db.komentari.kreiran.readable=False
    db.komentari.kreiran.writable=False
    commentform=SQLFORM(db.komentari).process()
    
    
    rows=db(db.komentari.FormulaID==jed.id).select()
    
    return locals()





# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    if auth.is_logged_in():
        rows=db(db.jednadzbe.vlasnikID ==auth.user.id).select()
        commrows=db(db.komentari.vlasnikID==auth.user.id).select()
    form=auth()
    return locals()

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
