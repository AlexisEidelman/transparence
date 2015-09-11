# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:39:32 2015

@author: User
"""

#import pandas as pd
#import os
#
#from sqlalchemy import create_engine
#
#path = 'D:\data\transparence'
#main_file = os.path.join(path, 'sunshine.sql')
#
#from sqlalchemy import create_engine
#engine = create_engine('D:/data/transparence', echo=False)
#tab = pd.read_sql(main_file, engine)

from CONFIG import *
import psycopg2
import pandas as pd

conn_string =  "dbname='" + dbname + "' user='" + user + "' host='" + \
                        host + "' password='" + password + "' client_encoding='utf-8'"
print (conn_string)
conn = psycopg2.connect(conn_string)
print("Connected!")
cur = conn.cursor()

schema = 'public'
table_name = 'declaration'
#command = "SELECT " + variable_utiles[table_name].replace('\n', ',') + \
#            " FROM " + table_name + ';'

command = """SELECT
  declaration.entreprise_uid,
  declaration.ligne_identifiant,
  declaration.ligne_action,
  declaration.ligne_rectification,
  declaration.benef_categorie_code,
  declaration.benef_nom,
  declaration.benef_prenom,
  declaration.benef_qualite_code,
  declaration.benef_adresse1,
  declaration.benef_adresse2,
  declaration.benef_adresse3,
  declaration.benef_adresse4,
  declaration.benef_codepostal,
  declaration.benef_ville,
  declaration.benef_pays_code,
  declaration.benef_titre_code,
  declaration.benef_specialite_code,
  declaration.benef_qualification,
  declaration.benef_identifiant_type_code,
  declaration.benef_identifiant_valeur,
  declaration.benef_etablissement,
  declaration.benef_etablissement_codepostal,
  declaration.benef_etablissement_ville,
  declaration.benef_denomination_sociale,
  declaration.benef_objet_social,
  declaration.ligne_type,
  declaration.conv_date_signature,
  declaration.conv_objet,
  declaration.conv_date_debut,
  declaration.conv_manifestation_date,
  declaration.conv_date_fin,
  declaration.conv_manifestation_nom,
  declaration.conv_manifestation_lieu,
  declaration.avant_date_signature,
  declaration.avant_montant_ttc,
  declaration.avant_nature,
  declaration.avant_convention_lie,
  declaration.conv_manifestation_organisateur,
  declaration.demande_rectification_en_cours,
  declaration.benef_departement_uid
FROM
  public.declaration;"""



#variable_utiles = {'declaration':
#  """entreprise_uid
#  ligne_identifiant
#  ligne_action
#  ligne_rectification
#  benef_categorie_code
#  benef_nom
#  benef_prenom
#  benef_qualite_code
#  benef_adresse1
#  benef_adresse2
#  benef_adresse3
#  benef_adresse4
#  benef_codepostal
#  benef_ville
#  benef_pays_code
#  benef_titre_code
#  benef_specialite_code
#  benef_qualification
#  benef_identifiant_type_code
#  benef_identifiant_valeur
#  benef_etablissement
#  benef_etablissement_codepostal
#  benef_etablissement_ville
#  benef_denomination_sociale
#  benef_objet_social
#  ligne_type
#  conv_date_signature
#  conv_objet
#  conv_date_debut
#  conv_manifestation_date
#  conv_date_fin
#  conv_manifestation_nom
#  conv_manifestation_lieu
#  avant_date_signature
#  avant_montant_ttc
#  avant_nature
#  avant_convention_lie
#  avant_conv_annee
#  avant_conv_semestre
#  lien_fichier
#  conv_manifestation_organisateur
#  demande_rectification_en_cours
#  benef_departement_uid"""}


variable_utiles = {'declaration':
  """entreprise_uid,
  ligne_identifiant,
  ligne_action,
  ligne_rectification,
  benef_categorie_code,
  benef_nom,
  benef_prenom,
  benef_qualite_code,
  benef_adresse1,
  benef_adresse2,
  benef_adresse3,
  benef_adresse4,
  benef_codepostal,
  benef_ville,
  benef_pays_code,
  benef_titre_code,
  benef_specialite_code,
  benef_qualification,
  benef_identifiant_type_code,
  benef_identifiant_valeur,
  benef_etablissement,
  benef_etablissement_codepostal,
  benef_etablissement_ville,
  benef_denomination_sociale,
  benef_objet_social,
  ligne_type,
  conv_date_signature,
  conv_objet,
  conv_date_debut,
  conv_manifestation_date,
  conv_date_fin,
  conv_manifestation_nom,
  conv_manifestation_lieu,
  avant_date_signature,
  avant_montant_ttc,
  avant_nature,
  avant_convention_lie,
  avant_conv_annee,
  avant_conv_semestre,
  lien_fichier,
  conv_manifestation_organisateur,
  demande_rectification_en_cours,
  benef_departement_uid"""}

cur.execute(command)
colnames = [desc[0] for desc in cur.description]
print (colnames)
df = pd.DataFrame(cur.fetchall(), columns = colnames)
