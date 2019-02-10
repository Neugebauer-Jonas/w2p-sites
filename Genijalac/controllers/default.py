# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@auth.requires_membership('Writer')
def index():
    if auth.is_logged_in():
        array=[]
        names=[]
        
        names.append('Povijest: ')
        array.append(db2(db2.Pitanja.Kategorija =='Povijest' ).count())
        
        names.append('Znanost: ')
        array.append(db2(db2.Pitanja.Kategorija =='Znanost' ).count())
        
        names.append('Geografija: ')
        array.append(db2(db2.Pitanja.Kategorija =='Geografija' ).count())
        
        names.append('Tehnologija: ')
        array.append(db2(db2.Pitanja.Kategorija =='Tehnologija' ).count())
        
        names.append('Sport: ')
        array.append(db2(db2.Pitanja.Kategorija =='Sport' ).count())
        
        #names.append('Kultura: ')
        # array.append(db2(db2.Pitanja.Kategorija =='Kultura' ).count())
        
        names.append('Književnost: ')
        array.append(db2(db2.Pitanja.Kategorija =='Knjizevnost' ).count())
        
        names.append('Glazba: ')
        array.append(db2(db2.Pitanja.Kategorija =='Glazba' ).count())
        names.append('Biologija: ')
        array.append(db2(db2.Pitanja.Kategorija =='Biologija' ).count())
        names.append('Film: ')
        array.append(db2(db2.Pitanja.Kategorija =='Film' ).count())
        names.append('Politika: ')
        array.append(db2(db2.Pitanja.Kategorija =='Politika' ).count())
        
        ct = db2(db2.Pitanja).count()
        cm=db2(db2.Pitanja.Autor == auth.user.first_name +' '+ auth.user.last_name).count()
        lastpos=db2(db2.Pitanja.id>0).select().last()
        br=lastpos.id - 10
        zadnje=db2(db2.Pitanja.id > br).select()
        
        if auth.user.id==1:
            grid2 = SQLFORM.grid(db2.Pitanja,             csv=False,create=False,orderby=~db2.Pitanja.id,paginate=15)

            return locals()
        q = db2.Pitanja.Autor == auth.user.first_name +' '+ auth.user.last_name
        grid2 = SQLFORM.grid(q,db2.Pitanja,csv=False,create=False,orderby=~db2.Pitanja.id,paginate=50)
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


@auth.requires_login()
@auth.requires_membership('Admin')
def statistika():
    broj=request.args(0)
    pit=db2.Pitanja(broj)
    form = SQLFORM(db2.Pitanja,pit)
    sve = db2(db2.Pitanja).select(orderby=~db2.Pitanja.id)
    
    #refactor = db2(db2.Pitanja.id>0).select()
    #for n in refactor:
    #    if n.Odgovor1==n.TocanOdgovor:
    #        db2(db2.Pitanja.id ==n.id).update(TocanOdgovor="")
    #    elif n.Odgovor2==n.TocanOdgovor:
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor2=n.Odgovor1)
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor1=n.TocanOdgovor)
    #        db2(db2.Pitanja.id ==n.id).update(TocanOdgovor="")
    #    elif n.Odgovor3==n.TocanOdgovor:
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor3=n.Odgovor1)
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor1=n.TocanOdgovor)
    #        db2(db2.Pitanja.id ==n.id).update(TocanOdgovor="")
    #    elif n.Odgovor4==n.TocanOdgovor:
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor4=n.Odgovor1)
    #        db2(db2.Pitanja.id ==n.id).update(Odgovor1=n.TocanOdgovor)
    #        db2(db2.Pitanja.id ==n.id).update(TocanOdgovor="")
        
   
    return locals()

@auth.requires_login()
@auth.requires_membership('Writer')
def kat():
    return locals()



@auth.requires_login()
@auth.requires_membership('Writer')
def newData():

    rows=db2(db2.Pitanja.Kategorija ==(request.args(0))).select(orderby=~db2.Pitanja.id)

    db2.Pitanja.Autor.default=auth.user.first_name +' '+ auth.user.last_name
    
    db2.Pitanja.Tocno.default=0
    db2.Pitanja.Krivo.default=0
    db2.Pitanja.Tocno.writable=False
    db2.Pitanja.Krivo.writable=False
    db2.Pitanja.Diff.writable=False
    db2.Pitanja.PitanjeSlika.writable=False
    db2.Pitanja.PitanjeAudio.writable=False
    db2.Pitanja.PitanjeVideo.writable=False
    db2.Pitanja.Credits.writable=False
    db2.Pitanja.Kategorija.default=(request.args(0))
    db2.Pitanja.TocanOdgovor.writable=False
    
    if auth.user.id==1:
        db2.Pitanja.PitanjeSlika.writable=True
        db2.Pitanja.Credits.writable=True
    form = SQLFORM(db2.Pitanja)
    if form.process().accepted:
        
        response.flash = 'form accepted'
        redirect(URL('newData',args=(request.args(0))))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return locals()


@request.restful()
def api():

    def GET(*args, **vars):
        broj=request.args(0,cast=int)
        tocno=request.args(1)
        row=db2(db2.Pitanja.id ==broj).select().first()
        if tocno=='T':
            if row.Tocno==None:
                db2(db2.Pitanja.id ==broj).update(Tocno=1)
            else:
                db2(db2.Pitanja.id ==broj).update(Tocno=(row.Tocno+1))

        elif tocno=='F':
            if row.Krivo==None:
                db2(db2.Pitanja.id ==broj).update(Krivo=1)
            else:
                db2(db2.Pitanja.id ==broj).update(Krivo=(row.Tocno+1))
                
                
        if row.Krivo*100/(1+row.Krivo+row.Tocno)>90:
            db2(db2.Pitanja.id ==broj).update(Diff=10)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>80:
            db2(db2.Pitanja.id ==broj).update(Diff=9)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>70:
            db2(db2.Pitanja.id ==broj).update(Diff=8)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>60:
            db2(db2.Pitanja.id ==broj).update(Diff=7)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>50:
            db2(db2.Pitanja.id ==broj).update(Diff=6)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>40:
            db2(db2.Pitanja.id ==broj).update(Diff=5)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>30:
            db2(db2.Pitanja.id ==broj).update(Diff=4)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>20:
            db2(db2.Pitanja.id ==broj).update(Diff=3)
        elif row.Krivo*100/(1+row.Krivo+row.Tocno)>10:
            db2(db2.Pitanja.id ==broj).update(Diff=2)
        else:
            db2(db2.Pitanja.id ==broj).update(Diff=1)
        
                    
        return 'OK'
    return locals()
