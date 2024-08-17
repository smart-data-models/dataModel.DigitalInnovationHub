from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    EmailStr,
    Field,
    RootModel,
    constr,
)


class AdditionalMaterialItem(BaseModel):
    label: Optional[str] = None
    url: Optional[str] = None


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ContactPoint(BaseModel):
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided. Supersedes serviceArea',
    )
    availabilityRestriction: Optional[
        Union[
            List[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                    min_length=1,
                    max_length=256,
                )
            ],
            List[AnyUrl],
        ]
    ] = Field(
        None,
        description='This property links a contact point to information about when the contact point is not available. The details are provided using the Opening Hours Specification class',
    )
    availableLanguage: Optional[Union[str, List[str]]] = Field(
        None,
        description='A language someone may use with or at the item, service or place. Please use one of the language codes from the IETF BCP 47 standard. It is implemented the Text option but it could be also Language',
    )
    contactOption: Optional[Union[str, List[str]]] = Field(
        None,
        description='An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers)',
    )
    contactType: Optional[str] = Field(None, description='Contact type of this item')
    email: Optional[EmailStr] = Field(None, description='Email address of owner')
    faxNumber: Optional[str] = Field(None, description='The fax number')
    name: Optional[str] = Field(None, description='The name of this item')
    productSupported: Optional[str] = Field(
        None,
        description="The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. 'iPhone') or a general category of products or services (e.g. 'smartphones')",
    )
    telephone: Optional[str] = Field(None, description='Telephone of this contact')
    url: Optional[AnyUrl] = Field(
        None,
        description='URL which provides a description or further information about this item',
    )


class Contact(BaseModel):
    contactPoint: Optional[ContactPoint] = Field(
        None, description='The details to contact with the item'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class RelationItem(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )


class Type6(Enum):
    DigitalInnovationHubService = 'DigitalInnovationHubService'


class DigitalInnovationHubService(BaseModel):
    additionalMaterial: Optional[List[AdditionalMaterialItem]] = Field(
        None, description='Additional Materials of the Digital Innovation Hub'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    author: Optional[str] = Field(
        None, description='Author of the Digital Innovation Hub Service'
    )
    category: Optional[str] = Field(
        None, description='Category of the Digital Innovation Hub Service'
    )
    contacts: Optional[List[Contact]] = Field(
        None, description='Contacts of the Digital Innovation Hub'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateSubmitted: Optional[AwareDatetime] = Field(
        None, description='The date and time of this observation in ISO8601 UTC format'
    )
    dateUpdated: Optional[AwareDatetime] = Field(
        None, description='The date and time of this observation in ISO8601 UTC format'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    relation: Optional[List[RelationItem]] = Field(
        None, description='Relations of the Digital Innovation Hub Service'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serviceImage: Optional[AnyUrl] = Field(
        None, description='URL of the image of the Digital Innovation Hub Service'
    )
    serviceSubType: Optional[str] = Field(
        None, description='ServiceSubType of the Digital Innovation Hub Service'
    )
    serviceType: Optional[str] = Field(
        None, description='ServiceType of the Digital Innovation Hub Service'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    target: Optional[List[str]] = Field(
        None, description='Targets of the Digital Innovation Hub Service'
    )
    title: Optional[str] = Field(None, description='Official name of the DIH')
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be DigitalInnovationHubService'
    )
    url: Optional[str] = Field(
        None, description='URL of the Digital Innovation Hub Service'
    )
