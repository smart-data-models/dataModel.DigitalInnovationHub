<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: DigitalInnovationHubService  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Fornire alle aziende intuizioni e tendenze sui mercati per stimolare la loro innovazione interna.  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `additionalMaterial[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Materiali aggiuntivi del Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `author[string]`: Proprietà. Modello:'https://schema.org/Text'. Autore del servizio Digital Innovation Hub.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: Proprietà. Modello:'https://schema.org/Text'. Categoria del servizio Digital Innovation Hub.  . Model: [https://schema.org/Text](https://schema.org/Text)- `contacts[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Contatti del Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateSubmitted[string]`: Proprietà. La data e l'ora di questa osservazione nel formato ISO8601 UTC. Modello:'https://schema.org/DateTime'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[string]`: Proprietà. La data e l'ora di questa osservazione nel formato ISO8601 UTC. Modello:'https://schema.org/DateTime'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `relation[array]`: Proprietà. Modello:'https://schema.org/StructuredValue'. Relazioni del servizio Digital Innovation Hub.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `serviceImage[string]`: Proprietà. Modello:'https://schema.org/URL'. URL dell'immagine del servizio Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)- `serviceSubType[string]`: Proprietà. Modello:'https://schema.org/Text'. ServiceSubType del servizio Digital Innovation Hub.  . Model: [https://schema.org/Text](https://schema.org/Text)- `serviceType[string]`: Proprietà. Modello:'https://schema.org/Text'. ServiceType del servizio Digital Innovation Hub.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `target[array]`: Proprietà. Modello:'https://schema.org/Text'. Obiettivi del servizio Digital Innovation Hub.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Proprietà. Tipo di entità NGSI. Deve essere DigitalInnovationHubService.  - `url[string]`: Proprietà. Modello:'https://schema.org/URL'. URL del servizio Digital Innovation Hub.  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
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
DigitalInnovationHubService:    
  description: Provision of insights and trend on markets to companies to stimulate their internal innovation.    
  properties:    
    additionalMaterial:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Additional Materials of the Digital Innovation Hub.'    
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
    author:    
      description: 'Property. Model:''https://schema.org/Text''. Author of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: 'Property. Model:''https://schema.org/Text''. Category of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contacts:    
      description: 'Property. Model:''https://schema.org/StructuredValue''. Contacts of the Digital Innovation Hub.'    
      items:    
        - description: Property. All contact elements in data models unless explicitly stated according to schema.org    
          properties:    
            contactPoint:    
              description: 'Property. Model:''https://schema.org/ContactPoint''. The details to contact with the item.'    
              properties:    
                areaServed:    
                  description: Property. The geographic area where a service or offered item is provided. Supersedes serviceArea.    
                  type: string    
                availabilityRestriction:    
                  anyOf:    
                    - description: Property. Array of identifiers format of any NGSI entity.    
                      items:    
                        maxLength: 256    
                        minLength: 1    
                        pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                        type: string    
                      type: array    
                    - description: Property. Array of identifiers format of any NGSI entity.    
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
                  description: Property. Contact type of this item.    
                  type: string    
                email:    
                  description: Property. Email address of owner.    
                  format: idn-email    
                  type: string    
                faxNumber:    
                  description: 'Property. Model:''http://schema.org/Text''. The fax number.'    
                  type: string    
                name:    
                  description: Property. The name of this item.    
                  type: string    
                productSupported:    
                  description: 'Property. Model:''http://schema.org/Text''. The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").'    
                  type: string    
                telephone:    
                  description: Property. Telephone of this contact.    
                  type: string    
                url:    
                  description: Property. URL which provides a description or further information about this item.    
                  format: uri    
                  type: string    
              type: object    
          type: object    
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
    id:    
      anyOf: &digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items: &properties_-_owner_-_items    
        anyOf: *digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
              anyOf: *digitalinnovationhubservice_-_properties_-_owner_-_items_-_anyof    
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
      description: list of uri pointing to additional resources about the item    
      oneOf: *digitalinnovationhubservice_-_properties_-_seealso_-_oneof    
      x-ngsi:    
        type: Property    
    serviceImage:    
      description: 'Property. Model:''https://schema.org/URL''. URL of the image of the Digital Innovation Hub Service.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    serviceSubType:    
      description: 'Property. Model:''https://schema.org/Text''. ServiceSubType of the Digital Innovation Hub Service.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceType:    
      description: 'Property. Model:''https://schema.org/Text''. ServiceType of the Digital Innovation Hub Service.'    
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
      description: 'Property. Model:''https://schema.org/Text''. Targets of the Digital Innovation Hub Service.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: Property. NGSI entity type. It has to be DigitalInnovationHubService    
      enum:    
        - DigitalInnovationHubService    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: 'Property. Model:''https://schema.org/URL''. URL of the Digital Innovation Hub Service.'    
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
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### DigitalInnovationHubService Valori chiave NGSI-v2 Esempio  
Ecco un esempio di DigitalInnovationHubService in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DigitalInnovationHubService NGSI-v2 normalizzato Esempio  
Ecco un esempio di DigitalInnovationHubService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DigitalInnovationHubService Valori-chiave NGSI-LD Esempio  
Ecco un esempio di DigitalInnovationHubService in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
        "https://smart-data-models.github.io/dataModel.DigitalInnovationHub/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.DigitalInnovationHub/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DigitalInnovationHubService NGSI-LD normalizzato Esempio  
Ecco un esempio di DigitalInnovationHubService in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
