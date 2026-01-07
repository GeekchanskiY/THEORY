GraphQL is an open-source data query and manipulation language for APIs and a query runtime engine. GraphQL enables declarative data fetching where a client can specify exactly what data it needs from an API

### Type system

The root type of a GraphQL schema, `Query` by default, contains all of the fields that can be queried. Other types define the objects and fields that the GraphQL server can return. There are several base types, called scalars, to represent things like strings, numbers, and IDs.

Fields are defined as nullable by default, and a trailing exclamation mark can be used to make a field non-nullable (required). A field can be defined as a list by wrapping the field's type in square brackets (for example, `authors: [String]`)

```graphql
type Query {
  currentUser: User
}

type User {
  id: ID!
  name: String!
}
```

### Queries
A GraphQL query defines the exact shape of the data needed by the client.

```graphql
query CurrentUser {
  currentUser {
    name
    age
  }
}
```

Once validated and executed by the GraphQL server, the data is returned in the same shape.

### Mutations
A GraphQL mutation allows for data to be created, updated, or deleted. Mutations generally contain _variables_, which allow data to be passed into the server from the client. The mutation also defines the shape of the data that will be returned to the client after the operation is complete.
```graphql
mutation CreateUser($name: String!, $age: Int!) {
  createUser(userName: $name, age: $age) {
    name
    age
  }
}
```

### Subscriptions
GraphQL also supports live updates sent from the server to client in an operation called a subscription. Again, the client defines the shape of the data that it needs whenever an update is made.
```graphql
subscription {
  newPerson {
    name
    age
  }
}
```
When a mutation is made through the GraphQL server that updates the associated field, data is sent to all subscribed clients in the format setup through the subscription.