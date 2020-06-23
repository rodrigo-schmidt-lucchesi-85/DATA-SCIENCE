# AWS
---

Serveless computing

*Serverless architectures are application designs that incorporate third-party “Backend as a Service” (BaaS) services, and/or that include custom code run in managed, ephemeral containers on a “Functions as a Service” (FaaS) platform. By using these ideas, and related ones like single-page applications, such architectures remove much of the need for a traditional always-on server component. Serverless architectures may benefit from significantly reduced operational cost, complexity, and engineering lead time, at a cost of increased reliance on vendor dependencies and comparatively immature supporting services.*

Focus on your application, no the infrastructure

## Function as a service
---

### Lambda function 

- You can insert any function inside that works
- Fast
- Not good for small projects
- If you work with Lambda you must use AWS
- Monitor on CloudWatch
- Event == route
- Specify things


### Sagemaker

Types of deployment:

- Real time Prediction: Mainly used for low latency, and interactive use cases where getting the inference in real time is very important;
- Batch Prediction: Used for cases where complete dataset or batch of dataset is sent for prediction;


Algorithms:

- Sklearn
- Pythorch
- Tensorflow
- MxNet
- Chainer

