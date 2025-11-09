const { gql } = require('apollo-server-express');

// Define GraphQL schema using SDL (Schema Definition Language)
const typeDefs = gql`
  """
  User type represents a user in our system
  """
  type User {
    id: ID!
    name: String!
    email: String!
    age: Int
    role: Role
    createdAt: String
  }

  """
  UserProfile type represents a user's profile data
  """
  type UserProfile {
    id: ID!
    username: String!
    email: String!
    displayName: String
    bio: String
    role: Role
    createdAt: String
    lastLogin: String
  }

  """
  Possible user roles in the system
  """
  enum Role {
    ADMIN
    USER
    GUEST
  }

  """
  Input type for creating a new user
  """
  input CreateUserInput {
    name: String!
    email: String!
    age: Int
    role: Role
  }

  """
  Input type for updating an existing user
  """
  input UpdateUserInput {
    name: String
    email: String
    age: Int
    role: Role
  }

  """
  Root Query type
  """
  type Query {
    """
    Get a user by ID
    """
    user(id: ID!): User

    """
    Get all users
    """
    users: [User]!

    """
    Get total number of users
    """
    userCount: Int!

    """
    Get the current authenticated user's profile
    Requires authentication - returns null if not authenticated
    """
    me: UserProfile
  }

  """
  Root Mutation type
  """
  type Mutation {
    """
    Create a new user
    """
    createUser(input: CreateUserInput!): User!

    """
    Update an existing user
    """
    updateUser(id: ID!, input: UpdateUserInput!): User

    """
    Delete a user by ID
    """
    deleteUser(id: ID!): Boolean!
  }
`;

module.exports = typeDefs;