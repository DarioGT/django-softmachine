# -*- coding: utf-8 -*-
import django.contrib.admin          

class PropertyAdmin(django.contrib.admin.ModelAdmin):
    verbose_name_plural = 'Elements de donnees' 
    list_display =( 'code',  'description', )

    protoExt = {'protoIcon': 'property' }

    protoExt[ 'searchFields' ] = ( 'code', 'concept__model__code' ) 
    protoExt[ 'sortFields' ] = ( 'code', 'concept__model__code' )
    protoExt[ 'baseFilter' ] = { 'isForeign': False  }
    
    # Valores iniciales ( initialFilter maneja el autoload )   
    protoExt[ 'initialSort' ] = ( 'code', 'concept__model__code', ) 
    protoExt[ 'initialFilter' ] = { 'code__istartswith': 'a'}
    
    protoExt[ 'protoDetails' ] = [ {}, 
#        {'menuText': 'Propiétés d''élément de donnée', 'conceptDetail': 'protoExt.Udp', 'detailField': 'metaObj__pk', 'masterField': 'pk'}, 
        ]

    # Define el manejo de propiedades extendidas ( User defined properties 'UDP'
    # Debe existir una FKey en la tabla UDP apuntando hacia la tabla de base 
    # 'udpFk': 'metaObj',  'basePk': 'id', Son Mapeados por el ORM     
    protoExt[ 'protoUdp' ] =   { 
        'udpTable': 'udp', 
        'propertyName': 'code', 
        'propertyValue': 'valueUdp', 
        'propertyPrefix' : 'udp',           # Las referencias a los campos estaran precedidas por [prefix]__
         }

    protoExt[ 'protoFields' ] =  {        
        'code': {'header' : 'Éléments de données', 'type': 'CharField' ,  'minWidth': 200, 'flex': 1 },
        'concept__model__code': {'header' : 'Vue', 'type': 'CharField' , 'minWidth': 200 , 'flex': 1 },  

#        'concept__code': {'header' : 'Concept', 'type': 'CharField' , 'minWidth': 200, 'flex': 1  },  
        'description': { 'storeOnly': True },
        'isNullable':{},
        'alias':{},
        'baseType' : {}, 
        'length' : {}, 

        'udp__DOCUMENTDEREFERENCE' :{},
        'udp__FORMAT': {  },
        'udp__GABARIT': {  },
        'udp__DEFINITION': {  },
        'udp__DESCRIPTIONCN': {  },
        'udp__PRECISIONS': {  },
        'udp__VALIDATION': {  },
        'udp__VALIDATIONSSURELEMENT': {  },
        'udp__VALIDATIONSINTERELEMENT': {  },
        'udp__VALIDATION_INTER-ENREGISTREMENT': {  },
        'udp__SOURCEDEDONNEESEXTERNES': {  },
        'udp__ELEMENTTRANSFORME': {  },
        'udp__ELEMENTTRANSMIS': {  },
        'udp__DOMAINEDEVALEURS': {  },
        'udp__ENTREEENVIGUEUR': {  },
        'udp__DATEDERNIREMODIFICATION': {  },
        'udp__REQUISPAR': {  },
        'udp__TRANSMISSION': {  },
     }

    TEMPLATE = '<table class="ficha" cellpadding="3">'
    TEMPLATE += '<tr class="azul"><td class="negro">Nom de l''élément de donnée: </td><td>{{code}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro"> Nom de la vue de l''élément de donnée:</td><td>{{concept__model__code}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro"> Document de référence: </td><td class="desc">{{udp__DOCUMENTDEREFERENCE}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Alias: </td><td class="desc">{{alias}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Type de donnée: </td><td class="desc">{{baseType}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Longueur: </td><td class="desc">{{length}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Valeur nulle possible (oui,non)</td><td class="desc">{{isNullable}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Description: </td><td class="desc">{{description}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Format: </td><td class="desc">{{udp__FORMAT}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Gabarit: </td><td class="desc">{{udp__GABARIT}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Définition: </td><td class="desc">{{udp__DEFINITION}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Description CN: </td><td class="desc">{{udp__DESCRIPTIONCN}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro"> Précisions: </td><td class="desc">{{udp__PRECISIONS}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Validation: </td><td class="desc">{{udp__VALIDATION}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Validations sur l''élément: </td><td class="desc">{{udp__VALIDATIONSSURELEMENT}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Validations inter-élément: </td><td class="desc">{{udp__VALIDATIONSINTERELEMENT}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Validation inter-enregistrement: </td><td class="desc">{{udp__VALIDATION_INTER-ENREGISTREMENT}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Source de données externes: </td><td class="desc">{{udp__SOURCEDEDONNEESEXTERNES}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Élément transformé: </td><td class="desc">{{udp__ELEMENTTRANSFORME}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Élément transmis: </td><td class="desc">{{udp__ELEMENTTRANSMIS}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Domaine de valeurs: </td><td class="desc">{{udp__DOMAINEDEVALEURS}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Entrée en vigueur: </td><td class="desc">{{udp__ENTREEENVIGUEUR}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Date de la dernière modification: </td><td class="desc">{{udp__DATEDERNIREMODIFICATION}}</td></tr>'
    TEMPLATE += '<tr class="blanco"><td class="negro">Requis par: </td><td class="desc">{{udp__REQUISPAR}}</td></tr>'
    TEMPLATE += '<tr class="azul"><td class="negro">Transmission: </td><td class="desc">{{udp__TRANSMISSION}}</td></tr>'
    TEMPLATE += '</table>'
    
    protoExt[ 'protoSheet' ] =  {        
          'title' : "Fiche descriptive de l'élément de donnée",                        
          'properties': (   'code',
                            'concept__model__code',
                            'isNullable',
                            'udp__DOCUMENTDEREFERENCE',
                            'alias',
                            'baseType',
                            'length',
                            'description',
                            'udp__FORMAT',
                            'udp__GABARIT',
                            'udp__DEFINITION',
                            'udp__DESCRIPTIONCN',
                            'udp__PRECISIONS',
                            'udp__VALIDATION',
                            'udp__VALIDATIONSSURELEMENT',
                            'udp__VALIDATIONSINTERELEMENT',
                            'udp__VALIDATION_INTER-ENREGISTREMENT',
                            'udp__SOURCEDEDONNEESEXTERNES',
                            'udp__ELEMENTTRANSFORME',
                            'udp__ELEMENTTRANSMIS',
                            'udp__DOMAINEDEVALEURS',
                            'udp__ENTREEENVIGUEUR',
                            'udp__DATEDERNIREMODIFICATION',
                            'udp__REQUISPAR',
                            'udp__TRANSMISSION',
                          ),   
          'template': TEMPLATE }  


    protoExt['protoViews'] = [
            { 'viewName': 'default', 
              'viewFields': (  'code', 'concept__model__code',  ), 
              'icon' : 'icon-1'},
#            { 'viewName': 'all', 
#              'viewFields': ( 'code', 'concept__code', 'concept__model__code' )},
                        ]


    protoExt['protoFilters'] = []
    for nFiltre in ['A','B','C','D','E','É','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    
        protoExt['protoFilters'].append ( 
                { 'filterName': nFiltre, 
                  'filter': { 'code__istartswith': nFiltre }, 
#                 'icon' : 'icon-?'
                  }
        ) 