import React, { useState, useEffect } from 'react';
import './form.css'
const NameForm = () => {
  const [data, setData] = useState([]);
  const [query, setQuery] = useState('nike socks');
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
    const [itemDict, setDict] = useState({})
   
  const [occasion, setOccasion] = useState("")
  const [celebrity, setCelebrity] = useState("")
  const [price, setPrice] = useState("")
  const [season, setSeason] = useState("")
 
 

  // Handling form submission
  const  handleSubmit =  async (event) => {
   
    let specificPrompt = `List specific clothing articles by brand to create an outfit for a ${occasion}, during the ${season}, under ${price} dollars, and based off of ${celebrity} seperated by commas`
    console.log()
    setSubmitted(true)
    setLoading(true)
    const response = await openai.createCompletion({

        model: "text-davinci-003",

        //prompt: "List 3 articles of clothing based off lebron james' style",
        prompt: specificPrompt,
        // each token is about 4 characters

        max_tokens: 100,

        temperature: 0,

    });
   
    //console.log(response.data.choices[0].text)
    const text = response.data.choices[0].text
    let split = text.split(",")
    console.log(split)
     // insert new key from = to cx (include &)
    var itemDict = {}
    // var googleapikey= a;
    for (let i = 0; i < split.length; i++) {
        let itemString = split[i]
        const res = await fetch(
            `https://www.googleapis.com/customsearch/v1?key=AIzaSyCbjpfGKScSURcaUJPe_ud6drieZFKBbPo&cx=f0aec48937b8f4a5a&q=${itemString}`
          );
          const json = await res.json();
            itemDict[itemString] = json.items[0].link
       }
       console.log("yaaaaaaa")
   
    setDict(itemDict)

    //console.log(split)

    // console.log(text)
    // const res = await fetch(
    //     `https://www.googleapis.com/customsearch/v1?key=AIzaSyAP_de780D8ciji7TC1LBKqRnWHo6Tqa9k&cx=277268e1202384f8b&q=${text}`
    //   );
    //   const json = await res.json();
    //   setData(json.items);

    setLoading(false)
    console.log("yayyyyyyyyyy")
   

    /*
    // call the GPT3 api with the query string
    const text =  callApi()
    console.log("aaaaaaaaaaaaaaaaaaa")
    console.log(text)

    // dsparks gpt key : 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

    // call google api with the result from gpt3
    fetchData(text)

   
    console.log('aslk;dfjas;lkdfjlkj;')
    setSubmitted(true)
    console.log(data)
    */

   
  }

    //////////////////// GPT3 //////////////////////////////////////////////////
    const { Configuration, OpenAIApi } = require("openai");

    const configuration = new Configuration({

        organization: "org-LCH831EKRQfTemslq6pe8Gmh",

        apiKey: "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",

    });

    const openai = new OpenAIApi(configuration);

   

    async function callApi() {

        const response = await openai.createCompletion({

            model: "text-davinci-003",

            prompt: "tell me a short story in 100 words",

            // each token is about 4 characters

            max_tokens: 100,

            temperature: 0,

        });
       
        //console.log(response.data.choices[0].text)
        const text = response.data.choices[0].text

        return text

    }

    ///////////////////////////////////////////////////////////



    ////////////Google API /////////////////////////////////////////////////
  const fetchData = async (query) => {
      //setLoading(true);
      // THIS GOOGLE KEY IS WHERE WE GO SO IF THINGS STOP WORKING
      const res = await fetch(
        `https://www.googleapis.com/customsearch/v1?key=AIzaSyCbjpfGKScSURcaUJPe_ud6drieZFKBbPo&cx=d2e35566790364c73&q=${query}`
      );
      const json = await res.json();
      setData(json.items);
      //setLoading(false);
    };
    //fetchData();
    //setSubmitted(true);
    ////////////////////////////////////////////////////////

    //Conditional returns
  if(!submitted){
    return (
        
        <div class="login-box">
            <h2 class >Get Dripped</h2>
            {/* <h3> find your next iconic outfit in seconds</h3> */}
            <h2 style = {{fontSize:12}}>find your next iconic outfit in seconds</h2>
            <form onSubmit={handleSubmit}>
                <div class="user-box">
                <input
                  type="text"
                  name="occasion"
                  id="occasion"
                  onChange={(event) =>
                    setOccasion(event.target.value)
                  }
                  //ref={node => (this.inputNode = node)}
                />
                <label>Occasion</label>
                </div>
                <div class="user-box">
                <input
                  type="text"
                  name="price"
                  onChange={(event) =>
                    setPrice(event.target.value.toString())
                  }
                  //ref={node => (this.inputNode = node)}
                />
                <label>Max Price</label>
                </div>

                <div class="user-box">
                <input
                  type="text"
                  name="season"
                  onChange={(event) =>
                    setSeason(event.target.value)
                  }
                  //ref={node => (this.inputNode = node)}
                />
                <label>Season</label>
                </div>
               
                <div class = "user-box">
               
                <input
                  type="text"
                  name="celebrity"
                  onChange={(event) =>
                    setCelebrity(event.target.value)
                  }
                  //ref={node => (this.inputNode = node)}
                />
                <label>Celebrity Influence</label>
                </div>
               

               
                <a onClick={handleSubmit}>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Submit
                </a>
               
            </form>
            </div>


       
      );
  }


  else{
    return(
        <div>
          {loading ? (
            <div>Loading...</div>
          ) : (
            <ul>
      {Object.entries(itemDict).map(([key, value], index) => (
        <li key={index} style={{padding: '10px'}}>
          <strong>{key}:</strong> <a href={value} style={{color: 'white'}}>{value}</a>
          <br></br>
        </li>
      ))}
    </ul>
           
          )}
        </div>
    )
  }
 
};

export default NameForm;
