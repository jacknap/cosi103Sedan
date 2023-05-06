const express = require('express');
const router = express.Router();
const GptQuery = require('../models/GptQuery')

const { Configuration, OpenAIApi } = require("openai");
const QueryItem = require('../models/QueryItem');
const apiKey = "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" // Set your OpenAI API key here
const configuration = new Configuration({ apiKey: apiKey });
const openai = new OpenAIApi(configuration);


router.get('/index/kevin', (req,res,next) => {
    res.render('kevinBio');
});

router.get('/gpt/kevin', (req,res,next) => {
    res.render('kevinInput');
});

router.post('/gpt/kevin', async (req,res,next) => {
    res.locals.prompt = req.body.query;
	const gptQuery = new GptQuery(
		{query: req.body.query,
		date: req.body.date,
		userId: req.user._id
		})
	await gptQuery.save();
	let v = req.body.query
    res.locals.response = await askGpt(req.body.query);
   // console.log('res.locals.response:', res.locals.response);
	console.log('fiwub')

	const thing = new QueryItem(
		{input: res.locals.prompt,
		output: res.locals.response,
		userId: req.user._id
	  })
	  
	await thing.save();
	
	res.locals.entry = thing
	
	
    res.render('kevinResponse');
});

const askGpt = async (query) => {
	let completion = openai.createCompletion({
		model: "text-davinci-003",
		prompt: "Please give some tourist destinations for : "+query,
		max_tokens: 1024,
		n: 1,
		temperature: 0.8,
	});
	let response = await completion;
    
	return response.data.choices[0].text;
}

module.exports = router;
