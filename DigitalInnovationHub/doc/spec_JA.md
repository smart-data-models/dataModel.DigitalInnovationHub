<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティDigitalInnovationHub  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.DigitalInnovationHub/blob/master/DigitalInnovationHub/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルでの説明**デジタル・イノベーション・ハブは、企業のビジネス/生産プロセスの競争力強化を支援するワンストップ・ショップです**。  
バージョン: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: デジタル・イノベーション・ハブの住所です。  . Model: [https://schema.org/PostalAddress](https://schema.org/PostalAddress)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `competences[array]`: デジタル・イノベーション・ハブのコンピタンス。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateSubmitted[string]`: ISO8601 UTC フォーマットによる観測日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateUpdated[string]`: ISO8601 UTC フォーマットによる観測日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: このアイテムの説明  - `domain[array]`: デジタル・イノベーション・ハブの領域。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `id[*]`: エンティティの一意な識別子  - `location[object]`: GeoProperty。GeoJSON デジタルイノベーションハブの位置へのポイントリファレンス。  . Model: [https://geojson.org/schema/Point.json](https://geojson.org/schema/Point.json)- `logo[string]`: デジタル・イノベーション・ハブのロゴのURLです。  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `relation[array]`: デジタル・イノベーション・ハブ・サービスの関係  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `representatives[array]`: デジタル・イノベーション・ハブの代表者。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `socialAccounts[object]`: デジタル・イノベーション・ハブのSocialAccounts。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSIエンティティタイプ。DigitalInnovationHubでなければならない。  - `website[string]`: デジタル・イノベーション・ハブのウェブサイトです。  . Model: [https://schema.org/URL](https://schema.org/URL)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### DigitalInnovationHub NGSI-v2キーバリューの例  
DigitalInnovationHubをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### DigitalInnovationHub NGSI-v2 正規化例  
DigitalInnovationHubをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### DigitalInnovationHub NGSI-LDのキー値例  
DigitalInnovationHubをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### DigitalInnovationHub NGSI-LD 正規化例  
DigitalInnovationHubをJSON-LD形式で正規化した例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
