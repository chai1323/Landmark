import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();



// import React, { useEffect, useRef, useState } from 'react'

// const useSpeechToText = ( options ={}) => {
//     const [isListening,setIsListening]=useState(false);
//     const [transcript,setTranscript]=useState("");
//     const recognitionRef = useRef(null)

//     useEffect(()=>{
//         if(!('webkitSpeechRecognition' in window)){
//             console.error("web speech is not supported")
//             return;
//         }
//         recognitionRef.current = new window.webkitSpeechRecognition()
//         const recognition = recognitionRef.current
//         recognition.interimResults = options.interimResults || true 
//         recognition.lang = options.lang || "en-US"
//         recognition.continuous = options.continuous || false
//         if("webkitSpeechGrammarList" in window){
//             const grammar = "#JSGF V1.0; grammar punctuation; public <punc> = . | , | ? | ! | ; | : ;"
//             const speechRecognitionList = new window.webkitSpeechGrammarList()
//             speechRecognitionList.addFromString(grammar ,1)
//             recognition.grammars = speechRecognitionList
//         }

//         recognition.onresult = (event) =>{
//             let text=""
//             for(let i=0;i<event.results.length;i++){
//                 text+=event.results[i][0].transcript
//             }
//             setTranscript(text);
//         }

//         recognition.error = (event)=>{
//             console.error("speech recognition error",event.error)
//         }

//         recognition.onend=()=>{
//             setIsListening(false);
//             setTranscript("")
//         }

//         return ()=>{
//             recognition.stop()
//         }
//     },[])

//     const startListening = () => {
//         if(recognitionRef.current && !isListening){
//             recognitionRef.current.start();
//             setIsListening(true);
//         }
//     }

//     const stopListening = () => {
//         if(recognitionRef.current && isListening) {
//             recognitionRef.current.stop()
//             setIsListening(false);
//         }
//     }

//     return {
//         isListening,
//         transcript,
//         startListening,
//         stopListening
//     }
// }

// export default useSpeechToText;
