[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: DigitalInnovationHubService  
====================================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Bereitstellung von Erkenntnissen und Trends über Märkte für Unternehmen, um deren interne Innovation zu fördern**.  
Version: 0.0.2  

## Liste der Eigenschaften  

- `additionalMaterial`: [StructuredValue](https://schema.org/StructuredValue). Zusätzliche Materialien des Digital Innovation Hub.  - `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `author`: [Text](https://schema.org/Text). Autor des Digital Innovation Hub Service.  - `category`: [Text](https://schema.org/Text). Kategorie des Digital Innovation Hub Service.  - `contacts`: [StructuredValue](https://schema.org/StructuredValue). Kontakte des Digital Innovation Hub.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `relation`: [StructuredValue](https://schema.org/StructuredValue). Beziehungen des Digital Innovation Hub Service.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `serviceImage`: [StructuredValue](https://schema.org/StructuredValue). Bild des Digital Innovation Hub Service.  - `serviceSubType`: [Text](https://schema.org/Text). ServiceSubType des Digital Innovation Hub Service.  - `serviceType`: [Text](https://schema.org/Text). ServiceType des Digital Innovation Hub Service.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `target`: [StructuredValue](https://schema.org/StructuredValue). Ziele des Digital Innovation Hub Service.  - `type`: NGSI-Entitätstyp. Es muss DigitalInnovationHubService sein.  - `url`: [URL](https://schema.org/URL). URL des Digital Innovation Hub Service.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DigitalInnovationHubService:    
  description: 'Provision of insights and trend on markets to companies to stimulate their internal innovation.'    
  properties:    
    additionalMaterial:    
      description: 'Additional Materials of the Digital Innovation Hub.'    
      items:    
        - properties:    
            label:    
              type: string    
            url:    
              type: string    
          type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    author:    
      description: 'Author of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Category of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contacts:    
      description: 'Contacts of the Digital Innovation Hub.'    
      items:    
        - description: 'Property. All contact elements in data models unless explicitly stated according to schema.org'    
          properties:    
            contactPoint:    
              description: 'Property. Model:''https://schema.org/ContactPoint''. The details to contact with the item.'    
              properties:    
                areaServed:    
                  description: 'Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.'    
                  type: string    
                availabilityRestriction:    
                  anyOf:    
                    - description: 'Property. Array of identifiers format of any NGSI entity.'    
                      items:    
                        maxLength: 256    
                        minLength: 1    
                        pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                        type: string    
                      type: array    
                    - description: 'Property. Array of identifiers format of any NGSI entity.'    
                      items:    
                        format: uri    
                        type: string    
                      type: array    
                  description: 'Relationship. Model:''http://schema.org/hoursAvailable''. This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class.'    
                availableLanguage:    
                  anyOf:    
                    - anyOf:    
                        - type: string    
                        - items:    
                            type: string    
                          type: array    
                  description: 'Property. Model:''http://schema.org/availableLanguage''. A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
                contactOption:    
                  anyOf:    
                    - type: string    
                    - items:    
                        type: string    
                      type: array    
                  description: 'Property. Model:''http://schema.org/contactOption''. An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).'    
                contactType:    
                  description: 'Property. Contact type of this item.'    
                  type: string    
                email:    
                  description: 'Property. Email address of owner.'    
                  format: idn-email    
                  type: string    
                faxNumber:    
                  description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
                  type: string    
                name:    
                  description: 'Property. The name of this item.'    
                  type: string    
                productSupported:    
                  description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
                  type: string    
                telephone:    
                  description: 'Property. Telephone of this contact.'    
                  type: string    
                url:    
                  description: 'Property. URL which provides a description or further information about this item.'    
                  format: uri    
                  type: string    
              type: object    
          type: object    
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
    id:    
      anyOf: &digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items: &properties_-_owner_-_items    
        anyOf: *digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
              anyOf: *digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
              oneOf: &digitalinnovationhubservice_-_properties_-_seealso_-_oneof    
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
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf: *digitalinnovationhubservice_-_properties_-_seealso_-_oneof    
      x-ngsi:    
        type: Property    
    serviceImage:    
      description: 'URL of the image of the Digital Innovation Hub Service.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    serviceSubType:    
      description: 'ServiceSubType of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceType:    
      description: 'ServiceType of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    target:    
      description: 'Targets of the Digital Innovation Hub Service.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be DigitalInnovationHubService'    
      enum:    
        - DigitalInnovationHubService    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: 'URL of the Digital Innovation Hub Service.'    
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
  x-license-url: https://github.com/smart-data-models/dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DIH/DigitalInnovationHubService/schema.json    
  x-model-tags: DIH    
  x-version: 0.0.3    
```  
</details>    
## Beispiel-Nutzlasten  
#### DigitalInnovationHubService NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHubService im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
    "type": "DigitalInnovationHubService",  
    "title": "Trend watching",  
    "description": "Provision of insights and trend on markets to companies to stimulate their internal innovation",  
    "serviceImage": "https://www.sample-dih.com/logo.png",  
    "category": "Ecosystem",  
    "serviceType": "DIH Innovation Development",  
    "serviceSubType": "Trend watching",  
    "target": [  
        "Engineers",  
        "Directors"  
    ],  
    "url": "https://www.sample-dih.com/trend-watching",  
    "additionalMaterial": [  
        {  
            "label": "Brochure",  
            "url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
        }  
    ],  
    "contacts": [  
        {  
            "name": "Mark Johnson",  
            "email": "mark.johnson@sample-dih.it"  
        }  
    ],  
    "author": "John Doe",  
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
#### DigitalInnovationHubService NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHubService im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
	"id": "urn:ngsi-ld:DigitalInnovationHubService:DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
	"type": "DigitalInnovationHubService",  
	"title": {  
		"type": "Text",  
		"value": "Trend watching"  
	},  
	"description": {  
		"type": "Text",  
		"value": "Provision of insights and trend on markets to companies to stimulate their internal innovation"  
	},  
	"serviceImage": {  
		"type": "URL",  
		"value": "https://www.sample-dih.com/logo.png"  
	},  
	"category": {  
		"type": "Text",  
		"value": "Ecosystem"  
	},  
	"serviceType": {  
		"type": "Text",  
		"value": "DIH Innovation Development"  
	},  
	"serviceSubType": {  
		"type": "Text",  
		"value": "Trend watching"  
	},  
	"target": {  
		"type": "array",  
		"value": [  
			"Engineers",  
			"Directors"  
		]  
	},  
	"url": {  
		"type": "Text",  
		"value": "https://www.sample-dih.com/trend-watching"  
	},  
	"additionalMaterial": {  
		"type": "array",  
		"value": [  
			{  
				"label": "Brochure",  
				"url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
			}  
		]  
	},  
	"contacts": {  
		"type": "array",  
		"value": [  
			{  
				"name": "Mark Johnson",  
				"email": "mark.johnson@sample-dih.it"  
			}  
		]  
	},  
	"author": {  
		"type": "Text",  
		"value": "John Doe"  
	},  
	"relation": {  
		"type": "array",  
		"value": [  
			{  
				"id": "urn:ngsi-ld:DigitalInnovationHubService:id:R5Ju4oO0_X_Jy8GO5d2"  
			},  
			{  
				"id": "urn:ngsi-ld:DigitalInnovationHubService:id:D5yr9HT3_X_RH7Fy7H9"  
			}  
		]  
	},  
	"dateSubmitted": {  
		"type": "Date-Time",  
		"value": "2020-07-07T15:05:59.408Z"  
	},  
	"dateUpdated": {  
		"type": "Date-Time",  
		"value": "2020-07-07T15:05:59.408Z"  
	}  
}  
```  
#### DigitalInnovationHubService NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHubService im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:DigitalInnovationHubService:DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
    "type": "DigitalInnovationHubService",  
    "title": "Trend watching",  
    "description": "Provision of insights and trend on markets to companies to stimulate their internal innovation",  
    "serviceImage": "https://www.sample-dih.com/logo.png",  
    "category": "Ecosystem",  
    "serviceType": "DIH Innovation Development",  
    "serviceSubType": "Trend watching",  
    "target": [  
        "Engineers",  
        "Directors"  
    ],  
    "url": "https://www.sample-dih.com/trend-watching",  
    "additionalMaterial": [  
        {  
            "label": "Brochure",  
            "url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
        }  
    ],  
    "contacts": [  
        {  
            "name": "Mark Johnson",  
            "email": "mark.johnson@sample-dih.it"  
        }  
    ],  
    "author": "John Doe",  
    "relation": [  
        {  
            "id": "urn:ngsi-ld:DigitalInnovationHubService:id:R5Ju4oO0_X_Jy8GO5d2"  
        },  
        {  
            "id": "urn:ngsi-ld:DigitalInnovationHubService:id:D5yr9HT3_X_RH7Fy7H9"  
        }  
    ],  
    "dateSubmitted": "2020-07-07T15:05:59.408Z",  
    "dateUpdated": "2020-07-07T15:05:59.408Z",  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld"  
    ]  
}  
```  
#### DigitalInnovationHubService NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen DigitalInnovationHubService im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
	"id": "urn:ngsi-ld:DigitalInnovationHubService:DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
	"type": "DigitalInnovationHubService",  
	"title": {  
		"type": "Property",  
		"value": "Trend watching"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Provision of insights and trend on markets to companies to stimulate their internal innovation"  
	},  
	"serviceImage": {  
		"type": "Property",  
		"value": "https://www.sample-dih.com/logo.png"  
	},  
	"category": {  
		"type": "Property",  
		"value": "Ecosystem"  
	},  
	"serviceType": {  
		"type": "Property",  
		"value": "DIH Innovation Development"  
	},  
	"serviceSubType": {  
		"type": "Property",  
		"value": "Trend watching"  
	},  
	"target": {  
		"type": "Property",  
		"value": [  
			"Engineers",  
			"Directors"  
		]  
	},  
	"url": {  
		"type": "Property",  
		"value": "https://www.sample-dih.com/trend-watching"  
	},  
	"additionalMaterial": {  
		"type": "Property",  
		"value": [  
			{  
				"label": "Brochure",  
				"url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
			}  
		]  
	},  
	"contacts": {  
		"type": "Property",  
		"value": [  
			{  
				"name": "Mark Johnson",  
				"email": "mark.johnson@sample-dih.it"  
			}  
		]  
	},  
	"author": {  
		"type": "Property",  
		"value": "John Doe"  
	},  
	"relation": {  
		"type": "Relationship",  
		"value": [  
			{  
                "id": "urn:ngsi-ld:DigitalInnovationHubService:id:R5Ju4oO0_X_Jy8GO5d2"  
            },  
            {  
                "id": "urn:ngsi-ld:DigitalInnovationHubService:id:D5yr9HT3_X_RH7Fy7H9"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
