/*
  jack.js -- Router for the Jack API
*/
const express = require("express");
const router = express.Router();
const GptQuery = require("../models/GptQuery");

const {Configuration, OpenAIApi} = require("openai");
const apiKey = "sk-XXXXX"; // Set your OpenAI API key here
const configuration = new Configuration({apiKey: apiKey});
const openai = new OpenAIApi(configuration);

router.get("/index/jack", (req, res, next) => {
	res.render("jackBio");
});

router.get("/gpt/jack", (req, res, next) => {
	res.render("jackInput");
});

router.post("/gpt/jack", async (req, res, next) => {});

const askGpt = async (query) => {
	let completion = openai.createCompletion({
		model: "text-davinci-003",
		prompt:
			"What is the running time of the following python function in terms of O(n): " +
			query,
		max_tokens: 1024,
		n: 1,
		temperature: 0.8,
	});
	let response = await completion;
	return response.data.choices[0].text;
};

module.exports = router;
