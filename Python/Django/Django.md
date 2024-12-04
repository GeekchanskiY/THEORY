

## ORM Problems

There are several potential problems that you might encounter when using the Django ORM (Object-Relational Mapper). Here are a few common issues:
1. Database performance issues: If you're experiencing poor database performance, there are several things you can try to improve it. You can use the Django ORM's query optimization features, such as select_related() and prefetch_related(), to 46 reduce the number of queries you need to run. You can also use indexes to improve the performance of your queries. 
2. Inconsistent data: If you're seeing inconsistent or unexpected data in your Django application, it could be due to a variety of issues. You might be experiencing race conditions, where multiple threads or processes are trying to update the same data simultaneously. You might also be experiencing issues with transactions, if you're using them to manage data consistency.
3. Complex relationships: If you have complex relationships between your models, it can be challenging to represent them using the Django ORM. You might need to use special field types, such as ForeignKey and ManyToManyField, to represent relationships between models.
4. Model design issues: If you're experiencing problems with your Django models, it could be due to poor model design. For example, you might have an overly complex model structure, or you might be using inappropriate field types for your data.


## Signals
In Django, signals are used to allow certain actions to be taken when certain events occur in the application. They're used to allow decoupled applications get notified when certain actions occur elsewhere in the application. For example, you might use a signal to send an email to the site administrator every time a new user registers for the site. Or you might use a signal to update a search index every time an object is saved to the database. To use signals in Django, you'll need to do the following: 
1. Define the signal you want to use. This involves creating a signal object and specifying the action that should be taken when the signal is sent.
2. Connect the signal to the event you want to trigger it. This involves creating a receiver function that will be called when the signal is sent, and connecting it to the signal using the @receiver decorator. 
3. Send the signal when the appropriate event occurs. This involves calling the send() method of the signal object and passing any necessary arguments.


In Django, signals are triggered when certain events occur in the application. These events can be triggered by a variety of actions, such as saving an object to the database, deleting an object, or updating a field on an object. For example, the post_save signal is triggered every time an object is saved to the database. The pre_delete signal is triggered just before an object is deleted from the database. And the pre_save signal is triggered just before an object is saved to the database.

To summarize, signals in Django are used to allow certain actions to be taken when certain events occur in the application. They're defined using the Signal object, connected to events using the @receiver decorator, and sent using the send() method

Django + Amazon Web Services setup:
https://dev.to/vaddimart/deploy-django-app-on-aws-lambda-using-serverless-part-1-1i90