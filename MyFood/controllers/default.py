# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

@request.restful()
def api():
    response.view = 'generic.json'
    def GET(tablename, broj):
        rows=db2(db2.HR).select().sort(lambda row: row.BROJ)
        return locals()

#def POST(tablename, **fields):
#        if not tablename == 'person':
#            raise HTTP(400)
#        return db.person.validate_and_insert(**fields)

#    def PUT(*args, **vars):
#        return dict()
#    def DELETE(*args, **vars):
#        return dict()
    return locals()










# ---- example index page ----
def index():
    redirect(URL('hrdatabase',))
    
 
    return locals()


@auth.requires_login()
@auth.requires_membership('admin')
def HRtoIW():
    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    rowsIW=db2.IW(db2.IW.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoIW',args=(1+request.args(0,cast=int))))
    else: pass


    db2.HR.BROJ.default=rows.BROJ
    db2.HR.NAZIV.writeble=False
    db2.HR.NAZIV.default=rows.NAZIV
    db2.HR.OPIS.default=rows.OPIS
    db2.HR.Funkcija.default=rows.Funkcija
    db2.HR.PAZI.default=rows.PAZI
    db2.HR.OPASNOST.default=rows.OPASNOST
    db2.IW.id.readable=False
    if not rowsIW:
        db2.IW.BROJ.default=rows.BROJ
    else:
        db2.IW.BROJ.default=rowsIW.BROJ
        db2.IW.NAZIV.default=rowsIW.NAZIV
        db2.IW.OPIS.default=rowsIW.OPIS
        db2.IW.PAZI.default=rowsIW.PAZI
        db2.IW.Funkcija.default=rowsIW.Funkcija
        pass
    db2.IW.OPASNOST.default=rows.OPASNOST
    db2.IW.OPASNOST.writeable=False
   


     
    
    
    

    formHr=SQLFORM(db2.HR,buttons=[]).process()
    if not rowsIW:
        formIW=SQLFORM(db2.IW,rowsIW).process()
    else:
        db2.IW.NAZIV.default=rowsIW.NAZIV
        db2.IW.OPIS.default=rowsIW.OPIS
        db2.IW.Funkcija.default=rowsIW.Funkcija
        db2.IW.PAZI.default=rowsIW.PAZI
        db2.IW.OPASNOST.default=rowsIW.OPASNOST
        formIW=SQLFORM(db2.IW,rowsIW).process()

    if formIW.accepted:
        redirect(URL('HRtoIW',args=(1+request.args(0,cast=int))))
    elif formIW.errors:
            pass
    return locals()

@auth.requires_login()
@auth.requires(auth.has_membership(auth.id_group('admin')) or auth.has_membership(auth.id_group('IT')))
def HRtoIT():
    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    rowsIT=db2.IT(db2.IT.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoIT',args=(1+request.args(0,cast=int))))
    else: pass


    db2.HR.BROJ.default=rows.BROJ
    db2.HR.NAZIV.writeble=False
    db2.HR.NAZIV.default=rows.NAZIV
    db2.HR.OPIS.default=rows.OPIS
    db2.HR.Funkcija.default=rows.Funkcija
    db2.HR.PAZI.default=rows.PAZI
    db2.HR.OPASNOST.default=rows.OPASNOST
    db2.IT.id.readable=False
    if not rowsIT:
        db2.IT.BROJ.default=rows.BROJ
    else:
        db2.IT.BROJ.default=rowsIT.BROJ
        db2.IT.NAZIV.default=rowsIT.NAZIV
        db2.IT.OPIS.default=rowsIT.OPIS
        db2.IT.PAZI.default=rowsIT.PAZI
        db2.IT.Funkcija.default=rowsIT.Funkcija
        pass
    db2.IT.OPASNOST.default=rows.OPASNOST
    db2.IT.OPASNOST.writeable=False

    formHr=SQLFORM(db2.HR,buttons=[]).process()
    if not rowsIT:
        formIT=SQLFORM(db2.IT,rowsIT).process()
    else:
        db2.IT.NAZIV.default=rowsIT.NAZIV
        db2.IT.OPIS.default=rowsIT.OPIS
        db2.IT.Funkcija.default=rowsIT.Funkcija
        db2.IT.PAZI.default=rowsIT.PAZI
        db2.IT.OPASNOST.default=rowsIT.OPASNOST
        formIT=SQLFORM(db2.IT,rowsIT).process()

    if formIT.accepted:
        redirect(URL('HRtoIT',args=(1+request.args(0,cast=int))))
    elif formIT.errors:
            pass
    return locals()


@auth.requires_login()
@auth.requires(auth.has_membership(auth.id_group('admin')) or auth.has_membership(auth.id_group('FR')))
def HRtoFR():
    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    rowsFR=db2.FR(db2.FR.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoFR',args=(1+request.args(0,cast=int))))
    else: pass


    db2.HR.BROJ.default=rows.BROJ
    db2.HR.NAZIV.writeble=False
    db2.HR.NAZIV.default=rows.NAZIV
    db2.HR.OPIS.default=rows.OPIS
    db2.HR.Funkcija.default=rows.Funkcija
    db2.HR.PAZI.default=rows.PAZI
    db2.HR.OPASNOST.default=rows.OPASNOST
    db2.FR.id.readable=False
    if not rowsFR:
        db2.FR.BROJ.default=rows.BROJ
    else:
        db2.FR.BROJ.default=rowsFR.BROJ
        db2.FR.NAZIV.default=rowsFR.NAZIV
        db2.FR.OPIS.default=rowsFR.OPIS
        db2.FR.PAZI.default=rowsFR.PAZI
        db2.FR.Funkcija.default=rowsFR.Funkcija
        pass
    db2.FR.OPASNOST.default=rows.OPASNOST
    db2.FR.OPASNOST.writeable=False

    formHr=SQLFORM(db2.HR,buttons=[]).process()
    if not rowsFR:
        formFR=SQLFORM(db2.FR,rowsFR).process()
    else:
        db2.FR.NAZIV.default=rowsFR.NAZIV
        db2.FR.OPIS.default=rowsFR.OPIS
        db2.FR.Funkcija.default=rowsFR.Funkcija
        db2.FR.PAZI.default=rowsFR.PAZI
        db2.FR.OPASNOST.default=rowsFR.OPASNOST
        formFR=SQLFORM(db2.FR,rowsFR).process()

    if formFR.accepted:
        redirect(URL('HRtoFR',args=(1+request.args(0,cast=int))))
    elif formFR.errors:
            pass
    return locals()


@auth.requires_login()
@auth.requires_membership('admin')
def hrvatski():
    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    
    if not rows:
        redirect(URL('hrvatski',args=(1+request.args(0,cast=int))))
    else:
        form=SQLFORM(db2.HR,rows).process()

    if form.accepted:
        redirect(URL('hrvatski',args=(1+request.args(0,cast=int))))
    elif form.errors:
            pass
    return locals()
        
   


@auth.requires_login()
@auth.requires(auth.has_membership(auth.id_group('admin')) or auth.has_membership(auth.id_group('IW')))
def ENtoIW():
    rows=db2.EN(db2.EN.BROJ==(request.args(0,cast=int)))
    rowsIW=db2.IW(db2.IW.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoIW',args=(request.args(0,cast=int))))
    else: pass


    db2.EN.BROJ.default=rows.BROJ
    db2.EN.NAZIV.writeble=False
    db2.EN.NAZIV.default=rows.NAZIV
    db2.EN.OPIS.default=rows.OPIS
    db2.EN.Funkcija.default=rows.Funkcija
    db2.EN.PAZI.default=rows.PAZI
    db2.EN.OPASNOST.default=rows.OPASNOST
    db2.IW.id.readable=False
    if not rowsIW:
        db2.IW.BROJ.default=rows.BROJ
    else:
        db2.IW.BROJ.default=rowsIW.BROJ
        db2.IW.NAZIV.default=rowsIW.NAZIV
        db2.IW.OPIS.default=rowsIW.OPIS
        db2.IW.PAZI.default=rowsIW.PAZI
        db2.IW.Funkcija.default=rowsIW.Funkcija
        pass
    db2.IW.OPASNOST.default=rows.OPASNOST
    db2.IW.OPASNOST.writeable=False
   


     
    
    
    

    formEN=SQLFORM(db2.EN,buttons=[]).process()
    if not rowsIW:
        formIW=SQLFORM(db2.IW,rowsIW).process()
    else:
        db2.IW.NAZIV.default=rowsIW.NAZIV
        db2.IW.OPIS.default=rowsIW.OPIS
        db2.IW.Funkcija.default=rowsIW.Funkcija
        db2.IW.PAZI.default=rowsIW.PAZI
        db2.IW.OPASNOST.default=rowsIW.OPASNOST
        formIW=SQLFORM(db2.IW,rowsIW).process()

    if formIW.accepted:
        redirect(URL('ENtoIW',args=(1+request.args(0,cast=int))))
    elif formIW.errors:
            pass
    return locals()

@auth.requires_login()
@auth.requires(auth.has_membership(auth.id_group('admin')) or auth.has_membership(auth.id_group('EN')))
def HRtoEN():
    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    rowsEN=db2.EN(db2.EN.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoEN',args=(1+request.args(0,cast=int))))
    else: pass
        
    
             
            
        

    db2.HR.BROJ.writeble=False
    db2.HR.BROJ.readable=True
    
    db2.HR.BROJ.default=rows.BROJ
    db2.EN.BROJ.default=rows.BROJ
    
    db2.HR.NAZIV.writeble=False
    db2.HR.NAZIV.default=rows.NAZIV
   
    
    db2.HR.OPIS.writeble=False
    db2.HR.OPIS.default=rows.OPIS
    
    
    db2.HR.Funkcija.writeble=False
    db2.HR.Funkcija.default=rows.Funkcija
    
    
    
    db2.HR.PAZI.writeble=False
    db2.HR.PAZI.default=rows.PAZI
    
    
    db2.HR.OPASNOST.writeble=False
    db2.HR.OPASNOST.default=rows.OPASNOST
    db2.EN.OPASNOST.default=rows.OPASNOST
    
    
   

    db2.EN.BROJ.writeble=False
    db2.EN.BROJ.readable=False

    formHr=SQLFORM(db2.HR,buttons=[]).process()
    if not rowsEN:
        formEN=SQLFORM(db2.EN,rowsEN).process()
    else:
        db2.EN.NAZIV.default=rowsEN.NAZIV
        db2.EN.OPIS.default=rowsEN.OPIS
        db2.EN.Funkcija.default=rowsEN.Funkcija
        db2.EN.PAZI.default=rowsEN.PAZI
        formEN=SQLFORM(db2.EN,rowsEN).process()
        
        
    if formEN.accepted:
        redirect(URL('HRtoEN',args=(1+request.args(0,cast=int))))
    elif formEN.errors:
            pass
    return locals()
@auth.requires_login()
@auth.requires(auth.has_membership(auth.id_group('admin')) or auth.has_membership(auth.id_group('DE')))
def HRtoDE():

    rows=db2.HR(db2.HR.BROJ==(request.args(0,cast=int)))
    rowsDE=db2.DE(db2.DE.BROJ==(request.args(0,cast=int)))
    if not rows:
        redirect(URL('HRtoDE',args=(1+request.args(0,cast=int))))
    else: pass


    db2.HR.BROJ.writeble=False
    db2.HR.BROJ.readable=True

    db2.HR.BROJ.default=rows.BROJ
    db2.DE.BROJ.default=rows.BROJ

    db2.HR.NAZIV.writeble=False
    db2.HR.NAZIV.default=rows.NAZIV
    
    
    db2.HR.OPIS.writeble=False
    db2.HR.OPIS.default=rows.OPIS
    
    
    db2.HR.Funkcija.writeble=False
    db2.HR.Funkcija.default=rows.Funkcija
    
    
    
    db2.HR.PAZI.writeble=False
    db2.HR.PAZI.default=rows.PAZI
    
    
    db2.HR.OPASNOST.writeble=False
    db2.HR.OPASNOST.default=rows.OPASNOST
    db2.DE.OPASNOST.default=rows.OPASNOST
    
    db2.DE.id.readable=False
    

    db2.DE.BROJ.writeble=False
    db2.DE.BROJ.readable=False

    formHr=SQLFORM(db2.HR,buttons=[]).process()
    if not rowsDE:
        formDe=SQLFORM(db2.DE,rowsDE).process()
    else:
        db2.DE.NAZIV.default=rowsDE.NAZIV
        db2.DE.OPIS.default=rowsDE.OPIS
        db2.DE.Funkcija.default=rowsDE.Funkcija
        db2.DE.PAZI.default=rowsDE.PAZI
        formDe=SQLFORM(db2.DE,rowsDE).process()
        
    if formDe.accepted:
        redirect(URL('HRtoDE',args=(1+request.args(0,cast=int))))
    elif formDe.errors:
            pass
    return locals()
    return locals()


@auth.requires_login()
def hrdatabase():
    rows=db2(db2.HR).select().sort(lambda row: row.BROJ)
    rows=db2(db2.HR).select().sort(lambda row: row.BROJ)
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
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
