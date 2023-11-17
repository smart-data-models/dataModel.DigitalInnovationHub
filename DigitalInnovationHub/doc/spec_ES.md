<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: DigitalInnovationHub    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Los centros de innovación digital son ventanillas únicas que ayudan a las empresas a ser más competitivas en sus procesos empresariales y de producción.    
versión: 0.0.4    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `competences[array]`: Competencias del Polo de Innovación Digital  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateSubmitted[date-time]`: La fecha y hora de esta observación en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[date-time]`: La fecha y hora de esta observación en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descripción de este artículo  - `domain[array]`: Dominio del Polo de Innovación Digital  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `logo[string]`: URL del logotipo del Polo de Innovación Digital  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `relation[array]`: Relaciones del Servicio Polo de Innovación Digital  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `representatives[array]`: Representantes del Polo de Innovación Digital  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `socialAccounts[object]`: [ValorEstructurado](https://schema.org/StructuredValue). SocialAccounts del Digital Innovation Hub  	- `facebook`:       
	- `instagram`:       
	- `linkedin`:       
- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser DigitalInnovationHub  - `website[string]`: Página web del Polo de Innovación Digital  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
    competences:      
      description: Competences of the Digital Innovation Hub      
      items:      
        type: string      
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
    domain:      
      description: Domain of the Digital Innovation Hub      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
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
    logo:      
      description: URL of the logo of the Digital Innovation Hub      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
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
    representatives:      
      description: Representatives of the Digital Innovation Hub      
      items:      
        properties:      
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
    socialAccounts:      
      description: "[StructuredValue](https://schema.org/StructuredValue). SocialAccounts of the Digital Innovation Hub"      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI entity type. It has to be DigitalInnovationHub      
      enum:      
        - DigitalInnovationHub      
      type: string      
      x-ngsi:      
        type: Property      
    website:      
      description: Website of the Digital Innovation Hub      
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
## Ejemplo de carga útil    
#### DigitalInnovationHub NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un DigitalInnovationHub en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### DigitalInnovationHub NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de DigitalInnovationHub en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
    "type": "Text",  
    "value": "https://www.sample-dih.com/"  
  },  
  "logo": {  
    "type": "Text",  
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
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Viale della Regione Siciliana Nord Ovest",  
      "addressRegion": "Sicily",  
      "postalCode": "90146",  
      "addressCountry": "IT",  
      "addressLocality": "Palermo"  
    }  
  },  
  "representatives": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "Manufacture of machinery and equipment"  
    ]  
  },  
  "competences": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "value": "2020-05-07T15:00:13.408Z"  
  },  
  "dateUpdated": {  
    "type": "DateTime",  
    "value": "2020-07-07T15:05:59.408Z"  
  }  
}  
```  
</details>    
#### DigitalInnovationHub NGSI-LD key-values Ejemplo    
He aquí un ejemplo de DigitalInnovationHub en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### DigitalInnovationHub NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de DigitalInnovationHub en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
