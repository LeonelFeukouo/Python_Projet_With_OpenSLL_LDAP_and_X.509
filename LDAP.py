import ldap
import ldap.modlist as modlist

#INITIALISATION DU SERVEUR LDAP
def Initialiser(addrIp):
    global l 
    l = ldap.initialize(f"ldap://{addrIp}")
    l.protocol_version = ldap.VERSION3
    l.set_option(ldap.OPT_REFERRALS,0)
    print("Initialisation du serveur...OK")

#AUTHENTIFICATION
def Authentifier(name,pwd):
    nom = "cn="+name+",dc=tekup,dc=leo"
    l.simple_bind_s(nom,pwd)
    print("Authentification de "+name+" ...OK")

#AUTHENTIFICATION UTILISATEUR
def AuthentifierUser(name,pwd):
    nom = "uid="+name+",ou=utilisateurs,dc=tekup,dc=leo"
    l.simple_bind_s(nom,pwd)
    print("Authentification de "+name+" ...OK")

#DECONNEXION DE L'UTILISATEUR
def Deconnecter():
    l.unbind_s()
    print("Deconnexion...OK")


#AJOUT D'UN UTILISATEUR (Le mot de passe doit etre hacher en SSHA)
def Ajouter(userId, userCn, userSn, userPass):
    dn = "uid="+userId+",ou=utilisateurs,dc=tekup,dc=leo"
    attrs = {}
    attrs['objectclass'] = [b'top', b'person', b'inetOrgPerson']
    attrs['uid'] = userId.encode('utf-8')
    attrs['cn'] = userCn.encode('utf-8')
    attrs['sn'] = userSn.encode('utf-8')
    #attrs['userPassword'] = '{SSHA}D6BwIWVHvnCDGQMdKLTjmHwsbBqjwXX6'.encode('utf-8')
    attrs['userPassword'] = userPass.encode('utf-8')
    ldif = modlist.addModlist(attrs)
    l.add_s(dn,ldif)
    print("Ajout de "+userId+" ...OK")

#MODIFICATION D'UN UTILISATEUR
def Modifier(userId, attrib, oldValue, newValue):
    dn="uid="+userId+",ou=utilisateurs,dc=tekup,dc=leo"
    old = {attrib : [oldValue.encode('utf-8')]}
    new = {attrib : [newValue.encode('utf-8')]}
    ldif = modlist.modifyModlist(old,new)
    l.modify_s(dn,ldif)
    print("Modification de "+userId+" ...OK")

#RECHERCHE SUR UN UTILISATEUR
def Rechercher(userId):
    print("\nRecherche de ",userId,"...")
    baseDN = "ou=utilisateurs,dc=tekup,dc=leo"
    searchScope = ldap.SCOPE_SUBTREE
    searchFilter = "uid="+userId
    searchAttributes = ["userPassword"]
    searchAttributes = None
    ldap_result_id = l.search(baseDN, searchScope, searchFilter, searchAttributes)
    result_set = []
    while 1:
        result_type, result_data = l.result(ldap_result_id, 0)
        if (result_data == []):
            break
        else:
            if result_type == ldap.RES_SEARCH_ENTRY:
                result_set.append(result_data)
    print(result_set,"\n")

#SUPRESSION D'UN UTILISATEUR
def Supprimer(userId):
    deleteDN = "uid="+userId+",ou=utilisateurs,dc=tekup,dc=leo"
    l.delete_s(deleteDN)
    print("Supression de ",userId," ...OK")


try:
    Initialiser("192.168.1.32")
    
    Authentifier('admin', 'leonel')

    #AuthentifierUser('leonelf', 'l')
    
    #Ajouter('leonelf', 'leonel', 'leonel', '{SSHA}D6BwIWVHvnCDGQMdKLTjmHwsbBqjwXX6')

    #Modifier('leonelf', 'sn', 'leonel', 'FEUKOUO')
    
    #Rechercher('leonelf')
    
    #Supprimer('leonelf')

    Deconnecter()

except ldap.INVALID_CREDENTIALS:
    print("Login ou mot de passe incorrect")

except ldap.LDAPError as e:
    print("Erreur : ", e)
