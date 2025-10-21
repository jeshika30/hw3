import json
import collections
import argparse
import random
import numpy as np
import requests
import re

def your_netid():
    YOUR_NET_ID = 'ej2485'
    return YOUR_NET_ID

def your_hf_token():
    YOUR_HF_TOKEN = 'hf_your_token_here'
    return YOUR_HF_TOKEN


# for adding small numbers (1-6 digits) and large numbers (7 digits), write prompt prefix and prompt suffix separately.
def your_prompt():
    """
    Few-shot prompt to teach Llama-2 how to add 7-digit numbers.
    The idea: Show clear examples with consistent formatting.
    """
    prefix = (
        "You are a helpful assistant that accurately adds large numbers.\n"
        "Follow the examples carefully and output only the result.\n\n"
        "Examples:\n"
        "Q: What is 1234567 + 7654321?\nA: 8888888\n"
        "Q: What is 1000000 + 2000000?\nA: 3000000\n"
        "Q: What is 3456789 + 1111111?\nA: 4567900\n\n"
        "Now answer this:\n"
        "Q: What is "
    )

    suffix = "?\nA: "

    return prefix, suffix


def your_config():
    """Returns a config for prompting api
    Returns:
        For both short/medium, long: a dictionary with fixed string keys.
    Note:
        do not add additional keys. 
        The autograder will check whether additional keys are present.
        Adding additional keys will result in error.
    """
    config = {
        'max_tokens': 60,
        'temperature': 0.3,
        'top_k': 40,
        'top_p': 0.7,
        'repetition_penalty': 1.1,
        'stop': []
    }
    return config


def your_pre_processing(s):
    return s

    
def your_post_processing(output_string):
    """Returns the post processing function to extract the answer for addition
    Returns:
        For: the function returns extracted result
    Note:
        do not attempt to "hack" the post processing function
        by extracting the two given numbers and adding them.
        the autograder will check whether the post processing function contains arithmetic additiona and the graders might also manually check.
    """
    """
    Extract the first integer that appears after model output.
    Handles cases like:
      "A: 8888888"
      "Answer: 8888888."
      "The sum is 8888888"
    """
    matches = re.findall(r"\d+", output_string)
    if matches:
        try:
            return int(matches[0])
        except:
            return 0
    return 0

