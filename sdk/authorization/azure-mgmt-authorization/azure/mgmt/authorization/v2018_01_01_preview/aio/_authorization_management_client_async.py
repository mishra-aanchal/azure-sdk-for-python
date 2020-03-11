# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AuthorizationManagementClientConfiguration
from .operations_async import ProviderOperationsMetadataOperations
from .operations_async import RoleAssignmentsOperations
from .operations_async import PermissionsOperations
from .operations_async import RoleDefinitionsOperations
from .. import models


class AuthorizationManagementClient(object):
    """Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These calls handle provider operations.

    :ivar provider_operations_metadata: ProviderOperationsMetadataOperations operations
    :vartype provider_operations_metadata: azure.mgmt.authorization.v2018_01_01_preview.aio.operations_async.ProviderOperationsMetadataOperations
    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments: azure.mgmt.authorization.v2018_01_01_preview.aio.operations_async.RoleAssignmentsOperations
    :ivar permissions: PermissionsOperations operations
    :vartype permissions: azure.mgmt.authorization.v2018_01_01_preview.aio.operations_async.PermissionsOperations
    :ivar role_definitions: RoleDefinitionsOperations operations
    :vartype role_definitions: azure.mgmt.authorization.v2018_01_01_preview.aio.operations_async.RoleDefinitionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AuthorizationManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.provider_operations_metadata = ProviderOperationsMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.permissions = PermissionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_definitions = RoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AuthorizationManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
