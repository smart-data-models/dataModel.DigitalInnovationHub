Entità: DigitalInnovationHubService  
===================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Fornitura di intuizioni e tendenze sui mercati alle aziende per stimolare la loro innovazione interna.  

## Elenco delle proprietà  

- `additionalMaterial`: [StructuredValue](https://schema.org/StructuredValue). Materiali aggiuntivi del Digital Innovation Hub.  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `author`: [Testo](https://schema.org/Text). Autore del servizio Digital Innovation Hub.  - `category`: [Testo](https://schema.org/Text). Categoria del servizio Digital Innovation Hub.  - `contacts`: [StructuredValue](https://schema.org/StructuredValue). Contatti del Digital Innovation Hub.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `relation`: [StructuredValue](https://schema.org/StructuredValue). Relazioni del servizio Digital Innovation Hub.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serviceImage`: [StructuredValue](https://schema.org/StructuredValue). Immagine del servizio Digital Innovation Hub.  - `serviceSubType`: [Testo](https://schema.org/Text). ServiceSubType del servizio Digital Innovation Hub.  - `serviceType`: [Testo](https://schema.org/Text). ServiceType del servizio Digital Innovation Hub.  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio pienamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `target`: [StructuredValue](https://schema.org/StructuredValue). Obiettivi del servizio Digital Innovation Hub.  - `type`: Tipo di entità NGSI. Deve essere DigitalInnovationHubService  - `url`: [URL](https://schema.org/URL). URL del servizio Digital Innovation Hub.    
Proprietà richieste  
- `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DigitalInnovationHubService:    
  description: 'Provision of insights and trend on markets to companies to stimulate their internal innovation.'    
  properties:    
    additionalMaterial:    
      description: "[StructuredValue](https://schema.org/StructuredValue). Additional Materials of the Digital Innovation Hub."    
      items:    
        - properties:    
            label:    
              type: string    
            url:    
              type: string    
          type: object    
      type: array    
      x-ngsi:    
        type: Property    
    address:    
      description: 'The mailing address'    
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
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
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
    author:    
      description: "[Text](https://schema.org/Text). Author of the Digital Innovation Hub Service."    
      type: string    
      x-ngsi:    
        type: Property    
    category:    
      description: "[Text](https://schema.org/Text). Category of the Digital Innovation Hub Service."    
      type: string    
      x-ngsi:    
        type: Property    
    contacts:    
      description: "[StructuredValue](https://schema.org/StructuredValue). Contacts of the Digital Innovation Hub."    
      items:    
        - description: 'Property. All contact elements in data models unless explicitly stated according to schema.org'    
          properties:    
            contactPoint:    
              description: 'Property. Model:''https://schema.org/ContactPoint''. The details to contact with the item.'    
              properties:    
                contactType:    
                  description: 'Property. Contact type of this item.'    
                  type: string    
                email:    
                  description: 'Property. Email address of owner.'    
                  format: idn-email    
                  type: string    
                name:    
                  description: 'Property. The name of this item.'    
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
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    relation:    
      description: "[StructuredValue](https://schema.org/StructuredValue). Relations of the Digital Innovation Hub Service."    
      items:    
        - properties:    
            relationIdentifier:    
              type: string    
            relationType:    
              type: string    
          required:    
            - relationType    
            - relationIdentifier    
          type: object    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serviceImage:    
      description: "[StructuredValue](https://schema.org/StructuredValue). Image of the Digital Innovation Hub Service."    
      properties:    
        base64Data:    
          type: string    
        fileName:    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    serviceSubType:    
      description: "[Text](https://schema.org/Text). ServiceSubType of the Digital Innovation Hub Service."    
      type: string    
      x-ngsi:    
        type: Property    
    serviceType:    
      description: "[Text](https://schema.org/Text). ServiceType of the Digital Innovation Hub Service."    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    target:    
      description: "[StructuredValue](https://schema.org/StructuredValue). Targets of the Digital Innovation Hub Service."    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be DigitalInnovationHubService'    
      enum:    
        - DigitalInnovationHubService    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: "[URL](https://schema.org/URL). URL of the Digital Innovation Hub Service."    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.DIH/DigitalInnovationHubService/schema.json    
  x-model-tags: DIH    
  x-version: 0.0.2    
```  
</details>    
## Esempio di payloads  
#### DigitalInnovationHubService NGSI-v2 valori chiave Esempio  
Ecco un esempio di un DigitalInnovationHubService in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
  "type": "DigitalInnovationHubService",  
  "title": "Trend watching",  
  "description": "Provision of insights and trend on markets to companies to stimulate their internal innovation",  
  "serviceImage": {  
    "base64Data": "iVBORa1ytHEAAAAAElFTkSuQmCC",  
    "fileName": "it.png"  
  },  
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
			"relationType": "dih",  
			"relationIdentifier": "b6IZuH0B_X_d5NJkB0eY"  
		},  
		{  
			"relationType": "service",  
			"relationIdentifier": "b6IZuH0B_X_d5NJkB0eX"  
		}  
	]  
}  
```  
#### DigitalInnovationHubService NGSI-v2 normalizzato Esempio  
Ecco un esempio di un DigitalInnovationHubService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
		"type": "StructuredValue",  
		"value": {  
			"base64Data": "iVBORa1ytHEAAAAAElFTkSuQmCC",  
			"fileName": "it.png"  
		}  
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
		"value": [{  
			"label": "Brochure",  
			"url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
		}]  
	},  
	"contacts": {  
		"type": "array",  
		"value": [{  
			"name": "Mark Johnson",  
			"email": "mark.johnson@sample-dih.it"  
		}]  
	},  
	"author": {  
		"type": "Text",  
		"value": "John Doe"  
	},  
	"relation": {  
		"type": "StructuredValue",  
		"value": [  
			{  
				"relationType": "dih",  
				"relationIdentifier": "b6IZuH0B_X_d5NJkB0eY"  
			},  
			{  
				"relationType": "service",  
				"relationIdentifier": "b6IZuH0B_X_d5NJkB0eX"  
			}  
		]  
	}  
}  
```  
#### DigitalInnovationHubService NGSI-LD valori-chiave Esempio  
Ecco un esempio di un DigitalInnovationHubService in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:DigitalInnovationHubService:DigitalInnovationHubService:b6IZuH0B_X_d5NJkB0eY",  
  "type": "DigitalInnovationHubService",  
  "title": "Trend watching",  
  "description": "Provision of insights and trend on markets to companies to stimulate their internal innovation",  
  "serviceImage": {  
    "base64Data": "iVBORa1ytHEAAAAAElFTkSuQmCC",  
    "fileName": "it.png"  
  },  
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
			"relationType": "dih",  
			"relationIdentifier": "b6IZuH0B_X_d5NJkB0eY"  
		},  
		{  
			"relationType": "service",  
			"relationIdentifier": "b6IZuH0B_X_d5NJkB0eX"  
		}  
	],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld"  
  ]  
}  
```  
#### DigitalInnovationHubService NGSI-LD normalizzato Esempio  
Ecco un esempio di un DigitalInnovationHubService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
		"value": {  
			"base64Data": "iVBORa1ytHEAAAAAElFTkSuQmCC",  
			"fileName": "it.png"  
		}  
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
		"value": [{  
			"label": "Brochure",  
			"url": "https://www.sample-dih.com/trend-watching/brochure.pdf"  
		}]  
	},  
	"contacts": {  
		"type": "Property",  
		"value": [{  
			"name": "Mark Johnson",  
			"email": "mark.johnson@sample-dih.it"  
		}]  
	},  
	"author": {  
		"type": "Property",  
		"value": "John Doe"  
	},  
	"relation": {  
		"type": "Property",  
		"value": [  
			{  
				"relationType": "dih",  
				"relationIdentifier": "b6IZuH0B_X_d5NJkB0eY"  
			},  
			{  
				"relationType": "service",  
				"relationIdentifier": "b6IZuH0B_X_d5NJkB0eX"  
			}  
		]  
	},  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
