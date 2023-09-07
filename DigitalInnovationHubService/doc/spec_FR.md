<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : DigitalInnovationHubService  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHubService/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Fournir aux entreprises des informations et des tendances sur les marchés afin de stimuler leur innovation interne**.  
version : 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `additionalMaterial[array]`: Matériel supplémentaire du Hub d'innovation numérique  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `author[string]`: Auteur du service Digital Innovation Hub  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: Catégorie de service du Hub d'innovation numérique  . Model: [https://schema.org/Text](https://schema.org/Text)- `contacts[array]`: Contacts du Hub d'innovation numérique  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateSubmitted[date-time]`: La date et l'heure de cette observation au format ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[date-time]`: La date et l'heure de cette observation au format ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `relation[array]`: Relations du service "Digital Innovation Hub" (centre d'innovation numérique)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `serviceImage[uri]`: URL de l'image du service Digital Innovation Hub  . Model: [https://schema.org/URL](https://schema.org/URL)- `serviceSubType[string]`: ServiceSubType du service Digital Innovation Hub  . Model: [https://schema.org/Text](https://schema.org/Text)- `serviceType[string]`: Type de service du centre d'innovation numérique  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `target[array]`: Objectifs du service "Hub d'innovation numérique  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de DigitalInnovationHubService.  - `url[string]`: URL du service Digital Innovation Hub  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DigitalInnovationHubService:    
  description: Provision of insights and trend on markets to companies to stimulate their internal innovation.    
  properties:    
    additionalMaterial:    
      description: Additional Materials of the Digital Innovation Hub    
      items:    
        properties:    
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
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
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
      description: Author of the Digital Innovation Hub Service    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: Category of the Digital Innovation Hub Service    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contacts:    
      description: Contacts of the Digital Innovation Hub    
      items:    
        description: All contact elements in data models unless explicitly stated according to schema.org    
        properties:    
          contactPoint:    
            description: The details to contact with the item    
            properties:    
              areaServed:    
                description: The geographic area where a service or offered item is provided. Supersedes serviceArea    
                type: string    
                x-ngsi:    
                  type: Property    
              availabilityRestriction:    
                anyOf:    
                  - description: Array of identifiers format of any NGSI entity    
                    items:    
                    type: array    
                    x-ngsi:    
                      type: Property    
                  - description: Array of identifiers format of any NGSI entity    
                    items:    
                    type: array    
                    x-ngsi:    
                      type: Property    
                description: This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class    
                x-ngsi:    
                  model: http://schema.org/hoursAvailable    
                  type: Relationship    
              availableLanguage:    
                anyOf:    
                  - anyOf:    
                      -    
                      -    
                description: 'A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language'    
                x-ngsi:    
                  model: http://schema.org/availableLanguage    
                  type: Property    
              contactOption:    
                anyOf:    
                  - type: string    
                  - items:    
                    type: array    
                description: An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)    
                x-ngsi:    
                  model: http://schema.org/contactOption    
                  type: Property    
              contactType:    
                description: Contact type of this item    
                type: string    
                x-ngsi:    
                  type: Property    
              email:    
                description: Email address of owner    
                format: idn-email    
                type: string    
                x-ngsi:    
                  type: Property    
              faxNumber:    
                description: The fax number    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Text    
                  type: Property    
              name:    
                description: The name of this item    
                type: string    
                x-ngsi:    
                  type: Property    
              productSupported:    
                description: The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Text    
                  type: Property    
              telephone:    
                description: Telephone of this contact    
                type: string    
                x-ngsi:    
                  type: Property    
              url:    
                description: URL which provides a description or further information about this item    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              model: https://schema.org/ContactPoint    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateSubmitted:    
      description: The date and time of this observation in ISO8601 UTC format    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateUpdated:    
      description: The date and time of this observation in ISO8601 UTC format    
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
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    relation:    
      description: Relations of the Digital Innovation Hub Service    
      items:    
        properties:    
          alternateName:    
            description: An alternative name for this item    
            type: string    
            x-ngsi:    
              type: Property    
          dataProvider:    
            description: A sequence of characters identifying the provider of the harmonised data entity    
            type: string    
            x-ngsi:    
              type: Property    
          dateCreated:    
            description: Entity creation timestamp. This will usually be allocated by the storage platform    
            format: date-time    
            type: string    
            x-ngsi:    
              type: Property    
          dateModified:    
            description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
            format: date-time    
            type: string    
            x-ngsi:    
              type: Property    
          description:    
            description: A description of this item    
            type: string    
            x-ngsi:    
              type: Property    
          id:    
            anyOf:    
              - description: Identifier format of any NGSI entity    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Identifier format of any NGSI entity    
                format: uri    
                type: string    
                x-ngsi:    
                  type: Property    
            description: Unique identifier of the entity    
            x-ngsi:    
              type: Property    
          name:    
            description: The name of this item    
            type: string    
            x-ngsi:    
              type: Property    
          owner:    
            description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
            items:    
              anyOf:    
                - description: Identifier format of any NGSI entity    
                  maxLength: 256    
                  minLength: 1    
                  pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                  type: string    
                  x-ngsi:    
                    type: Property    
                - description: Identifier format of any NGSI entity    
                  format: uri    
                  type: string    
                  x-ngsi:    
                    type: Property    
              description: Unique identifier of the entity    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          seeAlso:    
            description: list of uri pointing to additional resources about the item    
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
          source:    
            description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
      description: URL of the image of the Digital Innovation Hub Service    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    serviceSubType:    
      description: ServiceSubType of the Digital Innovation Hub Service    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    serviceType:    
      description: ServiceType of the Digital Innovation Hub Service    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    target:    
      description: Targets of the Digital Innovation Hub Service    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI entity type. It has to be DigitalInnovationHubService    
      enum:    
        - DigitalInnovationHubService    
      type: string    
      x-ngsi:    
        type: Property    
    url:    
      description: URL of the Digital Innovation Hub Service    
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
## Exemples de charges utiles  
#### DigitalInnovationHubService Valeurs clés NGSI-v2 Exemple  
Voici un exemple de DigitalInnovationHubService au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### DigitalInnovationHubService NGSI-v2 normalisé Exemple  
Voici un exemple de DigitalInnovationHubService au format JSON-LD tel que normalisé. Il est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### DigitalInnovationHubService Valeurs clés NGSI-LD Exemple  
Voici un exemple de DigitalInnovationHubService au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### DigitalInnovationHubService NGSI-LD normalisé Exemple  
Voici un exemple de DigitalInnovationHubService au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
