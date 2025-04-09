🧠 My GPT – A Personalized AI Chatbot App
NaszGPT is a Streamlit-based chatbot application that connects to OpenAI’s GPT models (like GPT-4o) to provide intelligent, conversational responses. It’s designed for users who want a customizable and cost-transparent AI assistant experience.

<iframe
    id="content"
    src="app.py"
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