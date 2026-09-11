"""
Database models and ORM-like functionality.

This module provides base classes and utilities for database models.
"""

from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod
from datetime import datetime


class DatabaseModel(ABC):
    """
    Abstract base class for database models.
    
    This class provides common functionality for all database models
    including CRUD operations and field management.
    
    Attributes:
        id: Primary key identifier.
        created_at: Timestamp when record was created.
        updated_at: Timestamp when record was last updated.
        
    Examples:
        >>> class User(DatabaseModel):
        ...     def __init__(self, name):
        ...         super().__init__()
        ...         self.name = name
        >>> user = User("John")
        >>> user.created_at is not None
        True
    """
    
    def __init__(self):
        """
        Initialize the database model.
        """
        self.id: Optional[int] = None
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert model to dictionary representation.
        
        Returns:
            Dictionary representation of the model.
            
        Examples:
            >>> class User(DatabaseModel):
            ...     def __init__(self, name):
            ...         super().__init__()
            ...         self.name = name
            ...     def to_dict(self):
            ...         return {"name": self.name}
            >>> user = User("John")
            >>> user.to_dict()
            {'name': 'John'}
        """
        pass
    
    @abstractmethod
    def from_dict(self, data: Dict[str, Any]) -> 'DatabaseModel':
        """
        Create model instance from dictionary.
        
        Args:
            data: Dictionary containing model data.
            
        Returns:
            Model instance populated with data.
            
        Examples:
            >>> class User(DatabaseModel):
            ...     def __init__(self, name=""):
            ...         super().__init__()
            ...         self.name = name
            ...     def to_dict(self):
            ...         return {"name": self.name}
            ...     def from_dict(self, data):
            ...         self.name = data.get("name", "")
            ...         return self
            >>> user = User().from_dict({"name": "Jane"})
            >>> user.name
            'Jane'
        """
        pass
    
    def save(self) -> bool:
        """
        Save the model to database.
        
        Returns:
            True if save successful, False otherwise.
            
        Examples:
            >>> class User(DatabaseModel):
            ...     def __init__(self, name=""):
            ...         super().__init__()
            ...         self.name = name
            ...     def to_dict(self):
            ...         return {"name": self.name}
            ...     def from_dict(self, data):
            ...         self.name = data.get("name", "")
            ...         return self
            >>> user = User("John")
            >>> result = user.save()
            >>> result
            True
        """
        self.updated_at = datetime.now()
        # Mock save operation
        return True
    
    def delete(self) -> bool:
        """
        Delete the model from database.
        
        Returns:
            True if delete successful, False otherwise.
            
        Examples:
            >>> class User(DatabaseModel):
            ...     def __init__(self, name=""):
            ...         super().__init__()
            ...         self.name = name
            ...     def to_dict(self):
            ...         return {"name": self.name}
            ...     def from_dict(self, data):
            ...         self.name = data.get("name", "")
            ...         return self
            >>> user = User("John")
            >>> result = user.delete()
            >>> result
            True
        """
        # Mock delete operation
        return True
    
    def update_timestamp(self) -> None:
        """
        Update the modified timestamp.
        
        Examples:
            >>> class User(DatabaseModel):
            ...     def __init__(self, name=""):
            ...         super().__init__()
            ...         self.name = name
            ...     def to_dict(self):
            ...         return {"name": self.name}
            ...     def from_dict(self, data):
            ...         self.name = data.get("name", "")
            ...         return self
            >>> user = User("John")
            >>> old_time = user.updated_at
            >>> user.update_timestamp()
            >>> user.updated_at > old_time
            True
        """
        self.updated_at = datetime.now()


class QueryBuilder:
    """
    Builder for constructing database queries.
    
    This class provides a fluent interface for building SQL queries
    with method chaining.
    
    Attributes:
        table: Target table name.
        conditions: Query conditions.
        fields: Fields to select.
        
    Examples:
        >>> builder = QueryBuilder("users")
        >>> query = builder.select("name", "email").where("id", 1).build()
        >>> "SELECT" in query
        True
    """
    
    def __init__(self, table: str):
        """
        Initialize the query builder.
        
        Args:
            table: Target table name.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> builder.table
            'users'
        """
        self.table = table
        self.conditions: List[str] = []
        self.fields: List[str] = []
        self.order_by: Optional[str] = None
        self.limit: Optional[int] = None
    
    def select(self, *fields: str) -> 'QueryBuilder':
        """
        Specify fields to select.
        
        Args:
            *fields: Field names to select.
            
        Returns:
            Self for method chaining.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> builder.select("name", "email")
            >>> len(builder.fields)
            2
        """
        self.fields.extend(fields)
        return self
    
    def where(self, field: str, value: Any) -> 'QueryBuilder':
        """
        Add a WHERE condition.
        
        Args:
            field: Field name.
            value: Field value.
            
        Returns:
            Self for method chaining.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> builder.where("id", 1)
            >>> len(builder.conditions)
            1
        """
        self.conditions.append(f"{field} = {repr(value)}")
        return self
    
    def order(self, field: str, direction: str = "ASC") -> 'QueryBuilder':
        """
        Add ORDER BY clause.
        
        Args:
            field: Field to order by.
            direction: Sort direction (ASC or DESC).
            
        Returns:
            Self for method chaining.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> builder.order("created_at", "DESC")
            >>> builder.order_by
            'created_at DESC'
        """
        self.order_by = f"{field} {direction}"
        return self
    
    def limit(self, count: int) -> 'QueryBuilder':
        """
        Add LIMIT clause.
        
        Args:
            count: Maximum number of results.
            
        Returns:
            Self for method chaining.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> builder.limit(10)
            >>> builder.limit
            10
        """
        self.limit = count
        return self
    
    def build(self) -> str:
        """
        Build the final SQL query.
        
        Returns:
            Complete SQL query string.
            
        Examples:
            >>> builder = QueryBuilder("users")
            >>> query = builder.select("name").where("id", 1).build()
            >>> "SELECT" in query
            True
        """
        fields = ", ".join(self.fields) if self.fields else "*"
        query = f"SELECT {fields} FROM {self.table}"
        
        if self.conditions:
            query += " WHERE " + " AND ".join(self.conditions)
        
        if self.order_by:
            query += f" ORDER BY {self.order_by}"
        
        if self.limit:
            query += f" LIMIT {self.limit}"
        
        return query