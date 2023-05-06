/*
  jack.js -- Router for jack's pages
*/
const express = require("express");
const router = express.Router();
const GptQuery = require("../models/GptQuery");
// const axios = require("axios");

const {Configuration, OpenAIApi} = require("openai");
const apiKey = "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"; // Set your OpenAI API key here
const configuration = new Configuration({apiKey: apiKey});
const openai = new OpenAIApi(configuration);

router.get("/index/jack", (req, res, next) => {
	res.render("jackBio");
});

router.get("/gpt/jack", (req, res, next) => {
	res.render("jackInput");
});

router.post("/gpt/jack", async (req, res, next) => {
	res.locals.prompt = req.body.query;
	const gptQuery = new GptQuery({
		query: req.body.query,
		date: req.body.date,
		userId: req.user._id,
	});
	await gptQuery.save();
	res.locals.response = await askGpt(req.body.query);
	const newQuery = new QueryItem({
		prompt: v,
		response: await askGpt(v),
		userId: req.user._id,
	});
	await newQuery.save();
	res.render("jackResponse");
});

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
