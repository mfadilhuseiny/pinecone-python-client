# coding: utf-8

"""
    Pinecone API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Contact: support@pinecone.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from pinecone.core.client.models.scored_vector import ScoredVector
from pinecone.core.client.models.single_query_results import SingleQueryResults


class QueryResponse(BaseModel):
    """
    The response for the `Query` operation. These are the matches found for a particular query vector. The matches are ordered from most similar to least similar.  # noqa: E501
    """

    results: Optional[conlist(SingleQueryResults)] = Field(
        None, description="DEPRECATED. The results of each query. The order is the same as `QueryRequest.queries`."
    )
    matches: Optional[conlist(ScoredVector)] = Field(None, description="The matches for the vectors.")
    namespace: Optional[StrictStr] = Field(None, description="The namespace for the vectors.")
    __properties = ["results", "matches", "namespace"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> QueryResponse:
        """Create an instance of QueryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matches (list)
        _items = []
        if self.matches:
            for _item in self.matches:
                if _item:
                    _items.append(_item.to_dict())
            _dict["matches"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueryResponse:
        """Create an instance of QueryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QueryResponse.parse_obj(obj)

        _obj = QueryResponse.parse_obj(
            {
                "results": [SingleQueryResults.from_dict(_item) for _item in obj.get("results")]
                if obj.get("results") is not None
                else None,
                "matches": [ScoredVector.from_dict(_item) for _item in obj.get("matches")]
                if obj.get("matches") is not None
                else None,
                "namespace": obj.get("namespace"),
            }
        )
        return _obj
