# # coding: utf-8

# """
#     Recruit Database

#     Groups of services that manage the data for the 247Sports recruiting database.<br>                                         Documentation for this silo can be found here:                                         <a target=\"_blank\" href=\"https://atlassian.cbsi.com/confluence/display/TWOSPORTS/RDB+Information\">                                         Recruit Database Documentation</a>  # noqa: E501

#     OpenAPI spec version: v1
    
#     Generated by: https://github.com/swagger-api/swagger-codegen.git
# """

# from __future__ import absolute_import

# import re  # noqa: F401

# # python 2 and python 3 compatibility library
# import six

# from recruitR.api_client import ApiClient


# class TagsApi(object):
#     """NOTE: This class is auto generated by the swagger code generator program.

#     Do not edit the class manually.
#     Ref: https://github.com/swagger-api/swagger-codegen
#     """

#     def __init__(self, api_client=None):
#         if api_client is None:
#             api_client = ApiClient()
#         self.api_client = api_client

#     def tfs_tagsautocomplete(self, **kwargs):  # noqa: E501
#         """Get a list of Ipa.DataAccess.MySql.Interfaces.ITaggable entities based on the search for us in AutoComplete or TokenInput controls  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagsautocomplete(async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str default_name: The search string, requeries at least 3 characters
#         :param int items: The number of items to return
#         :return: list[TagDto]
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """
#         kwargs['_return_http_data_only'] = True
#         if kwargs.get('async_req'):
#             return self.tfs_tagsautocomplete_with_http_info(**kwargs)  # noqa: E501
#         else:
#             (data) = self.tfs_tagsautocomplete_with_http_info(**kwargs)  # noqa: E501
#             return data

#     def tfs_tagsautocomplete_with_http_info(self, **kwargs):  # noqa: E501
#         """Get a list of Ipa.DataAccess.MySql.Interfaces.ITaggable entities based on the search for us in AutoComplete or TokenInput controls  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagsautocomplete_with_http_info(async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str default_name: The search string, requeries at least 3 characters
#         :param int items: The number of items to return
#         :return: list[TagDto]
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """

#         all_params = ['default_name', 'items']  # noqa: E501
#         all_params.append('async_req')
#         all_params.append('_return_http_data_only')
#         all_params.append('_preload_content')
#         all_params.append('_request_timeout')

#         params = locals()
#         for key, val in six.iteritems(params['kwargs']):
#             if key not in all_params:
#                 raise TypeError(
#                     "Got an unexpected keyword argument '%s'"
#                     " to method tfs_tagsautocomplete" % key
#                 )
#             params[key] = val
#         del params['kwargs']

#         collection_formats = {}

#         path_params = {}

#         query_params = []
#         if 'default_name' in params:
#             query_params.append(('defaultName', params['default_name']))  # noqa: E501
#         if 'items' in params:
#             query_params.append(('items', params['items']))  # noqa: E501

#         header_params = {}

#         form_params = []
#         local_var_files = {}

#         body_params = None
#         # HTTP header `Accept`
#         header_params['Accept'] = self.api_client.select_header_accept(
#             ['application/json'])  # noqa: E501

#         # Authentication setting
#         auth_settings = ['bearer']  # noqa: E501

#         return self.api_client.call_api(
#             '/rdb/v1/tags/autocomplete', 'GET',
#             path_params,
#             query_params,
#             header_params,
#             body=body_params,
#             post_params=form_params,
#             files=local_var_files,
#             response_type='list[TagDto]',  # noqa: E501
#             auth_settings=auth_settings,
#             async_req=params.get('async_req'),
#             _return_http_data_only=params.get('_return_http_data_only'),
#             _preload_content=params.get('_preload_content', True),
#             _request_timeout=params.get('_request_timeout'),
#             collection_formats=collection_formats)

#     def tfs_tagsprefixed_keyphotos(self, prefixed_key, **kwargs):  # noqa: E501
#         """Get a paginated listing of photos assigned to the specified tag  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagsprefixed_keyphotos(prefixed_key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str prefixed_key: The prefixed key of the tagged entity (required)
#         :param int page: The page number to fetch
#         :param int page_size: The size of the page to fetch
#         :return: ImageDtoPagedResults
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """
#         kwargs['_return_http_data_only'] = True
#         if kwargs.get('async_req'):
#             return self.tfs_tagsprefixed_keyphotos_with_http_info(prefixed_key, **kwargs)  # noqa: E501
#         else:
#             (data) = self.tfs_tagsprefixed_keyphotos_with_http_info(prefixed_key, **kwargs)  # noqa: E501
#             return data

#     def tfs_tagsprefixed_keyphotos_with_http_info(self, prefixed_key, **kwargs):  # noqa: E501
#         """Get a paginated listing of photos assigned to the specified tag  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagsprefixed_keyphotos_with_http_info(prefixed_key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str prefixed_key: The prefixed key of the tagged entity (required)
#         :param int page: The page number to fetch
#         :param int page_size: The size of the page to fetch
#         :return: ImageDtoPagedResults
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """

#         all_params = ['prefixed_key', 'page', 'page_size']  # noqa: E501
#         all_params.append('async_req')
#         all_params.append('_return_http_data_only')
#         all_params.append('_preload_content')
#         all_params.append('_request_timeout')

#         params = locals()
#         for key, val in six.iteritems(params['kwargs']):
#             if key not in all_params:
#                 raise TypeError(
#                     "Got an unexpected keyword argument '%s'"
#                     " to method tfs_tagsprefixed_keyphotos" % key
#                 )
#             params[key] = val
#         del params['kwargs']
#         # verify the required parameter 'prefixed_key' is set
#         if ('prefixed_key' not in params or
#                 params['prefixed_key'] is None):
#             raise ValueError("Missing the required parameter `prefixed_key` when calling `tfs_tagsprefixed_keyphotos`")  # noqa: E501

#         collection_formats = {}

#         path_params = {}
#         if 'prefixed_key' in params:
#             path_params['prefixedKey'] = params['prefixed_key']  # noqa: E501

#         query_params = []
#         if 'page' in params:
#             query_params.append(('page', params['page']))  # noqa: E501
#         if 'page_size' in params:
#             query_params.append(('pageSize', params['page_size']))  # noqa: E501

#         header_params = {}

#         form_params = []
#         local_var_files = {}

#         body_params = None
#         # HTTP header `Accept`
#         header_params['Accept'] = self.api_client.select_header_accept(
#             ['application/json'])  # noqa: E501

#         # Authentication setting
#         auth_settings = ['bearer']  # noqa: E501

#         return self.api_client.call_api(
#             '/rdb/v1/tags/{prefixedKey}/photos', 'GET',
#             path_params,
#             query_params,
#             header_params,
#             body=body_params,
#             post_params=form_params,
#             files=local_var_files,
#             response_type='ImageDtoPagedResults',  # noqa: E501
#             auth_settings=auth_settings,
#             async_req=params.get('async_req'),
#             _return_http_data_only=params.get('_return_http_data_only'),
#             _preload_content=params.get('_preload_content', True),
#             _request_timeout=params.get('_request_timeout'),
#             collection_formats=collection_formats)

#     def tfs_tagstypekeyphotos(self, type, key, **kwargs):  # noqa: E501
#         """Get a paginated listing of photos assigned to the specified tag  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagstypekeyphotos(type, key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str type: The type of the tagged entity. (Coach, Event, Institution, Player, StatGame) (required)
#         :param int key: The key of the tagged entity (required)
#         :param int page: The page number to fetch
#         :param int page_size: The size of the page to fetch
#         :return: ImageDtoPagedResults
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """
#         kwargs['_return_http_data_only'] = True
#         if kwargs.get('async_req'):
#             return self.tfs_tagstypekeyphotos_with_http_info(type, key, **kwargs)  # noqa: E501
#         else:
#             (data) = self.tfs_tagstypekeyphotos_with_http_info(type, key, **kwargs)  # noqa: E501
#             return data

#     def tfs_tagstypekeyphotos_with_http_info(self, type, key, **kwargs):  # noqa: E501
#         """Get a paginated listing of photos assigned to the specified tag  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagstypekeyphotos_with_http_info(type, key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str type: The type of the tagged entity. (Coach, Event, Institution, Player, StatGame) (required)
#         :param int key: The key of the tagged entity (required)
#         :param int page: The page number to fetch
#         :param int page_size: The size of the page to fetch
#         :return: ImageDtoPagedResults
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """

#         all_params = ['type', 'key', 'page', 'page_size']  # noqa: E501
#         all_params.append('async_req')
#         all_params.append('_return_http_data_only')
#         all_params.append('_preload_content')
#         all_params.append('_request_timeout')

#         params = locals()
#         for key, val in six.iteritems(params['kwargs']):
#             if key not in all_params:
#                 raise TypeError(
#                     "Got an unexpected keyword argument '%s'"
#                     " to method tfs_tagstypekeyphotos" % key
#                 )
#             params[key] = val
#         del params['kwargs']
#         # verify the required parameter 'type' is set
#         if ('type' not in params or
#                 params['type'] is None):
#             raise ValueError("Missing the required parameter `type` when calling `tfs_tagstypekeyphotos`")  # noqa: E501
#         # verify the required parameter 'key' is set
#         if ('key' not in params or
#                 params['key'] is None):
#             raise ValueError("Missing the required parameter `key` when calling `tfs_tagstypekeyphotos`")  # noqa: E501

#         collection_formats = {}

#         path_params = {}
#         if 'type' in params:
#             path_params['type'] = params['type']  # noqa: E501
#         if 'key' in params:
#             path_params['key'] = params['key']  # noqa: E501

#         query_params = []
#         if 'page' in params:
#             query_params.append(('page', params['page']))  # noqa: E501
#         if 'page_size' in params:
#             query_params.append(('pageSize', params['page_size']))  # noqa: E501

#         header_params = {}

#         form_params = []
#         local_var_files = {}

#         body_params = None
#         # HTTP header `Accept`
#         header_params['Accept'] = self.api_client.select_header_accept(
#             ['application/json'])  # noqa: E501

#         # Authentication setting
#         auth_settings = ['bearer']  # noqa: E501

#         return self.api_client.call_api(
#             '/rdb/v1/tags/{type}/{key}/photos', 'GET',
#             path_params,
#             query_params,
#             header_params,
#             body=body_params,
#             post_params=form_params,
#             files=local_var_files,
#             response_type='ImageDtoPagedResults',  # noqa: E501
#             auth_settings=auth_settings,
#             async_req=params.get('async_req'),
#             _return_http_data_only=params.get('_return_http_data_only'),
#             _preload_content=params.get('_preload_content', True),
#             _request_timeout=params.get('_request_timeout'),
#             collection_formats=collection_formats)

#     def tfs_tagstypekeyphotos_0(self, type, key, **kwargs):  # noqa: E501
#         """Create a tagged image  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagstypekeyphotos_0(type, key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str type: (required)
#         :param int key: (required)
#         :param list[str] files:
#         :param int asset_source:
#         :return: list[ImageDto]
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """
#         kwargs['_return_http_data_only'] = True
#         if kwargs.get('async_req'):
#             return self.tfs_tagstypekeyphotos_0_with_http_info(type, key, **kwargs)  # noqa: E501
#         else:
#             (data) = self.tfs_tagstypekeyphotos_0_with_http_info(type, key, **kwargs)  # noqa: E501
#             return data

#     def tfs_tagstypekeyphotos_0_with_http_info(self, type, key, **kwargs):  # noqa: E501
#         """Create a tagged image  # noqa: E501

#         This method makes a synchronous HTTP request by default. To make an
#         asynchronous HTTP request, please pass async_req=True
#         >>> thread = api.tfs_tagstypekeyphotos_0_with_http_info(type, key, async_req=True)
#         >>> result = thread.get()

#         :param async_req bool
#         :param str type: (required)
#         :param int key: (required)
#         :param list[str] files:
#         :param int asset_source:
#         :return: list[ImageDto]
#                  If the method is called asynchronously,
#                  returns the request thread.
#         """

#         all_params = ['type', 'key', 'files', 'asset_source']  # noqa: E501
#         all_params.append('async_req')
#         all_params.append('_return_http_data_only')
#         all_params.append('_preload_content')
#         all_params.append('_request_timeout')

#         params = locals()
#         for key, val in six.iteritems(params['kwargs']):
#             if key not in all_params:
#                 raise TypeError(
#                     "Got an unexpected keyword argument '%s'"
#                     " to method tfs_tagstypekeyphotos_0" % key
#                 )
#             params[key] = val
#         del params['kwargs']
#         # verify the required parameter 'type' is set
#         if ('type' not in params or
#                 params['type'] is None):
#             raise ValueError("Missing the required parameter `type` when calling `tfs_tagstypekeyphotos_0`")  # noqa: E501
#         # verify the required parameter 'key' is set
#         if ('key' not in params or
#                 params['key'] is None):
#             raise ValueError("Missing the required parameter `key` when calling `tfs_tagstypekeyphotos_0`")  # noqa: E501

#         collection_formats = {}

#         path_params = {}
#         if 'type' in params:
#             path_params['type'] = params['type']  # noqa: E501
#         if 'key' in params:
#             path_params['key'] = params['key']  # noqa: E501

#         query_params = []
#         if 'asset_source' in params:
#             query_params.append(('assetSource', params['asset_source']))  # noqa: E501

#         header_params = {}

#         form_params = []
#         local_var_files = {}
#         if 'files' in params:
#             form_params.append(('files', params['files']))  # noqa: E501
#             collection_formats['files'] = 'multi'  # noqa: E501

#         body_params = None
#         # HTTP header `Accept`
#         header_params['Accept'] = self.api_client.select_header_accept(
#             ['application/json'])  # noqa: E501

#         # HTTP header `Content-Type`
#         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
#             ['multipart/form-data'])  # noqa: E501

#         # Authentication setting
#         auth_settings = ['bearer']  # noqa: E501

#         return self.api_client.call_api(
#             '/rdb/v1/tags/{type}/{key}/photos', 'POST',
#             path_params,
#             query_params,
#             header_params,
#             body=body_params,
#             post_params=form_params,
#             files=local_var_files,
#             response_type='list[ImageDto]',  # noqa: E501
#             auth_settings=auth_settings,
#             async_req=params.get('async_req'),
#             _return_http_data_only=params.get('_return_http_data_only'),
#             _preload_content=params.get('_preload_content', True),
#             _request_timeout=params.get('_request_timeout'),
#             collection_formats=collection_formats)