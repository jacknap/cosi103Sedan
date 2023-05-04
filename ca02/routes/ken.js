const express = require('express');
const router = express.Router();
const GptQuery = require('../models/GptQuery')

const { Configuration, OpenAIApi } = require("openai");
const apiKey = "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" // Set your OpenAI API key here
const configuration = new Configuration({ apiKey: apiKey });
const openai = new OpenAIApi(configuration);


router.get('/index/ken', (req,res,next) => {
    res.render('kenBio');
});

router.get('/gpt/ken', (req,res,next) => {
    res.render('kenInput');
});

router.post('/gpt/ken', async (req,res,next) => {
    res.locals.prompt = req.body.query;
	const gptQuery = new GptQuery(
		{query: req.body.query,
		date: req.body.date,
		userId: req.user._id
		})
	await gptQuery.save();
    res.locals.response = await askGpt(req.body.query);
    res.render('kenResponse');
});

const askGpt = async (query) => {
	let completion = openai.createCompletion({
		model: "text-davinci-003",
		prompt: "Please convert the following code from Python into Java: "+query,
		max_tokens: 1024,
		n: 1,
		temperature: 0.8,
	});
	let response = await completion;
	return response.data.choices[0].text;
}

module.exports = router;
