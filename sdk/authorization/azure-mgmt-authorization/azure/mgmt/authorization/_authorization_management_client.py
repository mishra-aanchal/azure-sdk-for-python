# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.mgmt.core import ARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import AuthorizationManagementClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class AuthorizationManagementClient(MultiApiClientMixin, _SDKClient):
    """Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role assignments. A role assignment grants access to Azure Active Directory users.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credential which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2018-09-01-preview'
    _PROFILE_TAG = "azure.mgmt.authorization.AuthorizationManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'classic_administrators': '2015-07-01',
            'deny_assignments': '2018-07-01-preview',
            'global_administrator': '2015-07-01',
            'permissions': '2018-01-01-preview',
            'provider_operations_metadata': '2018-01-01-preview',
            'role_definitions': '2018-01-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credential, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default, **kwargs):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AuthorizationManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(AuthorizationManagementClient, self).__init__(
            credential,
            self._config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-06-01: :mod:`v2015_06_01.models<azure.mgmt.authorization.v2015_06_01.models>`
           * 2015-07-01: :mod:`v2015_07_01.models<azure.mgmt.authorization.v2015_07_01.models>`
           * 2018-01-01-preview: :mod:`v2018_01_01_preview.models<azure.mgmt.authorization.v2018_01_01_preview.models>`
           * 2018-07-01-preview: :mod:`v2018_07_01_preview.models<azure.mgmt.authorization.v2018_07_01_preview.models>`
           * 2018-09-01-preview: :mod:`v2018_09_01_preview.models<azure.mgmt.authorization.v2018_09_01_preview.models>`
        """
        if api_version == '2015-06-01':
            from .v2015_06_01 import models
            return models
        elif api_version == '2015-07-01':
            from .v2015_07_01 import models
            return models
        elif api_version == '2018-01-01-preview':
            from .v2018_01_01_preview import models
            return models
        elif api_version == '2018-07-01-preview':
            from .v2018_07_01_preview import models
            return models
        elif api_version == '2018-09-01-preview':
            from .v2018_09_01_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def classic_administrators(self):
        """Instance depends on the API version:

           * 2015-07-01: :class:`ClassicAdministratorsOperations<azure.mgmt.authorization.v2015_07_01.operations.ClassicAdministratorsOperations>`
           * 2015-06-01: :class:`ClassicAdministratorsOperations<azure.mgmt.authorization.v2015_06_01.operations.ClassicAdministratorsOperations>`
        """
        api_version = self._get_api_version('classic_administrators')
        if api_version == '2015-07-01':
            from .v2015_07_01.operations import ClassicAdministratorsOperations as OperationClass
        elif api_version == '2015-06-01':
            from .v2015_06_01.operations import ClassicAdministratorsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deny_assignments(self):
        """Instance depends on the API version:

           * 2018-07-01-preview: :class:`DenyAssignmentsOperations<azure.mgmt.authorization.v2018_07_01_preview.operations.DenyAssignmentsOperations>`
        """
        api_version = self._get_api_version('deny_assignments')
        if api_version == '2018-07-01-preview':
            from .v2018_07_01_preview.operations import DenyAssignmentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def global_administrator(self):
        """Instance depends on the API version:

           * 2015-07-01: :class:`GlobalAdministratorOperations<azure.mgmt.authorization.v2015_07_01.operations.GlobalAdministratorOperations>`
        """
        api_version = self._get_api_version('global_administrator')
        if api_version == '2015-07-01':
            from .v2015_07_01.operations import GlobalAdministratorOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def permissions(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`PermissionsOperations<azure.mgmt.authorization.v2018_01_01_preview.operations.PermissionsOperations>`
           * 2015-07-01: :class:`PermissionsOperations<azure.mgmt.authorization.v2015_07_01.operations.PermissionsOperations>`
        """
        api_version = self._get_api_version('permissions')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import PermissionsOperations as OperationClass
        elif api_version == '2015-07-01':
            from .v2015_07_01.operations import PermissionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def provider_operations_metadata(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`ProviderOperationsMetadataOperations<azure.mgmt.authorization.v2018_01_01_preview.operations.ProviderOperationsMetadataOperations>`
           * 2015-07-01: :class:`ProviderOperationsMetadataOperations<azure.mgmt.authorization.v2015_07_01.operations.ProviderOperationsMetadataOperations>`
        """
        api_version = self._get_api_version('provider_operations_metadata')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import ProviderOperationsMetadataOperations as OperationClass
        elif api_version == '2015-07-01':
            from .v2015_07_01.operations import ProviderOperationsMetadataOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def role_assignments(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`RoleAssignmentsOperations<azure.mgmt.authorization.v2018_01_01_preview.operations.RoleAssignmentsOperations>`
           * 2015-07-01: :class:`RoleAssignmentsOperations<azure.mgmt.authorization.v2015_07_01.operations.RoleAssignmentsOperations>`
           * 2018-09-01-preview: :class:`RoleAssignmentsOperations<azure.mgmt.authorization.v2018_09_01_preview.operations.RoleAssignmentsOperations>`
        """
        api_version = self._get_api_version('role_assignments')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import RoleAssignmentsOperations as OperationClass
        elif api_version == '2015-07-01':
            from .v2015_07_01.operations import RoleAssignmentsOperations as OperationClass
        elif api_version == '2018-09-01-preview':
            from .v2018_09_01_preview.operations import RoleAssignmentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def role_definitions(self):
        """Instance depends on the API version:

           * 2018-01-01-preview: :class:`RoleDefinitionsOperations<azure.mgmt.authorization.v2018_01_01_preview.operations.RoleDefinitionsOperations>`
           * 2015-07-01: :class:`RoleDefinitionsOperations<azure.mgmt.authorization.v2015_07_01.operations.RoleDefinitionsOperations>`
        """
        api_version = self._get_api_version('role_definitions')
        if api_version == '2018-01-01-preview':
            from .v2018_01_01_preview.operations import RoleDefinitionsOperations as OperationClass
        elif api_version == '2015-07-01':
            from .v2015_07_01.operations import RoleDefinitionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
