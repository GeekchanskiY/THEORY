https://k21academy.com/terraform-iac/terraform-beginners-guide/

## **What Is Terraform?**

**Terraform** is one of the most popular [[Infrastructure as Code]] (IaC) tool, used by DevOps teams to automate infrastructure tasks. It is used to automate the provisioning of your cloud resources. Terraform is an open-source, cloud-agnostic provisioning tool developed by HashiCorp and written in GO language.
**Benefits of using Terraform:**

- Does orchestration, not just configuration management
- Supports multiple providers such as AWS, Azure, Oracle, GCP, and many more
- Provide immutable infrastructure where configuration changes smoothly
- Uses easy to understand language, HCL (HashiCorp configuration language)
- Easily portable to any other provider
### Terraform Lifecycle
![[terraform-lifecycle-1024x145.png]]
1. **Terraform init** initializes the (local) Terraform environment. Usually executed only once per session.  
2. **Terraform plan** compares the Terraform state with the as-is state in the cloud, build and display an  
execution plan. This does not change the deployment (read-only).  
3. **Terraform apply** executes the plan. This potentially changes the deployment.  
4. **Terraform destroy** deletes all resources that are governed by this specific terraform environment.

## **Terraform Core Concepts**

**1. Variables**: Terraform has input and output variables, it is a key-value pair. Input variables are used as parameters to input values at run time to customize our deployments. Output variables are return values of a terraform module that can be used by other configurations.  
Read our blog on **[Terraform Variables](https://k21academy.com/terraform-iac/variables-in-terraform/)**

**2. Provider**: Terraform users provision their infrastructure on the major cloud providers such as AWS, Azure, OCI, and others. A _provider_ is a plugin that interacts with the various APIs required to create, update, and delete various resources.  
Read our blog to know more about **[Terraform Providers](https://k21academy.com/terraform-iac/terraform-providers-overview/)**

**3. Module**: Any set of Terraform configuration files in a folder is a _module_. Every Terraform configuration has at least one module, known as its **_root module._**

**4. State**: Terraform records information about what infrastructure is created in a Terraform _state_ file. With the state file, Terraform is able to find the resources it created previously, supposed to manage and update them accordingly.

**5. Resources**: Cloud Providers provides various services in their offerings, they are referenced as Resources in Terraform. Terraform resources can be anything from compute instances, virtual networks to higher-level components such as DNS records. Each resource has its own attributes to define that resource.

**6. Data Source**: Data source performs a read-only operation. It allows data to be fetched or computed from resources/entities that are not defined or managed by Terraform or the current Terraform configuration.

**7. Plan**: It is one of the stages in the Terraform lifecycle where it determines what needs to be created, updated, or destroyed to move from the real/current state of the infrastructure to the desired state.

**8. Apply**: It is one of the stages in the Terraform lifecycle where it applies the changes real/current state of the infrastructure in order to achieve the desired state.

**Check Out:** Our previous blog post on [**Terraform Cheat Sheet**](https://k21academy.com/terraform-iac/terraform-cheat-sheet/).


// useful links
https://developer.hashicorp.com/terraform/tutorials