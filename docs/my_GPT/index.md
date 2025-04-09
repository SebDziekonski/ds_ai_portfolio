🧠 My GPT – A Personalized AI Chatbot App
NaszGPT is a Streamlit-based chatbot application that connects to OpenAI’s GPT models (like GPT-4o) to provide intelligent, conversational responses. It’s designed for users who want a customizable and cost-transparent AI assistant experience.

✨ Key Features
Interactive Chat Interface
Chat with an AI assistant that remembers context and responds naturally.

Customizable Personality
Set the chatbot’s tone and behavior to suit your preferences.

Conversation Management
Save, rename, and switch between multiple conversations with history tracking.

Cost Monitoring
Real-time display of conversation costs in USD and PLN, based on actual token usage.

Local Storage
All conversations are stored securely in local JSON files for easy access and persistence.

🛠️ Built With
Streamlit – For the user interface

OpenAI API – For AI-generated responses

Python + JSON – For data handling and local storage

dotenv – For secure API key management

Link to see for your self how the application works:

https://github.com/SebDziekonski/ds_ai_portfolio.git

<iframe
    id="content"
    width="100%"
    style="border:1px solid black;overflow:hidden;"
></iframe>
<script>
function resizeIframeToFitContent(iframe) {
    iframe.style.height = (iframe.contentWindow.document.documentElement.scrollHeight + 50) + "px";
    iframe.contentDocument.body.style["overflow"] = 'hidden';
}
window.addEventListener('load', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
window.addEventListener('resize', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
</script>