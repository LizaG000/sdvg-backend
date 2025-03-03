import typing

from typing_extensions import Unpack
from typing import TypedDict, Any
from pydantic import Field, AliasChoices, AliasPath
import camelcaser as cc


class FieldParams(TypedDict, total=False):
    default: Any | None
    default_factory: typing.Callable[[], Any] | None
    alias: str | None
    alias_priority: int | None
    validation_alias: str | AliasPath | AliasChoices | None
    serialization_alias: str | None
    title: str | None
    description: str | None
    examples: list[Any] | None
    exclude: bool | None
    include: bool | None
    discriminator: str | None
    json_schema_extra: dict[str, Any] | None
    frozen: bool | None
    validate_default: bool | None
    repr: bool
    init_var: bool | None
    kw_only: bool | None
    pattern: str | None
    strict: bool | None
    gt: float | None
    ge: float | None
    lt: float | None
    le: float | None
    multiple_of: float | None
    allow_inf_nan: bool | None
    max_digits: int | None
    decimal_places: int | None
    min_length: int | None
    max_length: int | None
    additional_validation_aliases: list[str] | None


def build_pydantic_field(name: str,
                         **kwargs: Unpack[FieldParams]
                         ) -> Field:
    additional_validation_aliases = kwargs.pop('additional_validation_aliases', [])
    if not isinstance(additional_validation_aliases, list):
        raise TypeError('Argument additional_validation_aliases must be list of strings')
    return Field(**kwargs, alias=cc.make_camel_case(name),
                 validation_alias=AliasChoices(name, cc.make_lower_camel_case(name), *additional_validation_aliases))
