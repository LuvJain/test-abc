# GraphQL Server Infrastructure

A Node.js GraphQL server implementation with code-first schema generation, built with Apollo Server and Express.

## Features

- GraphQL endpoint established at `/graphql`
- Schema generated automatically from type definitions
- Basic query and mutation support implemented
- Introspection enabled for development environment
- Performance monitoring middleware added

## Project Structure

```
├── src/
│   ├── index.js            # Main server entry point
│   ├── config.js           # Configuration settings
│   ├── middleware/
│   │   └── performance.js  # Performance monitoring middleware
│   ├── models/
│   │   └── User.js         # User model with mock database
│   ├── resolvers/
│   │   ├── index.js        # Combined resolvers
│   │   └── userResolvers.js # User-specific resolvers
│   └── schemas/
│       └── typeDefs.js     # GraphQL type definitions
├── package.json
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm or yarn

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   npm install
   ```
3. Start the server:
   ```
   npm start
   ```

For development with auto-restart:
   ```
   npm run dev
   ```

## Using the GraphQL API

Once the server is running, you can access the GraphQL Playground at:
```
http://localhost:4000/graphql
```

### Example Queries

Get all users:
```graphql
query {
  users {
    id
    name
    email
    age
    role
  }
}
```

Get a specific user:
```graphql
query {
  user(id: "1") {
    id
    name
    email
  }
}
```

### Example Mutations

Create a new user:
```graphql
mutation {
  createUser(input: {
    name: "Alice Johnson"
    email: "alice@example.com"
    age: 28
    role: USER
  }) {
    id
    name
    email
  }
}
```

Update an existing user:
```graphql
mutation {
  updateUser(
    id: "1",
    input: {
      name: "John Doe Updated"
    }
  ) {
    id
    name
    email
  }
}
```

Delete a user:
```graphql
mutation {
  deleteUser(id: "1")
}
```

## Configuration

Server configuration is managed in `src/config.js`. Key settings include:

- Server port and environment
- GraphQL introspection settings
- Performance monitoring thresholds

## Performance Monitoring

The GraphQL server includes a performance monitoring middleware that:

1. Measures execution time of each resolver
2. Logs slow queries (configurable threshold)
3. Provides detailed logs in development mode

To enable detailed logging in development:
```
DEBUG_GRAPHQL=true npm run dev
```