# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Purpose

Shows how to use the AWS SDK for Python (Boto3) with the Amazon Bedrock Runtime client
to run inferences using Anthropic Claude 3 models.
"""

import json
import logging
from dotenv import load_dotenv
import os

import boto3
from botocore.exceptions import ClientError
from web_scrape import scrapeWebsite

logger = logging.getLogger(__name__)
EXIT_FUNCTIONS = ['q', 'quit', 'leave', 'url', 'exit', 'esc', 'escape']


# snippet-start:[python.example_code.bedrock-runtime.Claude3Wrapper.class]
class Claude3Wrapper:
    """Encapsulates Claude 3 model invocations using the Amazon Bedrock Runtime client."""

    def __init__(self, client=None):
        """
        :param client: A low-level client representing Amazon Bedrock Runtime.
                       Describes the API operations for running inference using Bedrock models.
                       Default: None
        """
        self.client = client

    # snippet-start:[python.example_code.bedrock-runtime.InvokeAnthropicClaude3Text]
    def invoke_claude_3_with_text(self, prompt):
        """
        Invokes Anthropic Claude 3 Sonnet to run an inference using the input
        provided in the request body.

        :param prompt: The prompt that you want Claude 3 to complete.
        :return: Inference response from the model.
        """

        # Initialize the Amazon Bedrock runtime client
        client = self.client or boto3.client(
            service_name="bedrock-runtime", region_name="us-east-1"
        )

        # Invoke Claude 3 with the text prompt
        model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

        try:
            response = client.invoke_model(
                modelId=model_id,
                body=json.dumps(
                    {
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "role": "user",
                                "content": [{"type": "text", "text": prompt}],
                            }
                        ],
                    }
                ),
            )

            # Process and print the response
            result = json.loads(response.get("body").read())
            input_tokens = result["usage"]["input_tokens"]
            output_tokens = result["usage"]["output_tokens"]
            output_list = result.get("content", [])
            for output in output_list:
                print("Response: " + output["text"])

            return result

        except ClientError as err:
            logger.error(
                "Couldn't invoke Claude 3 Sonnet. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise

    # snippet-end:[python.example_code.bedrock-runtime.InvokeAnthropicClaude3Text]

# snippet-end:[python.example_code.bedrock-runtime.Claude3Wrapper.class]


def usage_demo():
    """
    Demonstrates the invocation of Claude 3 models.
    """

    print("-" * 88)
    print("Initializing the Amazon Bedrock Runtime demo with Anthropic Claude 3.")
    print("-" * 88)

    client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
    wrapper = Claude3Wrapper(client)
    # Read the initial prompt from a text file
    with open("formatted_prompt.txt", "r") as file:
        initial_prompt = file.read()

    loop = True
    while(loop):
        text_prompt = input("Chat: ")
        if(text_prompt.lower() not in EXIT_FUNCTIONS):
            # Invoke Claude 3 with a text prompt
            wrapper.invoke_claude_3_with_text(initial_prompt + "the user said:" + text_prompt)
            print("-" * 88)
        else:
            loop = False

if __name__ == "__main__":
    load_dotenv()
    loop = True
    while(loop):
        url = input("Enter URL: ")
        if(url.lower() not in EXIT_FUNCTIONS):
            scrapeWebsite(url)
            usage_demo()
        else:
            loop = False
        