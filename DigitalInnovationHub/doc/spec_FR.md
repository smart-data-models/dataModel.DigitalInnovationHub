[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : DigitalInnovationHub  
=============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Les centres d'innovation numérique sont des guichets uniques qui aident les entreprises à devenir plus compétitives en ce qui concerne leurs processus d'affaires/de production**.  
version : 0.0.2  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `competences`: [Valeur structurée](https://schema.org/StructuredValue). Compétences du pôle d'innovation numérique.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `domain`: [Valeur structurée](https://schema.org/StructuredValue). Domaine du pôle d'innovation numérique.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `logo`: [Valeur structurée](https://schema.org/StructuredValue). Logo du pôle d'innovation numérique.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `relation`: [Valeur structurée](https://schema.org/StructuredValue). Relations du pôle d'innovation numérique.  - `representatives`: [Valeur structurée](https://schema.org/StructuredValue). Représentants du pôle d'innovation numérique.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `socialAccounts`: [Valeur structurée](https://schema.org/StructuredValue). Comptes sociaux du pôle d'innovation numérique.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit s'agir de DigitalInnovationHub  - `website`: [URL](https://schema.org/URL). Site web du Digital Innovation Hub.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DigitalInnovationHub:    
  description: 'Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes.'    
  properties:    
    address:    
      description: 'PostalAddress of the Digital Innovation Hub.'    
      type: object    
      x-ngsi:    
        model: https://schema.org/PostalAddress    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    competences:    
      description: 'Competences of the Digital Innovation Hub.'    
      items:    
        - type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateSubmitted:    
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateUpdated:    
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    domain:    
      description: 'Domain of the Digital Innovation Hub.'    
      items:    
        - type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    id:    
      anyOf: &digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'GeoProperty. GeoJSON Point reference to the location of the Digital Innovation Hub.'    
      type: object    
      x-ngsi:    
        model: https://geojson.org/schema/Point.json    
    logo:    
      description: 'URL of the logo of the Digital Innovation Hub.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items: &properties_-_owner_-_items    
        anyOf: *digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relation:    
      description: 'Relations of the Digital Innovation Hub Service.'    
      items:    
        - properties:    
            alternateName:    
              description: 'Property. An alternative name for this item'    
              type: string    
            dataProvider:    
              description: 'Property. A sequence of characters identifying the provider of the harmonised data entity.'    
              type: string    
            dateCreated:    
              description: 'Property. Entity creation timestamp. This will usually be allocated by the storage platform.'    
              format: date-time    
              type: string    
            dateModified:    
              description: 'Property. Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
              format: date-time    
              type: string    
            description:    
              description: 'Property. A description of this item'    
              type: string    
            id:    
              anyOf: *digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
              description: 'Property. Unique identifier of the entity'    
            name:    
              description: 'Property. The name of this item.'    
              type: string    
            owner:    
              description: 'Property. A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
              items: *properties_-_owner_-_items    
              type: array    
            seeAlso:    
              description: 'Property. list of uri pointing to additional resources about the item'    
              oneOf: &digitalinnovationhub_-_properties_-_seealso_-_oneof    
                - items:    
                    format: uri    
                    type: string    
                  minItems: 1    
                  type: array    
                - format: uri    
                  type: string    
            source:    
              description: 'Property. A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
              type: string    
          type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    representatives:    
      description: 'Representatives of the Digital Innovation Hub.'    
      items:    
        - properties:    
            email:    
              type: string    
            name:    
              type: string    
            responsibilities:    
              type: string    
            role:    
              type: string    
            surname:    
              type: string    
          type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf: *digitalinnovationhub_-_properties_-_seealso_-_oneof    
      x-ngsi:    
        type: Property    
    socialAccounts:    
      description: 'SocialAccounts of the Digital Innovation Hub.'    
      properties:    
        facebook:    
          type: string    
        instagram:    
          type: string    
        linkedin:    
          type: string    
        twitter:    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be DigitalInnovationHub'    
      enum:    
        - DigitalInnovationHub    
      type: string    
      x-ngsi:    
        type: Property    
    website:    
      description: 'Website of the Digital Innovation Hub.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DIH/DigitalInnovationHub/schema.json    
  x-model-tags: DIH    
  x-version: 0.0.3    
```  
</details>    
## Exemples de charges utiles  
#### DigitalInnovationHub NGSI-v2 key-values Exemple  
Voici un exemple de DigitalInnovationHub au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
	"id": "DigitalInnovationHub:Z6LGtH0B_X_d5NJkJEfB",  
	"type": "DigitalInnovationHub",  
	"title": "Sample DIH",  
	"website": "https://www.sample-dih.com/",  
	"logo": "https://www.sample-dih.com/logo.png",  
	"description": "Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes",  
	"location": {  
		"type": "Point",  
		"coordinates": [  
            43.66481,  
			7.196545  
        ]  
    },  
	"address": {  
		"streetAddress": "Viale della Regione Siciliana Nord Ovest",  
		"addressRegion": "Sicily",  
		"postalCode": "90146",  
		"addressCountry": "IT",  
		"addressLocality": "Palermo"  
	},  
	"representatives": [  
		{  
			"name": "John",  
			"surname": "Doe",  
			"email": "john.doe@sample-dih.com",  
			"role": "Engineer",  
			"responsibilities": "Manufacturing engineer"  
		}  
	],  
	"domain": [  
		"Manufacture of machinery and equipment"  
	],  
	"competences": [  
		"Additive manufacturing (3D printing)"  
	],  
	"socialAccounts": {  
		"linkedin": "https://www.linkedin.com/company/sample-dih",  
		"facebook": "https://www.facebook.com/sample.dih/",  
		"twitter": "https://www.twitter.com/sampledih",  
		"instagram": "https://www.instagram.com/lifeatsampledih"  
	},  
	"relation": [  
		{  
			"id": "DigitalInnovationHub:R5Ju4oO0_X_Jy8GO5d2"  
		},  
		{  
			"id": "DigitalInnovationHub:D5yr9HT3_X_RH7Fy7H9"  
		}  
	],  
	"dateSubmitted": "2020-07-07T15:05:59.408Z",  
	"dateUpdated": "2020-07-07T15:05:59.408Z"  
}  
```  
#### DigitalInnovationHub NGSI-v2 normalisé Exemple  
Voici un exemple de DigitalInnovationHub au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
	"id": "DigitalInnovationHub:Z6LGtH0B_X_d5NJkJEfB",  
	"type": "DigitalInnovationHub",  
	"title": {  
		"type": "Text",  
		"value": "Sample DIH"  
	},  
	"website": {  
		"type": "URL",  
		"value": "https://www.sample-dih.com/"  
	},  
	"logo": {  
		"type": "URL",  
		"value": "https://www.sample-dih.com/logo.png"  
	},  
	"description": {  
		"type": "Text",  
		"value": "Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes"  
	},  
	"location": {  
		"type": "geo:json",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				43.66481,  
				7.196545  
			]  
		}  
	},  
	"address": {  
		"type": "PostalAddress",  
		"value": {  
			"streetAddress": "Viale della Regione Siciliana Nord Ovest",  
			"addressRegion": "Sicily",  
			"postalCode": "90146",  
			"addressCountry": "IT",  
			"addressLocality": "Palermo"  
		}  
	},  
	"representatives": {  
		"type": "array",  
		"value": [  
			{  
				"name": "John",  
				"surname": "Doe",  
				"email": "john.doe@sample-dih.com",  
				"role": "Engineer",  
				"responsibilities": "Manufacturing engineer"  
			}  
		]  
	},  
	"domain": {  
		"type": "array",  
		"value": [  
			"Manufacture of machinery and equipment"  
		]  
	},  
	"competences": {  
		"type": "array",  
		"value": [  
			"Additive manufacturing (3D printing)"  
		]  
	},  
	"socialAccounts": {  
		"type": "StructuredValue",  
		"value": {  
			"linkedin": "https://www.linkedin.com/company/sample-dih",  
			"facebook": "https://www.facebook.com/sample.dih/",  
			"twitter": "https://www.twitter.com/sampledih",  
			"instagram": "https://www.instagram.com/lifeatsampledih"  
		}  
	},  
	"relation": {  
		"type": "array",  
		"value": [  
			{  
				"id": "DigitalInnovationHub:R5Ju4oO0_X_Jy8GO5d2"  
			},  
			{  
				"id": "DigitalInnovationHub:D5yr9HT3_X_RH7Fy7H9"  
			}  
		]  
	},  
	"dateSubmitted": {  
		"type": "DateTime",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-05-07T15:00:13.408Z"  
		}  
	},  
	"dateUpdated": {  
		"type": "DateTime",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	}  
}  
```  
#### DigitalInnovationHub NGSI-LD key-values Exemple  
Voici un exemple de DigitalInnovationHub au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
	"id": "urn:ngsi-ld:DigitalInnovationHub:DigitalInnovationHub:Z6LGtH0B_X_d5NJkJEfB",  
	"type": "DigitalInnovationHub",  
	"title": "Sample DIH",  
	"website": "https://www.sample-dih.com/",  
	"logo": "https://www.sample-dih.com/logo.png",  
	"description": "Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes",  
	"location": {  
	"type": "Point",  
        "coordinates": [  
            43.66481,  
			7.196545  
        ]  
    },  
	"address": {  
		"streetAddress": "Viale della Regione Siciliana Nord Ovest",  
		"addressRegion": "Sicily",  
		"postalCode": "90146",  
		"addressCountry": "IT",  
		"addressLocality": "Palermo"  
	},  
	"representatives": [  
		{  
			"name": "John",  
			"surname": "Doe",  
			"email": "john.doe@sample-dih.com",  
			"role": "Engineer",  
			"responsibilities": "Manufacturing engineer"  
		}  
	],  
	"domain": [  
		"Manufacture of machinery and equipment"  
	],  
	"competences": [  
		"Additive manufacturing (3D printing)"  
	],  
	"socialAccounts": {  
		"linkedin": "https://www.linkedin.com/company/sample-dih",  
		"facebook": "https://www.facebook.com/sample.dih/",  
		"twitter": "https://www.twitter.com/sampledih",  
		"instagram": "https://www.instagram.com/lifeatsampledih"  
	},  
	"relation": [  
        {  
            "id": "urn:ngsi-ld:DigitalInnovationHub:id:R5Ju4oO0_X_Jy8GO5d2"  
        },  
        {  
            "id": "urn:ngsi-ld:DigitalInnovationHub:id:D5yr9HT3_X_RH7Fy7H9"  
        }  
	],  
	"dateSubmitted": "2020-07-07T15:05:59.408Z",  
	"dateUpdated": "2020-07-07T15:05:59.408Z",  
	"@context": [  
		"https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld"  
	]  
}  
```  
#### DigitalInnovationHub NGSI-LD normalisé Exemple  
Voici un exemple de DigitalInnovationHub au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
	"id": "urn:ngsi-ld:DigitalInnovationHub:DigitalInnovationHub:Z6LGtH0B_X_d5NJkJEfB",  
	"type": "DigitalInnovationHub",  
	"title": {  
		"type": "Property",  
		"value": "Sample DIH"  
	},  
	"website": {  
		"type": "Property",  
		"value": "https://www.sample-dih.com/"  
	},  
	"logo": {  
		"type": "Property",  
		"value": "https://www.sample-dih.com/logo.png"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes"  
	},  
	"location": {  
		"type": "Geoproperty",  
		"value": {  
			"type": "Point",  
			"coordinates": [  
				43.66481,  
				7.196545  
			]  
		}  
	},  
	"address": {  
		"type": "Property",  
		"value": {  
			"streetAddress": "Viale della Regione Siciliana Nord Ovest",  
			"addressRegion": "Sicily",  
			"postalCode": "90146",  
			"addressCountry": "IT",  
			"addressLocality": "Palermo"  
		}  
	},  
	"representatives": {  
		"type": "Property",  
		"value": [  
			{  
				"name": "John",  
				"surname": "Doe",  
				"email": "john.doe@sample-dih.com",  
				"role": "Engineer",  
				"responsibilities": "Manufacturing engineer"  
			}  
		]  
	},  
	"domain": {  
		"type": "Property",  
		"value": [  
			"Manufacture of machinery and equipment"  
		]  
	},  
	"competences": {  
		"type": "Property",  
		"value": [  
			"Additive manufacturing (3D printing)"  
		]  
	},  
	"socialAccounts": {  
		"type": "Property",  
		"value": {  
			"linkedin": "https://www.linkedin.com/company/sample-dih",  
			"facebook": "https://www.facebook.com/sample.dih/",  
			"twitter": "https://www.twitter.com/sampledih",  
			"instagram": "https://www.instagram.com/lifeatsampledih"  
		}  
	},  
	"relation": {  
		"type": "Relationship",  
		"value": [  
			{  
                "id": "urn:ngsi-ld:DigitalInnovationHub:id:R5Ju4oO0_X_Jy8GO5d2"  
            },  
            {  
                "id": "urn:ngsi-ld:DigitalInnovationHub:id:D5yr9HT3_X_RH7Fy7H9"  
            }  
		]  
	},  
	"dateSubmitted": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"dateUpdated": {  
		"type": "Property",  
		"value": {  
			"type": "DateTime",  
			"value": "2020-07-07T15:05:59.408Z"  
		}  
	},  
	"@context": [  
		"https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld"  
	]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
