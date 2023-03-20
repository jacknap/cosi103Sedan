# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:48:14 2023

@author: kevinchen
"""

import openai


class GPT():
    ''' make queries to gpt from a given API '''

    def __init__(self, apikey):
        ''' store the apikey in an instance variable '''
        # Set up the OpenAI API client
        openai.api_key = apikey

        # Set up the model and prompt
        self.model_engine = "text-davinci-003"

    def getResponse(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def gettest(self, prompt):
        ''' Generate a GPT response '''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt="Amazon stock price in March 2020",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def kevin_response(self, prompt):
        '''Use GPT to generate travel destinations in a country / place'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Travel destinations in {prompt}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def ken_response(self, prompt):
        '''Use GPT to convert code from Python to Java'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"Please convert the following code from Python into Java: {prompt}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response

    def jack_response(self, prompt):
        '''Use GPT to do a runtime analysis of a python function'''
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=f"What is the running time of the following python function in terms of O(n): {prompt}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )

        response = completion.choices[0].text
        return response


if __name__ == '__main__':
    '''
    '''
    import os
    g = GPT(os.environ.get("APIKEY"))
    print(g.gettest("thing"))
