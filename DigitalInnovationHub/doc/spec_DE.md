<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: DigitalInnovationHub  
=============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Digital Innovation Hubs sind One-Stop-Shops, die Unternehmen dabei helfen, ihre Geschäfts-/Produktionsprozesse wettbewerbsfähiger zu machen.**  
Version: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Postanschrift des Digital Innovation Hub.  . Model: [https://schema.org/PostalAddress](https://schema.org/PostalAddress)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `competences[array]`: Kompetenzen des Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `dateSubmitted[string]`: Das Datum und die Uhrzeit dieser Beobachtung im ISO8601 UTC-Format  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[string]`: Das Datum und die Uhrzeit dieser Beobachtung im ISO8601 UTC-Format  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Eine Beschreibung dieses Artikels  - `domain[array]`: Bereich des Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[object]`: GeoProperty. GeoJSON Punktreferenz auf den Standort des Digital Innovation Hub.  . Model: [https://geojson.org/schema/Point.json](https://geojson.org/schema/Point.json)- `logo[string]`: URL des Logos des Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relation[array]`: Beziehungen des Digital Innovation Hub Service.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `representatives[array]`: Vertreter des Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `socialAccounts[object]`: SocialAccounts des Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `type[string]`: NGSI-Entitätstyp. Es muss DigitalInnovationHub sein.  - `website[string]`: Website des Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### DigitalInnovationHub NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHub im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DigitalInnovationHub NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHub im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DigitalInnovationHub NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHub im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DigitalInnovationHub/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DigitalInnovationHub NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHub im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "type": "GeoProperty",  
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
        "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DigitalInnovationHub/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
