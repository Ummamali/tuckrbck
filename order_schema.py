from pydantic import BaseModel, field_validator, PositiveInt, model_validator, StringConstraints
from typing import Optional, Annotated


def not_empty(string):
    if len(string) == 0:
        raise ValueError('Cannot be empty')


StringValue = Annotated[str, StringConstraints(min_length=1)]


class Order(BaseModel):
    firstName: StringValue
    lastName: StringValue
    emailAddress: StringValue
    street: StringValue
    postalCode: PositiveInt
    city: StringValue
    items: dict[str, PositiveInt]

    @field_validator('items')
    def validate_items(cls, field: dict):
        if not field:
            raise ValueError('items cannot be empty')
        return field


class OrderUpdate(Order):
    firstName: Optional[StringValue]
    lastName: Optional[StringValue]
    emailAddress: Optional[StringValue]
    street: Optional[StringValue]
    postalCode: Optional[PositiveInt]
    city: Optional[StringValue]
    items: Optional[dict]

    @model_validator(mode='before')
    def validate_whole(cls, values):
        if len(values) == 0:
            raise ValueError('Empty delta not allowed!')
        return values

    class Config:
        extra = 'forbid'
