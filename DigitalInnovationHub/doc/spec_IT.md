<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: DigitalInnovationHub  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **I **Digital Innovation Hubs sono sportelli unici che aiutano le aziende a diventare più competitive nei loro processi aziendali/produttivi.  
versione: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `competences[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Competenze del Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateSubmitted[string]`: Proprietà. La data e l'ora di questa osservazione nel formato ISO8601 UTC. Modello:'https://schema.org/DateTime'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[string]`: Proprietà. La data e l'ora di questa osservazione nel formato ISO8601 UTC. Modello:'https://schema.org/DateTime'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `domain[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Dominio del Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `logo[string]`: Proprietà. Modello:'https://schema.org/URL'. URL del logo del Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `relation[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Relazioni del servizio Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `representatives[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Rappresentanti del Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `socialAccounts[object]`: Proprietà. [StructuredValue](https://schema.org/StructuredValue). SocialAccounts del Digital Innovation Hub.  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà. Tipo di entità NGSI. Deve essere DigitalInnovationHub.  - `website[string]`: Proprietà. Modello:'https://schema.org/URL'. Sito web del Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DigitalInnovationHub:    
  description: Digital Innovation Hubs are one-stop-shops that help companies to become more competitive with regard to their business/production processes.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    competences:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Competences of the Digital Innovation Hub.'    
      items:    
        - type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateSubmitted:    
      description: 'Property. The date and time of this observation in ISO8601 UTC format. Model:''https://schema.org/DateTime'''    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateUpdated:    
      description: 'Property. The date and time of this observation in ISO8601 UTC format. Model:''https://schema.org/DateTime'''    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    domain:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Domain of the Digital Innovation Hub.'    
      items:    
        - type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    id:    
      anyOf: &digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    logo:    
      description: 'Property. Model:''https://schema.org/URL''. URL of the logo of the Digital Innovation Hub.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items: &properties_-_owner_-_items    
        anyOf: *digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    relation:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Relations of the Digital Innovation Hub Service.'    
      items:    
        - properties:    
            alternateName:    
              description: Property. An alternative name for this item    
              type: string    
            dataProvider:    
              description: Property. A sequence of characters identifying the provider of the harmonised data entity.    
              type: string    
            dateCreated:    
              description: Property. Entity creation timestamp. This will usually be allocated by the storage platform.    
              format: date-time    
              type: string    
            dateModified:    
              description: Property. Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
              format: date-time    
              type: string    
            description:    
              description: Property. A description of this item    
              type: string    
            id:    
              anyOf: *digitalinnovationhub_-_properties_-_owner_-_items_-_anyof    
              description: Property. Unique identifier of the entity    
            name:    
              description: Property. The name of this item.    
              type: string    
            owner:    
              description: Property. A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
              items: *properties_-_owner_-_items    
              type: array    
            seeAlso:    
              description: Property. list of uri pointing to additional resources about the item    
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
      description: 'Property. Model:''https://schema.org/StructuredValue''. Representatives of the Digital Innovation Hub.'    
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
      description: list of uri pointing to additional resources about the item    
      oneOf: *digitalinnovationhub_-_properties_-_seealso_-_oneof    
      x-ngsi:    
        type: Property    
    socialAccounts:    
      description: 'Property. [StructuredValue](https://schema.org/StructuredValue). SocialAccounts of the Digital Innovation Hub.'    
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
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: Property. NGSI entity type. It has to be DigitalInnovationHub    
      enum:    
        - DigitalInnovationHub    
      type: string    
      x-ngsi:    
        type: Property    
    website:    
      description: 'Property. Model:''https://schema.org/URL''. Website of the Digital Innovation Hub.'    
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
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### DigitalInnovationHub NGSI-v2 valori-chiave Esempio  
Ecco un esempio di DigitalInnovationHub in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### DigitalInnovationHub NGSI-v2 normalizzato Esempio  
Ecco un esempio di DigitalInnovationHub in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
#### DigitalInnovationHub NGSI-LD valori-chiave Esempio  
Ecco un esempio di DigitalInnovationHub in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### DigitalInnovationHub NGSI-LD normalizzato Esempio  
Ecco un esempio di DigitalInnovationHub in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
