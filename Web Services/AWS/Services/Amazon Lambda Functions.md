

### Lambda layers
AWS Lambda layers are a distribution mechanism for libraries, custom runtimes, and custom extensions. Layers let you manage your in-development function code independently from the unchanging code and resources that it uses. Lambda layers are a distribution mechanism for libraries, custom runtimes, and custom extensions. They allow you to manage your in-development function code independently from the unchanging code and resources that it uses. This can make it easier to manage and deploy your serverless applications. Here are some benefits of using Lambda layers:
● You can manage the common code that is used across multiple functions in a single place. 
● You can share code across multiple accounts.
● You can manage the common code independently from the function code. 
● You can reduce duplication of code in your deployment package. 
To use a layer in a function, you need to specify the Amazon Resource Name (ARN) of the layer when you create a function or update an existing function. You can specify up to five layers for a function. Lambda layers are a useful way to manage and share common code and resources in your serverless applications. They can help you reduce duplication and make it easier to manage and deploy your functions.

### Cold/Hot start
A cold start occurs when a new instance of a Lambda function is created to run a specific request. This can happen when the function has not been used in a while, or when the function is being used for the first time. Cold starts can introduce latency in your serverless application because it takes time to create a new instance of the function and run the request. There are several factors that can affect the cold start performance of a Lambda function: 
● Language runtime: Some language runtimes have a longer startup time than others. For example, a Python function may have a longer cold start time compared to a Node.js function. 
● Package size: The larger the package size of your function, the longer it will take to cold start. 
● Function memory size: The more memory you allocate to your function, the faster it will start up. However, this will also increase the cost of running your function. There are several ways you can optimize cold start performance for your Lambda functions: 
● Use a language runtime that has a fast startup time. 
● Keep the package size of your function as small as possible. 
● Allocate enough memory to your function to reduce startup time, but not so much that it becomes too expensive to run. 
● Use a function warming tool to keep your functions warm and reduce the frequency of cold starts.
● Use Provisioned Concurrency to keep a certain number of instances of your function running and warmed up at all times. Cold starts can introduce latency in your serverless applications, but there are ways to optimize cold start performance and minimize the impact on your application's performance.


Provision concurrency

React hooks, redux, lifecycle