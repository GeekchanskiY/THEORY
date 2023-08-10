The Saga design pattern is a way to manage data consistency across microservices in distributed transaction scenarios. A saga is a sequence of transactions that updates each service and publishes a message or event to trigger the next transaction step. If a step fails, the saga executes compensating transactions that counteract the preceding transactions.

![[SAGA Pattern.png]]

The Saga pattern provides transaction management using a sequence of _local transactions_. A local transaction is the atomic work effort performed by a saga participant. Each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga. If a local transaction fails, the saga executes a series of _compensating transactions_ that undo the changes that were made by the preceding local transactions.

In Saga patterns:

- _Compensable transactions_ are transactions that can potentially be reversed by processing another transaction with the opposite effect.
- A _pivot transaction_ is the go/no-go point in a saga. If the pivot transaction commits, the saga runs until completion. A pivot transaction can be a transaction that is neither compensable nor retryable, or it can be the last compensable transaction or the first retryable transaction in the saga.
- _Retryable transactions_ are transactions that follow the pivot transaction and are guaranteed to succeed.

There are two common saga implementation approaches, _choreography_ and _orchestration_. Each approach has its own set of challenges and technologies to coordinate the workflow.