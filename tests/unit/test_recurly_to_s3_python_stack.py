import aws_cdk as core
import aws_cdk.assertions as assertions

from recurly_to_s3_python.recurly_to_s3_python_stack import RecurlyToS3PythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in recurly_to_s3_python/recurly_to_s3_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = RecurlyToS3PythonStack(app, "recurly-to-s3-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
