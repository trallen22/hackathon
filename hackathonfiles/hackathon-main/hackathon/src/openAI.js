const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
    organization: "org-bc7fCUYhKAertCqdDbhen40D",
    apiKey: "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",
});
const openai = new OpenAIApi(configuration);

export async function callApi() {
    const response = await openai.createCompletion({
        model: "text-davinci-003",
        prompt: "tell me a short story in 100 words",
        // each token is about 4 characters 
        max_tokens: 100,
        temperature: 0,
      });
    console.log(response.data.choices[0].text)
}
