"""
Data models and business logic classes.

This module contains classes for managing data structures and business logic.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class User:
    """
    Represents a user in the system.
    
    Attributes:
        user_id: Unique identifier for the user.
        username: The user's username.
        email: The user's email address.
        created_at: Timestamp when the user was created.
        is_active: Whether the user account is active.
        
    Examples:
        >>> user = User(1, "john_doe", "john@example.com")
        >>> print(user.username)
        'john_doe'
    """
    user_id: int
    username: str
    email: str
    created_at: datetime = datetime.now()
    is_active: bool = True
    
    def get_full_name(self) -> str:
        """
        Get the user's full display name.
        
        Returns:
            The username as the display name.
            
        Examples:
            >>> user = User(1, "john_doe", "john@example.com")
            >>> user.get_full_name()
            'john_doe'
        """
        return self.username
    
    def deactivate(self) -> None:
        """
        Deactivate the user account.
        
        Examples:
            >>> user = User(1, "john_doe", "john@example.com")
            >>> user.deactivate()
            >>> user.is_active
            False
        """
        self.is_active = False


class UserManager:
    """
    Manages user operations and data access.
    
    This class provides methods for creating, retrieving, and managing users.
    
    Attributes:
        users: List of users managed by this manager.
        
    Examples:
        >>> manager = UserManager()
        >>> user = manager.create_user("alice", "alice@example.com")
        >>> print(user.username)
        'alice'
    """
    
    def __init__(self):
        """
        Initialize the UserManager with an empty user list.
        """
        self.users: List[User] = []
    
    def create_user(self, username: str, email: str) -> User:
        """
        Create a new user and add to the manager.
        
        Args:
            username: The desired username.
            email: The user's email address.
            
        Returns:
            The newly created User object.
            
        Raises:
            ValueError: If username already exists.
            
        Examples:
            >>> manager = UserManager()
            >>> user = manager.create_user("bob", "bob@example.com")
            >>> user.username
            'bob'
        """
        if any(u.username == username for u in self.users):
            raise ValueError(f"Username '{username}' already exists")
        
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users.append(user)
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by their ID.
        
        Args:
            user_id: The unique identifier of the user.
            
        Returns:
            The User object if found, None otherwise.
            
        Examples:
            >>> manager = UserManager()
            >>> user = manager.create_user("charlie", "charlie@example.com")
            >>> found = manager.get_user_by_id(1)
            >>> found.username
            'charlie'
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def get_active_users(self) -> List[User]:
        """
        Get all active users.
        
        Returns:
            List of all users with is_active=True.
            
        Examples:
            >>> manager = UserManager()
            >>> manager.create_user("dave", "dave@example.com")
            >>> manager.create_user("eve", "eve@example.com")
            >>> len(manager.get_active_users())
            2
        """
        return [user for user in self.users if user.is_active]
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by their ID.
        
        Args:
            user_id: The unique identifier of the user to delete.
            
        Returns:
            True if user was deleted, False if not found.
            
        Examples:
            >>> manager = UserManager()
            >>> user = manager.create_user("frank", "frank@example.com")
            >>> manager.delete_user(1)
            True
            >>> manager.delete_user(999)
            False
        """
        for i, user in enumerate(self.users):
            if user.user_id == user_id:
                del self.users[i]
                return True
        return False


class DataProcessor:
    """
    Processes and transforms data.
    
    This class provides various data processing utilities and transformations.
    
    Examples:
        >>> processor = DataProcessor()
        >>> result = processor.calculate_average([1, 2, 3, 4, 5])
        >>> result
        3.0
    """
    
    def __init__(self, precision: int = 2):
        """
        Initialize the DataProcessor.
        
        Args:
            precision: Number of decimal places for calculations.
        """
        self.precision = precision
    
    def calculate_average(self, numbers: List[float]) -> float:
        """
        Calculate the average of a list of numbers.
        
        Args:
            numbers: List of numbers to average.
            
        Returns:
            The average value rounded to the specified precision.
            
        Raises:
            ValueError: If the list is empty.
            
        Examples:
            >>> processor = DataProcessor()
            >>> processor.calculate_average([1.0, 2.0, 3.0])
            2.0
        """
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        
        average = sum(numbers) / len(numbers)
        return round(average, self.precision)
    
    def filter_by_threshold(self, numbers: List[float], threshold: float) -> List[float]:
        """
        Filter numbers greater than a threshold.
        
        Args:
            numbers: List of numbers to filter.
            threshold: Minimum value to include.
            
        Returns:
            List of numbers greater than the threshold.
            
        Examples:
            >>> processor = DataProcessor()
            >>> processor.filter_by_threshold([1, 5, 3, 7, 2], 4)
            [5.0, 7.0]
        """
        return [num for num in numbers if num > threshold]
    
    def normalize_data(self, numbers: List[float]) -> List[float]:
        """
        Normalize numbers to range [0, 1].
        
        Args:
            numbers: List of numbers to normalize.
            
        Returns:
            List of normalized numbers.
            
        Raises:
            ValueError: If the list is empty or contains identical values.
            
        Examples:
            >>> processor = DataProcessor()
            >>> processor.normalize_data([0, 5, 10])
            [0.0, 0.5, 1.0]
        """
        if not numbers:
            raise ValueError("Cannot normalize empty list")
        
        min_val = min(numbers)
        max_val = max(numbers)
        
        if max_val == min_val:
            raise ValueError("Cannot normalize list with identical values")
        
        return [round((num - min_val) / (max_val - min_val), self.precision) 
                for num in numbers]