# Sample GraphQL Queries

This document contains sample GraphQL queries that you can use to test the API. You can run these queries using the GraphiQL interface at http://127.0.0.1:5000/graphql after starting the server.

## Fetching all books

```graphql
query {
  books {
    id
    title
    publicationYear
    genre
    author {
      name
    }
  }
}
```

## Fetching a specific book by ID

```graphql
query {
  book(id: "1") {
    id
    title
    publicationYear
    genre
    author {
      id
      name
      birthDate
    }
  }
}
```

## Fetching all authors

```graphql
query {
  authors {
    id
    name
    birthDate
    books {
      id
      title
    }
  }
}
```

## Fetching a specific author by ID

```graphql
query {
  author(id: "1") {
    id
    name
    birthDate
    books {
      id
      title
      publicationYear
      genre
    }
  }
}
```

## Filtering books by genre

```graphql
query {
  books(genre: "Fantasy") {
    id
    title
    publicationYear
    author {
      name
    }
  }
}
```

## Nested query example

```graphql
query {
  authors {
    id
    name
    books {
      title
      publicationYear
      genre
    }
  }
}
```