import ldap
import pprint

# tomado de
# http://www.grotan.com/ldap/python-ldap-samples.html#search
# conectamos al active directory
l = ldap.open("10.0.0.203")

#hacemos un bind
# cn =test objecto
# cn=Users que pertene a los usuarios
#dc = dominio
l.simple_bind("cn=test,cn=Users, dc=ad,dc=interalia","zxc")

# vemos el resultado del bind
pprint.pprint(l.result())

#buscamos al usuario que tenga la palabra *a*
#en el grupo de usuarios del dominio
l.search("cn=Users,dc=ad,dc=interalia",ldap.SCOPE_SUBTREE,"cn=*a*")
# vemos el resulstado
pprint.pprint(l.result())