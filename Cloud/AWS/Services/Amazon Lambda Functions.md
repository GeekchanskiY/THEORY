
Restrictions:
 - Concurrent executions: 100
 - Function and layer storage: 75GB
 - Elastic network interfaces per VPC: 250
P.S. About elastic networks: 
There are use cases where a Lambda function needs VPC resources such as RDS -mysql. In that case, you need to configure the VPC subnet and AZs for the Lambda function. The Lambda function connects to these VPC resources through the Elastic Network Interface (ENI).

Hard Limits:
![[Pasted image 20240220172443.png]]

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

AWS Lambda cold starts occur when a function is invoked after not being used for some time, and it needs to initialize its resources, resulting in longer response times. Reducing cold starts can improve the overall performance and user experience of your serverless applications. Here are several ways to mitigate Lambda cold starts:

1. **Provisioned Concurrency**: Provisioned Concurrency is a feature that allows you to allocate a specific number of initialized execution environments (instances) to your Lambda function. This keeps instances "warm," reducing the likelihood of cold starts. With provisioned concurrency, your function is always ready to handle incoming requests without any initialization delays.

2. **Warm-up Scripts**: Warm-up scripts are essentially scheduled invocations of your Lambda function. You can create a separate Lambda function or use a tool like AWS CloudWatch Events to schedule periodic invocations of your primary Lambda function. These scheduled invocations keep the function warm, preventing cold starts when the actual traffic arrives.

3. **Scheduled Invocations**: Besides using warm-up scripts, you can schedule your Lambda function to run at specific intervals, even if you don't have a particular use case. By doing this, you keep the function warm and reduce the chances of cold starts when it's eventually needed.

4. **API Gateway Integration**: When using AWS API Gateway to trigger your Lambda function, you can enable the "Keep warm" option. This will automatically send periodic requests to your function, keeping it warm and reducing cold starts.

5. **Concurrency Reservations**: If you expect sudden spikes in traffic or you need to ensure low-latency responses for critical operations, you can set up concurrency reservations for your Lambda function. This ensures that a specific number of execution environments are always available, even during periods of high demand.

6. **Optimize Function Code**: Reducing the size and complexity of your Lambda function's code can help decrease the time it takes to initialize resources during cold starts. Minimize unnecessary dependencies and use efficient code practices.

7. **Use Lambda Layers**: If your function depends on large libraries, consider using Lambda Layers to separate these libraries from your function code. Lambda Layers are loaded separately and can remain cached, reducing the impact of cold starts on your primary function.

8. **Increase Function Memory**: Lambda function memory allocation is directly related to the CPU and network resources provided to the function. Increasing memory can lead to quicker function initialization and potentially reduce cold start times.

9. **Retain Connections**: For functions that maintain database or network connections, consider reusing existing connections instead of creating new ones for each invocation. This can help reduce the initialization time during cold starts.

Remember that cold starts are an inherent aspect of serverless computing. While you can reduce their frequency and impact using these techniques, it may not be possible to completely eliminate them. The most appropriate approach depends on your application's specific requirements and usage patterns.