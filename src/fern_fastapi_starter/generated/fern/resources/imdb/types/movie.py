# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .movie_id import MovieId


class Movie(pydantic.BaseModel):
    id: MovieId
    title: str
    rating: float = pydantic.Field(description=("The rating scale is one to five stars\n"))

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[MovieId]
        title: typing_extensions.NotRequired[str]
        rating: typing_extensions.NotRequired[float]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Movie.Validators.root()
            def validate(values: Movie.Partial) -> Movie.Partial:
                ...

            @Movie.Validators.field("id")
            def validate_id(id: MovieId, values: Movie.Partial) -> MovieId:
                ...

            @Movie.Validators.field("title")
            def validate_title(title: str, values: Movie.Partial) -> str:
                ...

            @Movie.Validators.field("rating")
            def validate_rating(rating: float, values: Movie.Partial) -> float:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Movie.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Movie.Validators._RootValidator]] = []
        _id_pre_validators: typing.ClassVar[typing.List[Movie.Validators.PreIdValidator]] = []
        _id_post_validators: typing.ClassVar[typing.List[Movie.Validators.IdValidator]] = []
        _title_pre_validators: typing.ClassVar[typing.List[Movie.Validators.PreTitleValidator]] = []
        _title_post_validators: typing.ClassVar[typing.List[Movie.Validators.TitleValidator]] = []
        _rating_pre_validators: typing.ClassVar[typing.List[Movie.Validators.PreRatingValidator]] = []
        _rating_post_validators: typing.ClassVar[typing.List[Movie.Validators.RatingValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Movie.Validators._RootValidator], Movie.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Movie.Validators._PreRootValidator], Movie.Validators._PreRootValidator]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Movie.Validators.PreIdValidator], Movie.Validators.PreIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Movie.Validators.IdValidator], Movie.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["title"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Movie.Validators.PreTitleValidator], Movie.Validators.PreTitleValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["title"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Movie.Validators.TitleValidator], Movie.Validators.TitleValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["rating"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Movie.Validators.PreRatingValidator], Movie.Validators.PreRatingValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["rating"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Movie.Validators.RatingValidator], Movie.Validators.RatingValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    if pre:
                        cls._id_pre_validators.append(validator)
                    else:
                        cls._id_post_validators.append(validator)
                if field_name == "title":
                    if pre:
                        cls._title_pre_validators.append(validator)
                    else:
                        cls._title_post_validators.append(validator)
                if field_name == "rating":
                    if pre:
                        cls._rating_pre_validators.append(validator)
                    else:
                        cls._rating_post_validators.append(validator)
                return validator

            return decorator

        class PreIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Movie.Partial) -> typing.Any:
                ...

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, __v: MovieId, __values: Movie.Partial) -> MovieId:
                ...

        class PreTitleValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Movie.Partial) -> typing.Any:
                ...

        class TitleValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: Movie.Partial) -> str:
                ...

        class PreRatingValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Movie.Partial) -> typing.Any:
                ...

        class RatingValidator(typing_extensions.Protocol):
            def __call__(self, __v: float, __values: Movie.Partial) -> float:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Movie.Partial) -> Movie.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: Movie.Partial) -> Movie.Partial:
        for validator in Movie.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: Movie.Partial) -> Movie.Partial:
        for validator in Movie.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("id", pre=True)
    def _pre_validate_id(cls, v: MovieId, values: Movie.Partial) -> MovieId:
        for validator in Movie.Validators._id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("id", pre=False)
    def _post_validate_id(cls, v: MovieId, values: Movie.Partial) -> MovieId:
        for validator in Movie.Validators._id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("title", pre=True)
    def _pre_validate_title(cls, v: str, values: Movie.Partial) -> str:
        for validator in Movie.Validators._title_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("title", pre=False)
    def _post_validate_title(cls, v: str, values: Movie.Partial) -> str:
        for validator in Movie.Validators._title_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("rating", pre=True)
    def _pre_validate_rating(cls, v: float, values: Movie.Partial) -> float:
        for validator in Movie.Validators._rating_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("rating", pre=False)
    def _post_validate_rating(cls, v: float, values: Movie.Partial) -> float:
        for validator in Movie.Validators._rating_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
