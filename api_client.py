"""
API client for external service integration.

This module provides a client class for making HTTP requests to external APIs
with proper error handling and response processing.
"""

import json
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from enum import Enum


class HTTPMethod(Enum):
    """HTTP methods supported by the API client."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


@dataclass
class APIResponse:
    """
    Represents an API response.
    
    Attributes:
        status_code: HTTP status code.
        data: Response data as dictionary.
        headers: Response headers.
        success: Whether the request was successful.
        
    Examples:
        >>> response = APIResponse(200, {"user": "john"}, {}, True)
        >>> response.success
        True
    """
    status_code: int
    data: Dict[str, Any]
    headers: Dict[str, str]
    success: bool
    
    def get_error_message(self) -> str:
        """
        Get error message from failed response.
        
        Returns:
            Error message string or empty string if successful.
            
        Examples:
            >>> response = APIResponse(404, {"error": "Not found"}, {}, False)
            >>> response.get_error_message()
            'Not found'
        """
        if self.success:
            return ""
        return self.data.get("error", "Unknown error")


class APIClient:
    """
    HTTP client for making API requests.
    
    This class provides methods for making HTTP requests to external APIs
    with built-in error handling and response processing.
    
    Attributes:
        base_url: Base URL for all API requests.
        timeout: Request timeout in seconds.
        headers: Default headers for all requests.
        
    Examples:
        >>> client = APIClient("https://api.example.com")
        >>> client.set_auth_header("Bearer token123")
        >>> response = client.get("/users/1")
        >>> response.success
        True
    """
    
    def __init__(self, base_url: str, timeout: int = 30):
        """
        Initialize the API client.
        
        Args:
            base_url: Base URL for API requests.
            timeout: Request timeout in seconds.
            
        Examples:
            >>> client = APIClient("https://api.example.com", timeout=60)
            >>> client.base_url
            'https://api.example.com'
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    
    def set_auth_header(self, auth_token: str) -> None:
        """
        Set authentication header for requests.
        
        Args:
            auth_token: Authentication token (e.g., "Bearer token123").
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> client.set_auth_header("Bearer token123")
            >>> "Authorization" in client.headers
            True
        """
        self.headers["Authorization"] = auth_token
    
    def set_header(self, key: str, value: str) -> None:
        """
        Set a custom header for requests.
        
        Args:
            key: Header name.
            value: Header value.
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> client.set_header("X-Custom-Header", "value")
            >>> client.headers["X-Custom-Header"]
            'value'
        """
        self.headers[key] = value
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a GET request.
        
        Args:
            endpoint: API endpoint path.
            params: Query parameters.
            
        Returns:
            APIResponse object with the response data.
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> response = client.get("/users", {"page": 1})
            >>> response.status_code
            200
        """
        return self._make_request(HTTPMethod.GET, endpoint, params=params)
    
    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a POST request.
        
        Args:
            endpoint: API endpoint path.
            data: Request body data.
            
        Returns:
            APIResponse object with the response data.
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> response = client.post("/users", {"name": "John"})
            >>> response.status_code
            201
        """
        return self._make_request(HTTPMethod.POST, endpoint, data=data)
    
    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a PUT request.
        
        Args:
            endpoint: API endpoint path.
            data: Request body data.
            
        Returns:
            APIResponse object with the response data.
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> response = client.put("/users/1", {"name": "Jane"})
            >>> response.status_code
            200
        """
        return self._make_request(HTTPMethod.PUT, endpoint, data=data)
    
    def delete(self, endpoint: str) -> APIResponse:
        """
        Make a DELETE request.
        
        Args:
            endpoint: API endpoint path.
            
        Returns:
            APIResponse object with the response data.
            
        Examples:
            >>> client = APIClient("https://api.example.com")
            >>> response = client.delete("/users/1")
            >>> response.status_code
            204
        """
        return self._make_request(HTTPMethod.DELETE, endpoint)
    
    def _make_request(
        self, 
        method: HTTPMethod, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> APIResponse:
        """
        Internal method to make HTTP requests.
        
        Args:
            method: HTTP method to use.
            endpoint: API endpoint path.
            params: Query parameters.
            data: Request body data.
            
        Returns:
            APIResponse object with the response data.
            
        Note:
            This is a mock implementation. In production, use requests library.
        """
        # Mock implementation for demonstration
        url = f"{self.base_url}{endpoint}"
        
        # Simulate successful response
        mock_data = {
            "url": url,
            "method": method.value,
            "params": params or {},
            "data": data or {}
        }
        
        return APIResponse(
            status_code=200,
            data=mock_data,
            headers={"Content-Type": "application/json"},
            success=True
        )


class ServiceRegistry:
    """
    Registry for managing multiple API services.
    
    This class allows management of multiple API clients for different services.
    
    Attributes:
        services: Dictionary of registered API clients.
        
    Examples:
        >>> registry = ServiceRegistry()
        >>> registry.register_service("users", "https://api.example.com/users")
        >>> client = registry.get_client("users")
        >>> client.base_url
        'https://api.example.com/users'
    """
    
    def __init__(self):
        """
        Initialize the service registry.
        """
        self.services: Dict[str, APIClient] = {}
    
    def register_service(self, name: str, base_url: str, timeout: int = 30) -> APIClient:
        """
        Register a new API service.
        
        Args:
            name: Service name/identifier.
            base_url: Base URL for the service.
            timeout: Request timeout in seconds.
            
        Returns:
            The created APIClient instance.
            
        Raises:
            ValueError: If service name already exists.
            
        Examples:
            >>> registry = ServiceRegistry()
            >>> client = registry.register_service("users", "https://api.example.com")
            >>> "users" in registry.services
            True
        """
        if name in self.services:
            raise ValueError(f"Service '{name}' already registered")
        
        client = APIClient(base_url, timeout)
        self.services[name] = client
        return client
    
    def get_client(self, name: str) -> Optional[APIClient]:
        """
        Get a registered API client by name.
        
        Args:
            name: Service name.
            
        Returns:
            APIClient instance if found, None otherwise.
            
        Examples:
            >>> registry = ServiceRegistry()
            >>> registry.register_service("users", "https://api.example.com")
            >>> client = registry.get_client("users")
            >>> client is not None
            True
        """
        return self.services.get(name)
    
    def list_services(self) -> List[str]:
        """
        List all registered service names.
        
        Returns:
            List of service names.
            
        Examples:
            >>> registry = ServiceRegistry()
            >>> registry.register_service("users", "https://api.example.com")
            >>> registry.register_service("products", "https://api.example.com")
            >>> len(registry.list_services())
            2
        """
        return list(self.services.keys())
    
    def remove_service(self, name: str) -> bool:
        """
        Remove a registered service.
        
        Args:
            name: Service name to remove.
            
        Returns:
            True if service was removed, False if not found.
            
        Examples:
            >>> registry = ServiceRegistry()
            >>> registry.register_service("users", "https://api.example.com")
            >>> registry.remove_service("users")
            True
            >>> registry.remove_service("nonexistent")
            False
        """
        if name in self.services:
            del self.services[name]
            return True
        return False