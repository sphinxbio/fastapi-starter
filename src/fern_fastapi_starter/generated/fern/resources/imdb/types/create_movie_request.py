# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions


class CreateMovieRequest(pydantic.BaseModel):
    title: str
    rating: float

    class Partial(typing_extensions.TypedDict):
        title: typing_extensions.NotRequired[str]
        rating: typing_extensions.NotRequired[float]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @CreateMovieRequest.Validators.root()
            def validate(values: CreateMovieRequest.Partial) -> CreateMovieRequest.Partial:
                ...

            @CreateMovieRequest.Validators.field("title")
            def validate_title(title: str, values: CreateMovieRequest.Partial) -> str:
                ...

            @CreateMovieRequest.Validators.field("rating")
            def validate_rating(rating: float, values: CreateMovieRequest.Partial) -> float:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators._RootValidator]] = []
        _title_pre_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators.PreTitleValidator]] = []
        _title_post_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators.TitleValidator]] = []
        _rating_pre_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators.PreRatingValidator]] = []
        _rating_post_validators: typing.ClassVar[typing.List[CreateMovieRequest.Validators.RatingValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateMovieRequest.Validators._RootValidator], CreateMovieRequest.Validators._RootValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateMovieRequest.Validators._PreRootValidator], CreateMovieRequest.Validators._PreRootValidator
        ]:
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
            cls, field_name: typing_extensions.Literal["title"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateMovieRequest.Validators.PreTitleValidator], CreateMovieRequest.Validators.PreTitleValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["title"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateMovieRequest.Validators.TitleValidator], CreateMovieRequest.Validators.TitleValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["rating"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[
            [CreateMovieRequest.Validators.PreRatingValidator], CreateMovieRequest.Validators.PreRatingValidator
        ]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["rating"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[
            [CreateMovieRequest.Validators.RatingValidator], CreateMovieRequest.Validators.RatingValidator
        ]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
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

        class PreTitleValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateMovieRequest.Partial) -> typing.Any:
                ...

        class TitleValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: CreateMovieRequest.Partial) -> str:
                ...

        class PreRatingValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: CreateMovieRequest.Partial) -> typing.Any:
                ...

        class RatingValidator(typing_extensions.Protocol):
            def __call__(self, __v: float, __values: CreateMovieRequest.Partial) -> float:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: CreateMovieRequest.Partial) -> CreateMovieRequest.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: CreateMovieRequest.Partial) -> CreateMovieRequest.Partial:
        for validator in CreateMovieRequest.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: CreateMovieRequest.Partial) -> CreateMovieRequest.Partial:
        for validator in CreateMovieRequest.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("title", pre=True)
    def _pre_validate_title(cls, v: str, values: CreateMovieRequest.Partial) -> str:
        for validator in CreateMovieRequest.Validators._title_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("title", pre=False)
    def _post_validate_title(cls, v: str, values: CreateMovieRequest.Partial) -> str:
        for validator in CreateMovieRequest.Validators._title_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("rating", pre=True)
    def _pre_validate_rating(cls, v: float, values: CreateMovieRequest.Partial) -> float:
        for validator in CreateMovieRequest.Validators._rating_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("rating", pre=False)
    def _post_validate_rating(cls, v: float, values: CreateMovieRequest.Partial) -> float:
        for validator in CreateMovieRequest.Validators._rating_post_validators:
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
        extra = pydantic.Extra.forbid
